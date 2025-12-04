"""
Entry point.

Usage:
  python main.py               # download Code.ipynb if missing, split into chunks/, then run
  python main.py --split-only  # only split into chunks/, do not execute
  python main.py --run-only    # run existing chunks/ without splitting
  python main.py --no-download # do not download Code.ipynb (expect it to exist locally)
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path

from splitter import ensure_notebook, split_notebook_to_chunks
from runner import run_chunks


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--split-only", action="store_true", help="Only create chunks/, do not execute.")
    p.add_argument("--run-only", action="store_true", help="Only execute existing chunks/, do not split.")
    p.add_argument("--no-download", action="store_true", help="Do not download Code.ipynb if missing.")
    p.add_argument("--notebook", default="Code.ipynb", help="Notebook file to split/run.")
    p.add_argument("--chunks-dir", default="chunks", help="Directory where chunks will be written.")
    p.add_argument("--verbose", action="store_true", help="Print chunk progress.")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parent
    os.chdir(root)

    nb_path = root / args.notebook
    chunks_dir = root / args.chunks_dir

    if not args.run_only:
        if not args.no_download:
            ensure_notebook(nb_path)

        if not nb_path.exists():
            raise FileNotFoundError(
                f"Notebook not found: {nb_path}. "
                f"Place Code.ipynb next to main.py or omit --no-download."
            )

        split_notebook_to_chunks(
            notebook_path=nb_path,
            chunks_dir=chunks_dir,
        )

    if args.split_only:
        return

    if not chunks_dir.exists():
        raise FileNotFoundError(f"Chunks directory not found: {chunks_dir}")

    run_chunks(chunks_dir=chunks_dir, verbose=args.verbose)


if __name__ == "__main__":
    main()
