#!/usr/bin/env python3
"""
install.py — Shanghai Unemployment Advisor Skill Installer
Supports macOS, Windows, and Linux.

Installs the skill into any agent skills directory.
Common paths by agent:
  Cursor (global)      : ~/.cursor/skills/
  Cursor (project)     : .cursor/skills/
  Claude Code (global) : ~/.claude/skills/
  Claude Code (project): .claude/skills/

Usage:
    python install.py
"""

import os
import sys
import shutil
import platform
from pathlib import Path

SKILL_NAME = "shanghai-unemployment-advisor"
SKILL_DIR  = Path(__file__).parent / SKILL_NAME


# ── Terminal colours ──────────────────────────────────────────────────────────

def _supports_colour() -> bool:
    if platform.system() == "Windows":
        return (
            "ANSICON" in os.environ
            or "WT_SESSION" in os.environ
            or os.environ.get("TERM_PROGRAM") == "vscode"
        )
    return sys.stdout.isatty()

USE_COLOUR = _supports_colour()

def _c(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if USE_COLOUR else text

def green(t):  return _c("32", t)
def yellow(t): return _c("33", t)
def cyan(t):   return _c("36", t)
def bold(t):   return _c("1",  t)
def red(t):    return _c("31", t)


# ── Helpers ───────────────────────────────────────────────────────────────────

def home() -> Path:
    if platform.system() == "Windows":
        return Path(os.environ.get("USERPROFILE", Path.home()))
    return Path.home()


def ask(prompt: str, choices: list[str], default: str) -> str:
    choice_str = "/".join(c.upper() if c == default else c for c in choices)
    while True:
        raw = input(f"{prompt} [{choice_str}]: ").strip().lower()
        if raw == "":
            return default
        if raw in [c.lower() for c in choices]:
            return raw
        print(red(f"  Please enter one of: {', '.join(choices)}"))


def ask_path(prompt: str, default: Path) -> Path:
    raw = input(f"{prompt} [{default}]: ").strip()
    return Path(raw).expanduser() if raw else default


def install_skill(target_dir: Path) -> None:
    dest = target_dir / SKILL_NAME

    if dest.exists():
        print(yellow(f"\n  ⚠  Skill already exists at:\n     {dest}"))
        overwrite = ask("  Overwrite?", ["y", "n"], "n")
        if overwrite != "y":
            print("  Skipped — no changes made.")
            return
        shutil.rmtree(dest)

    target_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n  Copying skill to:\n  {cyan(str(dest))}")
    shutil.copytree(SKILL_DIR, dest)
    print(green("\n  ✓ Skill installed successfully!\n"))
    print(bold("  Quick start — ask your agent:"))
    print(cyan('  "上海失业金怎么领？" / "我被裁员了社保怎么处理？"\n'))


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    print()
    print(bold("╔══════════════════════════════════════════════════════╗"))
    print(bold("║   Shanghai Unemployment Advisor — Skill Installer    ║"))
    print(bold("╚══════════════════════════════════════════════════════╝"))
    print(f"\n  OS    : {cyan(platform.system())} ({platform.machine()})")
    print(f"  Skill : {cyan(SKILL_NAME)}")

    if not SKILL_DIR.exists():
        print(red(f"\n  ✗ Skill source not found: {SKILL_DIR}"))
        print(red("  Run install.py from the repository root."))
        sys.exit(1)

    # ── Reference table ───────────────────────────────────────────────────
    print()
    print(bold("  Common agent skills paths:"))
    entries = [
        ("Cursor",      "global",  "~/.cursor/skills/"),
        ("Cursor",      "project", ".cursor/skills/"),
        ("Claude Code", "global",  "~/.claude/skills/"),
        ("Claude Code", "project", ".claude/skills/"),
    ]
    for agent, scope, path in entries:
        print(f"    {agent:<14} {scope:<9} {cyan(path)}")

    # ── Scope choice ──────────────────────────────────────────────────────
    print()
    print(bold("  Install scope:"))
    print(f"  {bold('g')} — Global   (user home, available across all projects)")
    print(f"  {bold('p')} — Project  (current directory, shareable via git)")
    print(f"  {bold('c')} — Custom   (enter any path)")
    print()

    scope = ask("  Scope", ["g", "p", "c", "q"], "g")

    if scope == "q":
        print("\n  Cancelled.\n")
        sys.exit(0)

    if scope == "g":
        default_dir = home() / ".skills"
        target = ask_path("  Global skills directory", default_dir)
    elif scope == "p":
        default_dir = Path.cwd() / "skills"
        target = ask_path("  Project skills directory", default_dir)
    else:
        target = ask_path("  Enter destination path", home() / ".skills")

    install_skill(target)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Cancelled.\n")
        sys.exit(0)
