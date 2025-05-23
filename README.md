# BAM-ICL


This repository contains the notebook of our demo, which implements a complete pipeline for BAM-ICL attacks on the language model you would like to pick up by yourself.  The notebook is organised into five top-level code blocks, each with a clear purpose and a small set of flags you can tweak.

⸻

Code Notebook Structure
	1.	Hyperparameter Tuning – Algorithm-1
Purpose: Run an Optuna to find the best values of steps and alpha for the global Algorithm-1 attack.
Main switch: TUNE = True, enables tuning.
Key settings num_shots (in-context examples), n_edit (tokens that may be replaced), and eps (ℓ₂ radius) are defined in the global header.
Output A file called best_params.pkl with the winning hyperparameters.
	2.	Execute Algorithm-1
Purpose: Run Algorithm-1 using either the tuned parameters or the built-in defaults.
Main switches: Set TUNE = False and USE_SAVED_PARAMS = True to load best_params.pkl automatically.
Printed Output: containing attack success rate, loss, and other metrics. Details will be recorded in the .pkl file.
	3.	Budget Profile Calculation
Purpose: Allocate the total ε-budget across token positions once Algorithm-1 is finished.
Inputs: Inherits n_edit and eps from the global header.
Output budget_profile describing per-token ε usage with normalization
	4.	Algorithm-2 – Flat Attack
Purpose: Run the flat variant of Algorithm-2 using the budget profile and, if present, the tuned steps and alpha.
Output the ASR and accuracy, and record the ICEs into pkl.
	5.	Algorithm-2 – BAM-ICL Attack
Purpose: Run the budget-aware in-context learning (BAM-ICL) variant of Algorithm-2 with pre-computed budget profile.
Output the ASR and accuracy, and record the ICEs into pkl.

Quick Start
	1.	Open the notebook on a GPU machine and run the environment-setup cells.
	2.	Optional Set TUNE = True in the first block if you want to perform Optuna tuning; otherwise, leave it False.
	3.	Verify or change n_edit and eps to match your experiment.
	4.	Execute the remaining blocks sequentially from Algorithm 1 through both Algorithm 2 variants.、


Configuration Cheatsheet (text version)
	•	TUNE – True means “run Optuna search”; False means “skip search”.
	•	USE_SAVED_PARAMS – True loads best_params.pkl when TUNE=False.
	•	num_shots – Number of in-context examples in each prompt.
	•	n_edit – Maximum number of tokens Algorithm-1 is allowed to substitute.
	•	eps – ℓ₂-norm budget applied to the sentence-level perturbation.



 
