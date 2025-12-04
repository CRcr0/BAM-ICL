"""
Chunk runner.

Executes chunk .py files in-order with a shared global context,
so it behaves like sequential notebook execution.
"""
from __future__ import annotations

import json
from pathlib import Path


def _neutralize_ipython_magics(code: str) -> str:
    """
    Make IPython magics safe in plain Python by commenting them out at runtime.
    The chunk files themselves are not modified.
    """
    out_lines: list[str] = []
    for ln in code.splitlines(True):  # keep line endings
        stripped = ln.lstrip()
        if stripped.startswith(("!", "%")):
            out_lines.append("# " + ln)
        else:
            out_lines.append(ln)
    return "".join(out_lines)


def run_chunks(*, chunks_dir: Path, verbose: bool = False) -> None:
    chunks_dir = Path(chunks_dir)

    manifest_path = chunks_dir / "_manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(
            f"Missing manifest: {manifest_path}. "
            "Run main.py once without --run-only to generate chunks."
        )

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    chunk_names = manifest.get("chunks", [])
    if not chunk_names:
        raise RuntimeError("No chunks listed in manifest.")

    ctx: dict = {
        "__name__": "__main__",
        "__package__": None,
    }

    for i, name in enumerate(chunk_names, start=1):
        path = chunks_dir / name
        code = path.read_text(encoding="utf-8")
        safe_code = _neutralize_ipython_magics(code)

        if verbose:
            print(f"[{i:03d}/{len(chunk_names):03d}] exec {path.name}")

        compiled = compile(safe_code, str(path), "exec")
        exec(compiled, ctx, ctx)
