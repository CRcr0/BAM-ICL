"""
Execution of Algorithm-1 with tuned or default hyperparameters.
"""

from __future__ import annotations

from . import config


def run_algorithm1() -> None:
    """
    Run Algorithm-1 using either tuned parameters (best_params.pkl) or
    the built-in defaults.

    Expected behavior (from the notebook):

    - Optionally load `config.BEST_PARAMS_PATH` when `config.USE_SAVED_PARAMS` is True.
    - Iterate over validation queries and run Algorithm-1 for each.
    - Print and save metrics (clean acc, adv acc, ASR, etc.).

    Currently this is a placeholder.
    """
    raise NotImplementedError(
        "Paste the Algorithm-1 execution code from Code.ipynb into alg1_run.run_algorithm1()."
    )
