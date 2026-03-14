#!/usr/bin/env python3
"""
Fetch policy content from a given URL for the Shanghai Unemployment Advisor skill.

Usage:
    python scripts/fetch_policy.py "<URL>"
    python scripts/fetch_policy.py "<URL1>" "<URL2>" ...   # fetch multiple URLs

Returns plain text content extracted from the webpage.
Handles Chinese government sites and news portals commonly used in source.md.

Some sites (e.g. m12333.cn) have bot protection and may return 4xx errors.
In that case the script prints a clear error message so the skill knows to
try a different URL or tell the user to visit the link directly.
"""

import sys
import urllib.request
import urllib.error
import html
import re
import time


# Extended headers that pass basic bot-detection checks on Chinese gov portals
BASE_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "identity",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0",
}


def fetch_url(url: str, timeout: int = 20, retry: int = 2) -> str:
    """Fetch a URL and return cleaned text content."""
    last_error = ""
    for attempt in range(retry):
        if attempt > 0:
            time.sleep(1.5)
        req = urllib.request.Request(url, headers=BASE_HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                raw = response.read()
                # Try common Chinese encodings in order
                for encoding in ("utf-8", "gb18030", "gbk", "gb2312", "utf-8-sig"):
                    try:
                        content = raw.decode(encoding)
                        break
                    except (UnicodeDecodeError, LookupError):
                        continue
                else:
                    content = raw.decode("utf-8", errors="replace")
                return extract_text(content, url)

        except urllib.error.HTTPError as e:
            last_error = f"HTTP {e.code} {e.reason}"
            # 412/403 = bot protection, no point retrying with same headers
            if e.code in (412, 403, 401):
                break
        except urllib.error.URLError as e:
            last_error = f"连接错误: {e.reason}"
        except Exception as e:
            last_error = f"{type(e).__name__}: {e}"

    # Return a helpful error rather than crashing
    tips = ""
    if "412" in last_error or "403" in last_error:
        tips = (
            "\n\n提示：该网站启用了访问保护，自动抓取受阻。"
            "\n建议：\n"
            "  1. 请用户直接打开浏览器访问该链接\n"
            "  2. 或尝试 source.md 中的其他相关链接"
        )
    return f"[抓取失败] {last_error}\nURL: {url}{tips}"


def extract_text(html_content: str, url: str = "") -> str:
    """Extract readable Chinese text from HTML."""
    # Drop script / style / comment blocks
    html_content = re.sub(
        r"<(script|style|noscript)[^>]*>.*?</\1>",
        "",
        html_content,
        flags=re.DOTALL | re.IGNORECASE,
    )
    html_content = re.sub(r"<!--.*?-->", "", html_content, flags=re.DOTALL)

    # Convert block-level elements to newlines before stripping tags
    html_content = re.sub(r"<br\s*/?>", "\n", html_content, flags=re.IGNORECASE)
    html_content = re.sub(
        r"</?(?:p|div|li|ul|ol|h[1-6]|tr|td|th|section|article|header|footer|nav|main|aside)[^>]*>",
        "\n",
        html_content,
        flags=re.IGNORECASE,
    )

    # Strip all remaining tags
    text = re.sub(r"<[^>]+>", "", html_content)

    # Decode HTML entities (&amp; &lt; &#x4e2d; etc.)
    text = html.unescape(text)

    # Normalise whitespace
    lines: list[str] = []
    for line in text.splitlines():
        line = re.sub(r"[ \t\u3000]+", " ", line).strip()
        if line:
            lines.append(line)

    # Collapse excess blank lines
    result_lines: list[str] = []
    blank_run = 0
    for line in lines:
        if not line:
            blank_run += 1
            if blank_run <= 1:
                result_lines.append("")
        else:
            blank_run = 0
            result_lines.append(line)

    text = "\n".join(result_lines).strip()

    # Truncate long pages — first 8000 chars covers most policy articles
    max_chars = 8000
    if len(text) > max_chars:
        text = text[:max_chars] + f"\n\n...[内容过长，已截断至 {max_chars} 字符，如需完整内容请直接访问链接]"

    if len(text) < 100:
        return (
            f"[内容提取失败] 页面可能需要 JavaScript 渲染、已失效或需要登录。\n"
            f"URL: {url}\n"
            f"建议直接用浏览器访问该链接。"
        )

    header = f"=== 来源: {url} ===\n\n"
    return header + text


def safe_print(text: str) -> None:
    """Print text handling Windows console encoding gracefully."""
    try:
        sys.stdout.buffer.write((text + "\n").encode("utf-8"))
        sys.stdout.buffer.flush()
    except AttributeError:
        # Fallback for environments without buffer attribute
        print(text.encode("utf-8", errors="replace").decode("utf-8", errors="replace"))


def main():
    if len(sys.argv) < 2:
        print("用法: python scripts/fetch_policy.py \"<URL>\" [\"<URL2>\" ...]", file=sys.stderr)
        print("示例: python scripts/fetch_policy.py \"https://m.sh.bendibao.com/zffw/288778.html\"", file=sys.stderr)
        sys.exit(1)

    urls = [u.strip().strip('"').strip("'") for u in sys.argv[1:]]
    results = []
    for url in urls:
        if not url.startswith(("http://", "https://")):
            results.append(f"[错误] 无效URL（需以 http:// 或 https:// 开头）: {url}")
            continue
        results.append(fetch_url(url))

    safe_print("\n\n" + "="*60 + "\n\n".join(results))


if __name__ == "__main__":
    main()
