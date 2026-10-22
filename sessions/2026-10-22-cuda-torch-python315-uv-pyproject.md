# Switch to CUDA PyTorch, Python 3.15 and a uv pyproject

**Date:** 2026-10-22

## Resume this session

```
claude --resume f8977336-d4d6-4ebf-8d30-be6b17a6e154
```

Originally started in: `/home/frank/devel/ai-courses/andrei-karpathy/nn-zero-to-hero/lectures/own-repos/micrograd`

Display name when written: `micrograd-c1` (directory placeholder; may have since changed).

---

## Summary

The session started from a new, empty `torch-tutorial.py` (for the PyTorch part of the
lecture) and grew into a rework of the Python environment. The user did the environment
commands themselves to learn how uv works; Claude explained, checked results and only
edited `torch-tutorial.py` (initial skeleton) and `CLAUDE.md`.

**GPU / CUDA.** The machine has an NVIDIA GeForce RTX 4060 Laptop GPU (driver 580.178.04,
supports CUDA up to 13.0; no `nvcc` toolkit installed, and none is needed because PyTorch
wheels bundle the CUDA runtime). The venv had `torch 2.14.1+cpu`. The user switched the
index in `requirements.txt` to `https://download.pytorch.org/whl/cu130` and replaced torch
with `uv pip install -r requirements.txt --reinstall-package torch`. A plain
`uv pip install -r` would have done nothing, because the installed CPU build already
satisfied the unpinned `torch` requirement. Result: `torch 2.14.1+cu130`,
`torch.version.cuda == 13.0`, `torch.cuda.is_available() == True`.

**Python 3.15.** `uv python install 3.15` installed CPython 3.15.1 (newest stable uv
offered; 3.16.0a1 is an alpha). Compatibility was checked with
`uv pip compile requirements.txt --python-version 3.15` (not `uv pip install --python 3.15`,
which needs an existing 3.15 venv and fails). The venv was recreated with
`uv venv --python 3.15 --clear`, packages reinstalled, and the Jupyter kernel re-registered
(`.venv/bin/python -m ipykernel install --sys-prefix --name micrograd --display-name
"Python (micrograd)"`), since `--clear` deletes the kernel spec inside the venv. PyCharm
picked up 3.15.1 for the same interpreter path.

**Notebook breakage after the upgrade.** The `MLP` training cell failed with
`TypeError: Calling np.sum(generator) is deprecated`. Cause: a leftover
`from numpy import *` in cell 1 (added as a test for another project) shadowed the
built-in `sum` (and `min`, `max`, `abs`, `round`, …) with numpy's. The older numpy only
warned and fell back to the built-in; the new numpy raises. The user removed the line and
restarted the kernel.

**Why `--upgrade` left packages old: index priority.** With `--extra-index-url`, uv's
default `first-index` strategy takes each package from the first index that has it at all,
and the PyTorch index hosts stale copies of common packages (certifi 2022.12.7,
charset-normalizer 2.1.1, idna 3.4, requests 2.28.1, urllib3 1.26.13, …). These weren't
leftovers; all 127 installed packages were in the resolved tree. A `requirements.txt` can't
restrict an index to one package, so the fix was to move to a uv project.

**Conversion to `pyproject.toml`** (done by the user): `uv init --bare --python 3.15`, then
the index added by hand before adding packages:

```toml
[[tool.uv.index]]
name = "pytorch-cu130"
url = "https://download.pytorch.org/whl/cu130"
explicit = true

[tool.uv.sources]
torch = { index = "pytorch-cu130" }
```

then `uv add numpy matplotlib graphviz torch jupyter ipykernel`. With `explicit = true`
only torch comes from the PyTorch index; its dependencies (`cuda-toolkit`, `nvidia-*`,
filelock, …) come from PyPI but still obey torch's version pins (verified with a throwaway
lock in the scratchpad before converting).

**Remaining "outdated" packages are intentional.** PyCharm still flags 16 packages; their
installed metadata shows each one is pinned: `cuda-toolkit==13.0.3`, `nvidia-cudnn-cu13`,
`nvidia-cusparselt-cu13`, `nvidia-nccl-cu13`, `nvidia-nvshmem-cu13` directly by torch;
`nvidia-cublas`, `-cuda-cupti`, `-cuda-nvrtc`, `-cuda-runtime`, `-cufft`, `-cufile`,
`-curand`, `-cusolver`, `-cusparse`, `-nvtx` by `cuda-toolkit 13.0.3`'s extras; and
`mpmath` (1.3.0 vs 1.4.1) by sympy's `mpmath<1.4`. `torch 2.14.1+cu130` vs PyPI's `2.14.1`
is the same release. Don't use PyCharm's upgrade button on these. A final
`uv lock --upgrade && uv sync` changed only `pycparser 3.11 → 3.12`.

**Concepts explained along the way** (no changes involved): uv's roles (Python installer,
venv creator, Rust re-implementation of the pip interface with a hard-linked global cache in
`~/.cache/uv`; the venv has no pip); how `uv pip` finds the target venv (`--python`, then
`VIRTUAL_ENV`, then `.venv` upwards); `--python` vs `--python-version`; keeping a CPU build
as backup (needs a second venv; not worthwhile since the cu130 build also runs on the CPU);
and where PyCharm stores that the interpreter is uv-managed:
`~/.config/JetBrains/PyCharm2026.2/options/jdk.table.xml` (`FLAVOR_ID = UvSdkFlavor`,
`IS_UV="true"`, `usePip: false`), referenced by name from `.idea/micrograd.iml`, so it is not
part of the repo.

## Changes

- `torch-tutorial.py`: created as a `main()` skeleton by Claude; the user then added a GPU
  check (CUDA version, device name, a tensor on `cuda`).
- `micrograd.ipynb`: user removed `from numpy import *` from cell 1.
- `pyproject.toml`: new uv project config (Python `>=3.15`, six dependencies, explicit
  cu130 index for torch).
- `uv.lock`: new lock file.
- `requirements.txt`: deleted (`git rm -f`).
- `CLAUDE.md`: Environment section rewritten for the uv project, Python 3.15, the
  Jupyter kernel, the cu130 torch and the rule not to upgrade `cuda-toolkit`/`nvidia-*`
  separately.
- `.venv/`: recreated with CPython 3.15.1; torch `2.14.1+cu130`; all other packages at the
  newest versions torch allows; Jupyter kernel "Python (micrograd)" re-registered.
- Machine: CPython 3.15.1 installed via `uv python install 3.15`
  (in `~/.local/share/uv/python/`).

## Status

Everything works: CUDA is available in the venv (`13.0 True`), PyCharm uses the 3.15.1 uv
interpreter, and the notebook runs again after the kernel restart.

Nothing from this session is committed. At the time of writing, `pyproject.toml`,
`uv.lock` and the `requirements.txt` deletion were staged; `CLAUDE.md`, `micrograd.ipynb`,
`torch-tutorial.py` and this recap were not. A `.python-version` pin (`uv python pin 3.15`)
was suggested but not created.

To upgrade later: `uv tree --outdated` to look, `uv lock --upgrade && uv sync` to apply,
then check `torch.cuda.is_available()` if torch changed.
