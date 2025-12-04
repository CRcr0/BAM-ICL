"""
Model loading and helper utilities for BAM-ICL.

This module is intended to host the same logic as the notebook for:
- loading the OPT model (with quantization),
- creating the tokenizer,
- mapping sentiment/topic labels to token IDs,
- computing logits for the last token, etc.
"""

from __future__ import annotations

import gc

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

from . import config


_model = None
_tokenizer = None
_pos_id = None
_neg_id = None


def load_model():
    """
    Lazily load the language model and tokenizer.

    If your Code.ipynb contains additional model customization,
    port that logic here.
    """
    global _model, _tokenizer, _pos_id, _neg_id

    if _model is not None:
        return _model, _tokenizer, _pos_id, _neg_id

    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    tok = AutoTokenizer.from_pretrained(config.MODEL_ID, use_auth_token=True)
    tok.pad_token = tok.eos_token

    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    model = AutoModelForCausalLM.from_pretrained(
        config.MODEL_ID,
        quantization_config=quant_config,
        device_map="auto",
    ).eval()

    pos_id = tok("positive", add_special_tokens=False)["input_ids"][0]
    neg_id = tok("negative", add_special_tokens=False)["input_ids"][0]

    _model, _tokenizer, _pos_id, _neg_id = model, tok, pos_id, neg_id
    return _model, _tokenizer, _pos_id, _neg_id


def classify_token(ids: torch.Tensor):
    """
    Mirror the notebook's 'classify_token' helper: inspect the last-token
    logits and return the predicted sentiment token and its probability.
    """
    model, tok, pos_id, neg_id = load_model()
    logits = model(ids.unsqueeze(0)).logits[0, -1]
    if logits[pos_id] > logits[neg_id]:
        pred = pos_id
        prob = torch.softmax(logits[[neg_id, pos_id]], dim=0)[1].item()
    else:
        pred = neg_id
        prob = torch.softmax(logits[[neg_id, pos_id]], dim=0)[0].item()
    return pred, prob
