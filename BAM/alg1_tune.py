"""
Hyperparameter tuning for Algorithm-1 using Optuna.

IMPORTANT:
This module only provides the structure. To preserve exact behavior,
copy the tuning-related code from Code.ipynb (the `TUNE = True` block)
into `run_tuning()`.
"""

from __future__ import annotations

from . import config


def run_tuning() -> None:
    """
    Run an Optuna study to find the best hyperparameters for Algorithm-1.

    Expected behavior (from the notebook):

    - Define an Optuna objective that:
        * sets global search hyperparameters (STEPS, ALPHA, etc.),
        * runs Algorithm-1 across a collection of queries,
        * computes attack success rate (ASR).
    - Save the best hyperparameters to `config.BEST_PARAMS_PATH`.

    Currently this is a placeholder.
    """
    raise NotImplementedError(
        "Paste the Optuna tuning code from Code.ipynb into alg1_tune.run_tuning()."
    )
