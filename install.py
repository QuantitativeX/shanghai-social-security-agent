#!/usr/bin/env python3
"""
install.py — Shanghai Unemployment Advisor Skill Installer
Supports macOS, Windows, and Linux.

Usage:
    python install.py
"""

import os
import sys
import shutil
import platform
from pathlib import Path

SKILL_NAME = "shanghai-unemployment-advisor"
SKILL_DIR = Path(__file__).parent / SKILL_NAME


# ── Terminal colours (disabled on Windows unless ANSICON/WT is detected) ──────

def _supports_colour() -> bool:
    if platform.system() == "Windows":
        return (
            "ANSICON" in os.environ
            or "WT_SESSION" in os.environ          # Windows Terminal
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

def ask(prompt: str, choices: list[str], default: str) -> str:
    """Prompt the user and return their validated choice."""
    choice_str = "/".join(
        c.upper() if c == default else c for c in choices
    )
    while True:
        raw = input(f"{prompt} [{choice_str}]: ").strip().lower()
        if raw == "":
            return default
        if raw in [c.lower() for c in choices]:
            return raw
        print(red(f"  Please enter one of: {', '.join(choices)}"))


def global_skills_dir() -> Path:
    """Return the global Cursor skills directory for the current OS."""
    system = platform.system()
    if system == "Windows":
        base = Path(os.environ.get("USERPROFILE", Path.home()))
    else:
        base = Path.home()
    return base / ".cursor" / "skills"


def project_skills_dir() -> Path:
    """Return the project-level Cursor skills directory (cwd-relative)."""
    return Path.cwd() / ".cursor" / "skills"


def install_skill(target_dir: Path) -> None:
    """Copy the skill folder into target_dir, with overwrite confirmation."""
    dest = target_dir / SKILL_NAME

    if dest.exists():
        print(yellow(f"\n  ⚠  Skill already exists at:\n     {dest}"))
        overwrite = ask("  Overwrite?", ["y", "n"], "n")
        if overwrite != "y":
            print("  Skipped — no changes made.")
            return
        shutil.rmtree(dest)

    print(f"\n  Copying skill to:\n  {cyan(str(dest))}")
    shutil.copytree(SKILL_DIR, dest)
    print(green("\n  ✓ Skill installed successfully!\n"))

    # Print quick-start hint
    print(bold("  Quick start:"))
    print("  Open any project in Cursor and ask something like:")
    print(cyan('  "上海失业金怎么领？" or "我被裁员了社保怎么办？"\n'))


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    print()
    print(bold("╔══════════════════════════════════════════════════════╗"))
    print(bold("║   Shanghai Unemployment Advisor — Skill Installer    ║"))
    print(bold("╚══════════════════════════════════════════════════════╝"))
    print(f"\n  Detected OS : {cyan(platform.system())} ({platform.machine()})")
    print(f"  Skill       : {cyan(SKILL_NAME)}")

    # Verify source skill exists
    if not SKILL_DIR.exists():
        print(red(f"\n  ✗ Skill source not found at:\n    {SKILL_DIR}"))
        print(red("  Make sure you run install.py from the repository root."))
        sys.exit(1)

    print()
    print(bold("  Where would you like to install the skill?"))
    print(f"  {bold('g')} — Global  {cyan(str(global_skills_dir() / SKILL_NAME))}")
    print(f"      Available in ALL your Cursor projects")
    print(f"  {bold('p')} — Project {cyan(str(project_skills_dir() / SKILL_NAME))}")
    print(f"      Available only in the current project (shared via git)")
    print()

    choice = ask("  Install location", ["g", "p", "q"], "g")

    if choice == "q":
        print("\n  Cancelled.\n")
        sys.exit(0)

    target = global_skills_dir() if choice == "g" else project_skills_dir()
    target.mkdir(parents=True, exist_ok=True)

    install_skill(target)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Cancelled.\n")
        sys.exit(0)
