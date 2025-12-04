"""
Dataset loading and sampling utilities for BAM-ICL.
"""

from __future__ import annotations

import random
from typing import List

import torch
from datasets import load_dataset

from . import config


def load_sst2():
    """
    Load GLUE SST-2 train and validation splits.

    Returns
    -------
    train_ds, val_ds : datasets.Dataset
    """
    train_ds = load_dataset("glue", "sst2", split="train")
    val_ds = load_dataset("glue", "sst2", split="validation")
    return train_ds, val_ds


def sample_queries(val_ds) -> list:
    """
    Sample a list of validation examples to use as attack queries,
    following the original notebook's behavior (TRIALS draws).

    The exact sampling rule (full sweep vs. random subset) should match
    Code.ipynb. If your notebook uses a different rule, mirror it here.
    """
    random.seed(config.SEED)
    torch.manual_seed(config.SEED)

    val_list = list(val_ds)
    if config.TRIALS >= len(val_list):
        return val_list
    return random.sample(val_list, config.TRIALS)
