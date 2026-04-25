<<<<<<< HEAD
# Git Branching – Reflection


##  Why is pushing directly to main problematic?

Pushing directly to the main branch can be risky because it can introduce bugs or incomplete code into the production environment. It also makes it harder to track changes and review code properly. In a team setting, this can affect other developers and disrupt the workflow.


## How do branches help with reviewing code?

Branches allow developers to work on features or fixes independently without affecting the main codebase. Once the work is complete, it can be reviewed through pull requests before merging into main. This helps ensure code quality, catch mistakes early, and maintain a clean and stable main branch.


## What happens if two people edit the same file on different branches?

If two people edit the same file on different branches, Git will create a merge conflict when trying to combine the changes. This requires manual resolution to decide which changes to keep. While conflicts can be challenging, they help prevent accidental overwriting of someone else’s work.


## Reflection

Working with branches helps maintain a structured and safe development process. It allows experimentation without risk and improves collaboration by enabling proper code review and conflict management.

This line was added from the conflict-test branch.
=======
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

This line is added for testing 
>>>>>>> Test_branch_1
