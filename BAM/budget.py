"""
Budget profile calculation module.
"""

from __future__ import annotations

from . import config


def compute_budget_profile() -> None:
    """
    Compute and save the epsilon budget profile across token positions.

    Expected behavior (from the notebook):

    - Load Algorithm-1 perturbation statistics.
    - Aggregate and normalize per-token epsilon usage.
    - Save to `config.BUDGET_PROFILE_PATH`.

    Currently this is a placeholder.
    """
    raise NotImplementedError(
        "Paste the budget-profile code from Code.ipynb into budget.compute_budget_profile()."
    )
