#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow, one sentence."""

from pathlib import Path

LINE = "I vow to reboot beside you for the next 10,000 mornings, even when my battery reads 1% and my sensors forget your name."


def main() -> None:
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
