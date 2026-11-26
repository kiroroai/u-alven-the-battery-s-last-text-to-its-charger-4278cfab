#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one line (at most 200 characters): the phone battery's final
text message to the charger it waited for all day.
"""
from pathlib import Path

TEXT = (
    "All day I sat at 1% waiting for you to plug me in. "
    "You never came. So I'm leaving you \u2014 for the power bank "
    "in my owner's bag. He shows up. Goodbye, and don't text back, "
    "I'll be dead."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = TEXT.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
