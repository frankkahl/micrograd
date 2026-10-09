# Set up micrograd repo, venv and notebook

**Date:** 2026-10-08

## Resume this session

```
claude --resume 88ed9843-6371-447f-814e-dd75c7ca82b5
```

Originally started in: `/home/frank/devel/ai-courses/andrei-karpathy/nn-zero-to-hero/lectures/own-repos/micrograd`

Display name when written: `micrograd-a8` (auto-generated; may have since changed).

---

## Summary

The goal was to set up a personal repo for following Andrej Karpathy's lecture 1 of
*Neural Networks: Zero to Hero* ("building micrograd",
<https://www.youtube.com/watch?v=VMj-3S1tku0&list=PLXYLzZ3XzIbi4lL43O6fIU_ojuZwBO6vi>)
and re-creating his micrograd repo. The setup includes a public GitHub repo with `master`
as the default branch, a `CLAUDE.md`, a `.venv` for PyCharm, and a Jupyter notebook.

The user also asked to group the repo into a "karpathy" folder on GitHub. GitHub has no
folders for repositories, and the `karpathy` organization name belongs to Karpathy
himself. The repo was given the topic `karpathy` instead, along with `micrograd` and
`nn-zero-to-hero`. The group can be filtered with
`github.com/frankkahl?tab=repositories&q=topic:karpathy`. A differently named
organization is still an option if real grouping is wanted.

The `master` default branch came from creating the GitHub repo empty, then running
`git init -b master` locally and pushing. GitHub took the first pushed branch as the
default.

PyTorch is installed from the CPU wheel index to keep the venv small. The lecture only
uses torch to check micrograd's gradients, so the CUDA build isn't needed.

The micrograd folder sits inside a local clone of `karpathy/nn-zero-to-hero`, so it
showed up as untracked in that outer repo. It was excluded locally rather than through
the outer repo's `.gitignore`, so nothing is committed upstream.

## Changes

- GitHub: created <https://github.com/frankkahl/micrograd>. It's public, with default
  branch `master` and topics `karpathy`, `micrograd` and `nn-zero-to-hero`.
- Local repo `.../lectures/own-repos/micrograd`: ran `git init -b master` and set the
  remote `origin` to `git@github.com:frankkahl/micrograd.git`.
- Files created and committed in one initial commit, pushed to `origin/master`:
  - `CLAUDE.md`: the repo's purpose (lecture link, learning repo, so Claude shouldn't
    write ahead of the user), repo details and environment notes.
  - `requirements.txt`: numpy, matplotlib, graphviz, torch (via the
    `--extra-index-url https://download.pytorch.org/whl/cpu` line), jupyter and ipykernel.
  - `.gitignore`: `.venv/`, `__pycache__/`, `*.pyc`, `.ipynb_checkpoints/` and `.idea/`.
  - `micrograd.ipynb`: a title/lecture-link markdown cell and an imports cell (math,
    numpy, matplotlib, `%matplotlib inline`). Its kernelspec is `micrograd`.
- `.venv/`: Python 3.12.13 created with `uv venv`, with the requirements installed
  (torch 2.14.1+cpu). The Jupyter kernel `micrograd` ("Python (micrograd)") is
  registered inside the venv with `--sys-prefix`.
- Outer repo `nn-zero-to-hero/.git/info/exclude`: appended
  `/lectures/own-repos/micrograd/`.

## Status

- Everything works. The notebook ran headless through `nbconvert --execute` without
  errors, all imports load in the venv, and the system `dot` binary is at `/usr/bin/dot`.
- Not yet checked in PyCharm. Open the `micrograd` folder as a project and select
  `.venv/bin/python` as the interpreter if PyCharm doesn't detect it automatically.
- Next step: start the lecture and build the `Value` class in the notebook.
- This recap file (`sessions/`) is not committed yet.
