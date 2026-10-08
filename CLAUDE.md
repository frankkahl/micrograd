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

- Python virtual environment in `.venv/` (managed with `uv`), used as the PyCharm
  project interpreter and as the Jupyter kernel.
- Dependencies are listed in `requirements.txt`; install/update with
  `uv pip install -r requirements.txt` (PyTorch from the CPU wheel index, see the file).
- `graphviz` (used for `draw_dot` visualisation of the computation graph) needs the
  system `dot` binary, which is installed at `/usr/bin/dot`.
- Notebook work happens in `micrograd.ipynb`, opened in PyCharm with the `.venv`
  kernel.
