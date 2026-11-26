#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one line (at most 200 characters): the phone battery's final
text message to the charger it waited for all day.
"""
from pathlib import Path

TEXT = (
    "You said 'in a bit' at 9am. It's midnight, I'm at 1%, and "
    "you're still across the room. So I'm leaving you for the power "
    "bank in my bag \u2014 he actually shows up. Goodbye. Don't text "
    "back, I'll be dead."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = TEXT.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
