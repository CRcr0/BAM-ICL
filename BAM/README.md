# BAM


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





