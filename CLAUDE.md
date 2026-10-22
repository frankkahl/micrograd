# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Purpose

This repo exists to follow Andrej Karpathy's lecture
["The spelled-out intro to neural networks and backpropagation: building micrograd"](https://www.youtube.com/watch?v=VMj-3S1tku0&list=PLXYLzZ3XzIbi4lL43O6fIU_ojuZwBO6vi)
(lecture 1 of *Neural Networks: Zero to Hero*) and to re-create his
[micrograd](https://github.com/karpathy/micrograd) repo step by step while watching.

It is a learning repo: the user writes the code along with the lecture. Explain and
help, but don't jump ahead and write the finished micrograd unless asked.

## Repository

- GitHub: <https://github.com/frankkahl/micrograd> (public), default branch **`master`**
  (not `main`).
- Tagged with the GitHub topic `karpathy` to group it with the other Karpathy course
  repos — GitHub has no folders for repositories, so topics are the grouping mechanism.
- This directory lives inside a local clone of `karpathy/nn-zero-to-hero`
  (`lectures/own-repos/micrograd`), but it is its own independent git repo.

## Environment

- uv project: dependencies are declared in `pyproject.toml` and pinned in `uv.lock`
  (both committed). Use `uv add` / `uv remove` to change dependencies, `uv sync` to
  rebuild the environment, and `uv lock --upgrade && uv sync` to upgrade.
- Python 3.15 virtual environment in `.venv/` (uv-managed interpreter), used as the
  PyCharm project interpreter (a uv interpreter) and as the Jupyter kernel
  "Python (micrograd)", registered inside the venv with `--sys-prefix`.
- PyTorch is the CUDA 13.0 build (`+cu130`) for the RTX 4060 GPU. Only `torch` comes
  from the PyTorch index: it is declared `explicit = true` and mapped to torch via
  `[tool.uv.sources]`, so everything else, including torch's own dependencies, comes
  from PyPI. The `cuda-toolkit` / `nvidia-*` packages are pinned by torch to CUDA 13.0
  and must not be upgraded on their own (e.g. via PyCharm's upgrade button).
- `graphviz` (used for `draw_dot` visualisation of the computation graph) needs the
  system `dot` binary, which is installed at `/usr/bin/dot`.
- Notebook work happens in `micrograd.ipynb`, opened in PyCharm with the `.venv`
  kernel.
