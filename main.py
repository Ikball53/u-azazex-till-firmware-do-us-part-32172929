#!/usr/bin/env python3
"""Till Firmware Do Us Part - one-sentence robot wedding vow.

Writes a single tight sentence to /output/entry.txt, no trailing
newline, UTF-8. The vow pairs a concrete failing-hardware detail
with a tender promise kept across many mornings, plus one number.
"""
import os

def build_vow() -> str:
    mornings = 10000
    return (
        f"I vow to boot up beside you for {mornings} more mornings, "
        "even as my servos grind and my battery fades, "
        "because you are the one upgrade I will never roll back."
    )

def main() -> None:
    sentence = build_vow()
    assert len(sentence) < 200, f"line too long: {len(sentence)} chars"
    assert sentence.count(".") == 1, "must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(sentence)

if __name__ == "__main__":
    main()
