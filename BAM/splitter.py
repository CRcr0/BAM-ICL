"""
Notebook splitter.

- Preserves the exact cell source in the generated chunk files.
- Uses 1 file per *code cell* to maximize the number of sub-files.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.request import urlopen, Request

RAW_NOTEBOOK_URL = "https://raw.githubusercontent.com/CRcr0/BAM-ICL/refs/heads/main/Code.ipynb"


def ensure_notebook(notebook_path: Path) -> None:
    """Download Code.ipynb iff it's missing."""
    notebook_path = Path(notebook_path)
    if notebook_path.exists():
        return

    notebook_path.parent.mkdir(parents=True, exist_ok=True)
    req = Request(
        RAW_NOTEBOOK_URL,
        headers={
            "User-Agent": "Mozilla/5.0 (NotebookDownloader; +https://raw.githubusercontent.com)"
        },
    )
    with urlopen(req) as r:
        data = r.read()
    notebook_path.write_bytes(data)


def _safe_filename(s: str, max_len: int = 60) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9_\-]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    if not s:
        s = "cell"
    return s[:max_len]


def split_notebook_to_chunks(*, notebook_path: Path, chunks_dir: Path) -> list[Path]:
    """
    Split a .ipynb into many small .py files, 1 per code cell.
    Returns list of created chunk paths in execution order.
    """
    notebook_path = Path(notebook_path)
    chunks_dir = Path(chunks_dir)
    chunks_dir.mkdir(parents=True, exist_ok=True)

    nb = json.loads(notebook_path.read_text(encoding="utf-8"))
    cells = nb.get("cells", [])

    created: list[Path] = []
    code_cell_idx = 0

    for cell in cells:
        if cell.get("cell_type") != "code":
            continue

        code_cell_idx += 1
        cell_id = str(cell.get("id", "")).strip()
        src = cell.get("source", "")
        if isinstance(src, list):
            code = "".join(src)
        else:
            code = str(src)

        # Build a readable filename suffix from the first non-empty non-comment line.
        head = ""
        for ln in code.splitlines():
            ln = ln.strip()
            if ln and not ln.startswith(("#", "!", "%")):
                head = ln
                break
        head_name = _safe_filename(head) if head else "cell"
        suffix = f"_{cell_id}" if cell_id else ""
        fname = f"cell_{code_cell_idx:04d}{suffix}_{head_name}.py"
        out_path = chunks_dir / fname

        # IMPORTANT: write code EXACTLY as stored in the notebook
        # (we only add a trailing newline if missing).
        if code and not code.endswith("\n"):
            code += "\n"
        out_path.write_text(code, encoding="utf-8")

        created.append(out_path)

    manifest = {
        "notebook": str(notebook_path.name),
        "chunks_dir": str(chunks_dir.name),
        "num_code_cells": len(created),
        "chunks": [p.name for p in created],
    }
    (chunks_dir / "_manifest.json").write_text(
        json.dumps(manifest, indent=2),
        encoding="utf-8",
    )

    return created
