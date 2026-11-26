#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry."""
import os

WORD = "buffering"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)

if __name__ == "__main__":
    main()
