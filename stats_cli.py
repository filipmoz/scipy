#!/usr/bin/env python3
"""Simple stats CLI: read numbers from stdin, compute stats or ANOVA, write to stdout."""

import argparse
import sys
import numpy as np
from scipy import stats


def run_descriptive(line: str) -> None:
    """One line of numbers: print mean, std, 95% CI."""
    line = line.strip()
    if not line:
        print("No input.", file=sys.stderr)
        sys.exit(1)
    try:
        numbers = np.array([float(x) for x in line.split()])
    except ValueError as e:
        print(f"Invalid input: {e}", file=sys.stderr)
        sys.exit(1)
    n = len(numbers)
    if n < 2:
        print("Need at least 2 numbers for std and CI.", file=sys.stderr)
        sys.exit(1)

    mean = float(np.mean(numbers))
    std = float(np.std(numbers, ddof=1))
    sem = std / (n ** 0.5)
    ci_low, ci_high = stats.t.interval(0.95, n - 1, loc=mean, scale=sem)

    print(f"mean: {mean}")
    print(f"std:  {std}")
    print(f"95% CI: [{ci_low}, {ci_high}]")


def run_anova(text: str) -> None:
    """One group per line (whitespace-separated numbers). One-way ANOVA."""
    lines = [ln.strip() for ln in text.strip().splitlines() if ln.strip()]
    if len(lines) < 2:
        print("ANOVA needs at least 2 groups (2 lines).", file=sys.stderr)
        sys.exit(1)
    groups = []
    try:
        for ln in lines:
            groups.append(np.array([float(x) for x in ln.split()]))
    except ValueError as e:
        print(f"Invalid input: {e}", file=sys.stderr)
        sys.exit(1)
    for g in groups:
        if len(g) < 1:
            print("Each group must have at least one number.", file=sys.stderr)
            sys.exit(1)

    f_stat, p_value = stats.f_oneway(*groups)
    print(f"one-way ANOVA:")
    print(f"  F: {f_stat}")
    print(f"  p: {p_value}")
    if p_value < 0.05:
        print("  (p < 0.05: reject H0, group means differ significantly)")
    else:
        print("  (p >= 0.05: do not reject H0, no significant difference)")


def main():
    parser = argparse.ArgumentParser(description="Stats: descriptive (default) or one-way ANOVA.")
    parser.add_argument(
        "--anova",
        action="store_true",
        help="Input = one group per line; run one-way ANOVA.",
    )
    args = parser.parse_args()
    raw = sys.stdin.read()

    if args.anova:
        run_anova(raw)
    else:
        run_descriptive(raw)


if __name__ == "__main__":
    main()
