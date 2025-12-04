
# BAM-ICL

### [Poster](https://neurips.cc/media/PosterPDFs/NeurIPS%202025/116672.png?t=1764864651.985822) | [Slides](https://neurips.cc/virtual/2025/loc/san-diego/poster/116672) | [Paper](https://openreview.net/pdf?id=hCc6obJhlj)



**BAM-ICL: Causal Hijacking In-Context Learning with Budgeted Adversarial Manipulation**

[Rui Chu](https://scholar.google.com/citations?user=Jd2YfKQAAAAJ&hl=en), [Bingyin Zhao](https://bxz9200.github.io/),  [Hanling Jiang](https://openreview.net/profile?id=%7EVivian_Jiang3), [Shuchin Aeron](https://shuchin.github.io), and [Yingjie Lao†](https://laogroup.ece.tufts.edu/).

Conference on Neural Information Processing Systems (NeurIPS), 2025.

![BAM-ICL Demo](BAM-ICL_poster.png)

---

## BAM-ICL Attack Demo


# BAM-ICL Attack Demo

This repository contains the code in jupyter for our demo, which implements a complete pipeline for BAM-ICL attacks on the language model of your choice. The notebook is organized into five top-level code blocks, each with a clear purpose and a small set of flags you can tweak.

---

## Code Notebook Structure

1. **Hyperparameter Tuning – Algorithm-1**  
   - **Purpose:** Run an Optuna study to find the best values of `steps` and `alpha` for the global Algorithm-1 attack.  
   - **Main switch:** `TUNE = True` (enables tuning).  
   - **Key settings:**  
     - `num_shots` (number of in-context examples)  
     - `n_edit` (number of tokens that may be replaced)  
     - `eps` (ℓ₂ radius)  
   - **Output:** A file called `best_params.pkl` containing the winning hyperparameters.

2. **Execute Algorithm-1**  
   - **Purpose:** Run Algorithm-1 using either the tuned parameters or the built-in defaults.  
   - **Main switches:**  
     - `TUNE = False`  
     - `USE_SAVED_PARAMS = True` (loads `best_params.pkl` automatically)  
   - **Output:** Printed attack success rate, loss, and other metrics (also saved in a .pkl file).

3. **Budget Profile Calculation**  
   - **Purpose:** Allocate the total ε-budget across token positions after Algorithm-1 completes.  
   - **Inputs:** Inherits `n_edit` and `eps` from the global header.  
   - **Output:** A `budget_profile` describing per-token ε usage (normalized).

4. **Algorithm-2 – Flat Attack**  
   - **Purpose:** Run the flat variant of Algorithm-2 using the budget profile and (if present) the tuned `steps` and `alpha`.  
   - **Output:** Attack success rate (ASR), accuracy, and recorded ICEs in a .pkl file.

5. **Algorithm-2 – BAM-ICL Attack**  
   - **Purpose:** Run the budget-aware in-context learning (BAM-ICL) variant of Algorithm-2 with the precomputed budget profile.  
   - **Output:** ASR, accuracy, and recorded ICEs in a .pkl file.

---

## Quick Start

1. Open the notebook on a GPU-enabled machine and run the environment-setup cells.  
2. **Optional:** In the first block, set `TUNE = True` to perform Optuna tuning; otherwise, leave it `False`.  
3. Verify or change `n_edit` and `eps` to match your experiment.  
4. Run the remaining blocks sequentially—from Algorithm-1 through both Algorithm-2 variants.

---

## Configuration Cheatsheet

- `TUNE` – `True` means **run** Optuna search; `False` means **skip** search.  
- `USE_SAVED_PARAMS` – `True` loads `best_params.pkl` when `TUNE=False`.  
- `num_shots` – Number of in-context examples per prompt.  
- `n_edit` – Maximum number of tokens Algorithm-1 may substitute.  
- `eps` – ℓ₂-norm budget applied to the sentence-level perturbation.  

---

## Running Environment

For the environment, we are using Python 3.11, CUDA 12.2, and correlated PyTorch on Linux. Please refer to:  https://pytorch.org/get-started/locally/
 
