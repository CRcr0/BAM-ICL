# BAM-ICL (auto-split into many sub-files)

This package **splits `Code.ipynb` into as many sub-files as possible** (1 file per code cell),
while keeping the original cell contents unchanged. It also guarantees that:

```bash
python main.py
```

runs the whole pipeline by executing the generated chunk files in-order (notebook-style).

## What you get

- `chunks/` (auto-generated): many `cell_XXXX_*.py` files, one per code cell
- `chunks/_manifest.json`: stable execution order
- `main.py`: entry point

## Quick start

```bash
python main.py --verbose
```

If `Code.ipynb` is not found, `main.py` downloads it from:

- `https://raw.githubusercontent.com/CRcr0/BAM-ICL/refs/heads/main/Code.ipynb`

## Useful modes

Only split (do not execute):

```bash
python main.py --split-only
```

Only run existing chunks (do not split):

```bash
python main.py --run-only
```

Do not download (expect `Code.ipynb` next to `main.py`):

```bash
python main.py --no-download
```

## Notes

- IPython magics like `!pip install ...` are **commented out at runtime** so plain Python can execute.
  The chunk files themselves are written exactly as stored in the notebook.
- This runs the notebook code **sequentially in one shared global namespace** (like a notebook),
  so it avoids breaking dependencies between cells.
