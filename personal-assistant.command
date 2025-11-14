#!/usr/bin/env bash
set -euo pipefail
cd "$(cd "$(dirname "$0")" && pwd)"

# Try to set a larger, portrait-oriented window size (macOS Terminal)
# Adjusts the front window bounds to be taller than wide.
# Guarded with try so it won't fail on systems where AppleScript is restricted.
osascript <<'OSA' >/dev/null 2>&1 || true
tell application "Terminal"
  try
    set w to front window
    set b to bounds of w
    set leftPos to item 1 of b
    set topPos to item 2 of b
    set newWidth to 900
    set newHeight to 1200
    set bounds of w to {leftPos, topPos, leftPos + newWidth, topPos + newHeight}
  end try
end tell
OSA

# Clear screen and scrollback so our banner is the first visible line
printf '\e[3J\e[H\e[2J'

# Prefer local venv if present
if [[ -x .venv/bin/python ]]; then
  PY=.venv/bin/python
elif command -v python3 >/dev/null 2>&1; then
  PY=python3
else
  PY=python
fi

"$PY" main.py
status=$?

echo
read -n 1 -s -r -p "Press any key to close..."
exit $status