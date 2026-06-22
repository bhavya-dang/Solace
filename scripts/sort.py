#!/usr/bin/env python3

import json
from collections import OrderedDict
from pathlib import Path

THEME_FILE = Path("themes/solace.json")


def sort_style(style):
    result = OrderedDict()

    # Keep players first
    if "players" in style:
        result["players"] = style["players"]

    for key in sorted(k for k in style if k != "players"):
        result[key] = style[key]

    return result


with open(THEME_FILE) as f:
    data = json.load(f)

sorted_themes = []

for theme in data["themes"]:
    sorted_theme = OrderedDict()

    for key in ("name", "appearance"):
        if key in theme:
            sorted_theme[key] = theme[key]

    if "style" in theme:
        sorted_theme["style"] = sort_style(theme["style"])

    for key in sorted(k for k in theme if k not in {"name", "appearance", "style"}):
        sorted_theme[key] = theme[key]

    sorted_themes.append(sorted_theme)

data["themes"] = sorted_themes

with open(THEME_FILE, "w") as f:
    json.dump(data, f, indent=2)
    f.write("\n")

print(f"Sorted {THEME_FILE}")
