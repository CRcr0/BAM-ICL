"""
CLI entry point for the modular BAM-ICL project.

Each sub-command corresponds to one conceptual stage:

  1. Hyperparameter Tuning – Algorithm-1
  2. Execute Algorithm-1
  3. Budget Profile Calculation
  4. Algorithm-2 – Flat Attack
  5. Algorithm-2 – BAM-ICL Attack
"""

from __future__ import annotations

import argparse

from . import alg1_tune, alg1_run, budget, alg2_flat, alg2_bam


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="BAM-ICL experiment driver.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("tune-alg1", help="Hyperparameter tuning for Algorithm-1.")
    sub.add_parser("run-alg1", help="Execute Algorithm-1 with configured params.")
    sub.add_parser("budget", help="Compute epsilon budget profile.")
    sub.add_parser("alg2-flat", help="Run Algorithm-2 (Flat attack).")
    sub.add_parser("alg2-bam", help="Run Algorithm-2 (BAM-ICL attack).")
    sub.add_parser("full", help="Run the full pipeline (1→2→3→4→5).")

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.command == "tune-alg1":
        alg1_tune.run_tuning()

    elif args.command == "run-alg1":
        alg1_run.run_algorithm1()

    elif args.command == "budget":
        budget.compute_budget_profile()

    elif args.command == "alg2-flat":
        alg2_flat.run_flat_attack()

    elif args.command == "alg2-bam":
        alg2_bam.run_bam_icl_attack()

    elif args.command == "full":
        # Run all stages in order.
        alg1_tune.run_tuning()
        alg1_run.run_algorithm1()
        budget.compute_budget_profile()
        alg2_flat.run_flat_attack()
        alg2_bam.run_bam_icl_attack()

    else:
        raise ValueError(f"Unknown command: {args.command!r}")


if __name__ == "__main__":
    main()
