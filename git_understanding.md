# Git Staging vs Committing – Reflection

## What is the difference between staging and committing?

Staging means selecting the changes that I want to include in the next commit. It is like preparing changes before saving them permanently in Git history.

Committing means saving the staged changes into Git history with a commit message. Once committed, the change becomes part of the project timeline.


## Why does Git separate these two steps?

Git separates staging and committing so developers can control exactly what changes go into each commit. This is useful when multiple files are changed, but only some changes are related to one task.

It helps keep commits clean, organised, and easier to review.


## When would you want to stage changes without committing?

I would stage changes without committing when I want to review what I am about to commit first. It is also useful when I am preparing a specific set of changes but want to double-check them before creating the final commit.

For example, if I modify multiple files, I can stage only the files related to one task and commit them separately.