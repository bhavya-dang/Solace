#!/usr/bin/env sh
set -eu

if [ -n "${APPDATA:-}" ]; then
  THEMES_DIR="${APPDATA}/Zed/themes"
else
  THEMES_DIR="${HOME}/.config/zed/themes"
fi

mkdir -p "$THEMES_DIR"

URL="https://raw.githubusercontent.com/bhavya-dang/Solace/refs/heads/master/themes/solace.json"

if command -v curl > /dev/null 2>&1; then
  curl -fsSL -o "$THEMES_DIR/solace.json" "$URL"
elif command -v wget > /dev/null 2>&1; then
  wget -q -O "$THEMES_DIR/solace.json" "$URL"
else
  echo "Error: curl or wget required"
  exit 1
fi

echo "Installed Solace theme to $THEMES_DIR/solace.json"
