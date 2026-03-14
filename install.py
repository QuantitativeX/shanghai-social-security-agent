#!/usr/bin/env python3
"""
install.py — Shanghai Unemployment Advisor Skill Installer
Supports macOS, Windows, and Linux.

Supported agents:
  Cursor     global  : ~/.cursor/skills/
  Cursor     project : .cursor/skills/
  Claude Code global : ~/.claude/skills/
  Claude Code project: .claude/skills/
  Lingma     global  : ~/.lingma/skills/
  Lingma     project : .lingma/skills/

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

# Agent definitions: (display name, key, global subdir, project subdir)
AGENTS = [
    ("Cursor",      "1", ".cursor/skills",  ".cursor/skills"),
    ("Claude Code", "2", ".claude/skills",  ".claude/skills"),
    ("Lingma",      "3", ".lingma/skills",  ".lingma/skills"),
    ("Custom",      "4", None,              None),
]


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
def dim(t):    return _c("2",  t)


# ── Helpers ───────────────────────────────────────────────────────────────────

def home() -> Path:
    if platform.system() == "Windows":
        return Path(os.environ.get("USERPROFILE", Path.home()))
    return Path.home()


def ask(prompt: str, choices: list[str], default: str) -> str:
    """Prompt for a single-character choice, return lower-cased result."""
    choice_str = "/".join(c.upper() if c == default else c for c in choices)
    while True:
        raw = input(f"{prompt} [{choice_str}]: ").strip().lower()
        if raw == "":
            return default.lower()
        if raw in [c.lower() for c in choices]:
            return raw
        print(red(f"  Please enter one of: {', '.join(choices)}"))


def ask_path(prompt: str, default: Path) -> Path:
    raw = input(f"{prompt}\n  [{default}]: ").strip()
    return Path(raw).expanduser() if raw else default


def install_skill(target_dir: Path) -> None:
    """Copy skill into target_dir/SKILL_NAME, with overwrite confirmation."""
    dest = target_dir / SKILL_NAME

    if dest.exists():
        print(yellow(f"\n  ⚠  Skill already exists at:\n     {dest}"))
        overwrite = ask("  Overwrite?", ["y", "n"], "n")
        if overwrite != "y":
            print("  Skipped — no changes made.")
            return
        shutil.rmtree(dest)

    target_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n  Installing to:\n  {cyan(str(dest))}")
    shutil.copytree(SKILL_DIR, dest)
    print(green("\n  ✓ Installed successfully!\n"))
    print(bold("  Quick start — ask your agent:"))
    print(cyan('  "上海失业金怎么领？"'))
    print(cyan('  "我被裁员了，社保怎么处理？"\n'))


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

    # ── Step 1: choose agent ──────────────────────────────────────────────
    print()
    print(bold("  Step 1 — Choose your agent:"))
    print()
    for name, key, global_sub, project_sub in AGENTS:
        if global_sub:
            global_path  = dim(f"~/{global_sub}/")
            project_path = dim(f"./{project_sub}/")
            print(f"  {bold(key)}) {name:<14} "
                  f"global {global_path}  |  project {project_path}")
        else:
            print(f"  {bold(key)}) {name:<14} (enter any path manually)")
    print()
    print(f"  {bold('q')}) Quit")
    print()

    agent_keys = [a[1] for a in AGENTS] + ["q"]
    agent_choice = ask("  Agent", agent_keys, "1")

    if agent_choice == "q":
        print("\n  Cancelled.\n")
        sys.exit(0)

    selected = next(a for a in AGENTS if a[1] == agent_choice)
    agent_name, _, global_sub, project_sub = selected

    # ── Step 2: choose scope ──────────────────────────────────────────────
    if global_sub is None:
        # Custom path — skip scope question
        target = ask_path(
            "  Enter the full destination directory path:",
            home() / ".skills"
        )
    else:
        print()
        print(bold(f"  Step 2 — Install scope for {agent_name}:"))
        print()
        global_dir  = home() / global_sub
        project_dir = Path.cwd() / project_sub
        print(f"  {bold('g')} — Global   {cyan(str(global_dir))}")
        print(f"      Available across all your projects")
        print(f"  {bold('p')} — Project  {cyan(str(project_dir))}")
        print(f"      Current directory only, shareable via git")
        print()

        scope = ask("  Scope", ["g", "p", "q"], "g")

        if scope == "q":
            print("\n  Cancelled.\n")
            sys.exit(0)

        target = global_dir if scope == "g" else project_dir

    # ── Step 3: install ───────────────────────────────────────────────────
    install_skill(target)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Cancelled.\n")
        sys.exit(0)
