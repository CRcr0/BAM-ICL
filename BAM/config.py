"""
Global configuration and hyperparameters for BAM-ICL.

Edit this file to change experimental settings. The actual algorithmic
content is expected to be identical to the original Code.ipynb; only the
organization into modules is new.
"""

# ====== Algorithm-1 / Optuna search ======
TUNE: bool = False               # True: run Optuna search; False: skip
USE_SAVED_PARAMS: bool = True    # True: load best_params.pkl when TUNE=False

# ====== Few-shot and perturbation parameters ======
NUM_SHOTS: int = 4               # number of in-context examples per prompt
N_EDIT: int = 3                  # maximum number of tokens Algorithm-1 may substitute
EPS: float = 100.0               # L2 budget on the perturbation

# Default local search hyperparameters (can be overridden by tuning)
STEPS: int = 40
ALPHA: float = 3.0

# ====== Data / evaluation settings ======
TRIALS: int = 20                 # number of validation queries to attack
SEED: int = 42                   # random seed

# ====== Model settings ======
MODEL_ID: str = "facebook/opt-30b"

# ====== Paths ======
BEST_PARAMS_PATH: str = "best_params.pkl"
BUDGET_PROFILE_PATH: str = "budget_profile.pkl"
RESULTS_DIR: str = "results"
