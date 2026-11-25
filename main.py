#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry.

Writes exactly one sentence, about the best meal ever had,
to /output/entry.txt. Deterministic: the same sentence every run.
"""

import os

SENTENCE = (
    "My grandmother's soto ayam at a Jakarta street stall \u2014 "
    "turmeric broth, shredded chicken, lime squeezed over the top "
    "\u2014 still tastes like the whole city stopping to feed me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
