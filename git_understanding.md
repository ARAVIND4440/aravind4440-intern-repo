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
<<<<<<< HEAD
>>>>>>> Test_branch_1
=======

# Git Merge Conflict Reflection

## What caused the conflict?

The conflict happened because I edited the same part of git_understanding.md in two different branches. I first made a change in the Test_branch_1 branch, then switched back to main and made a different change in the same location. When I tried to merge the branch back into main, Git could not automatically decide which version to keep.

## How did I resolve it?

I resolved the conflict using VS Code. VS Code showed the conflicting changes and gave options such as accepting the current change, accepting the incoming change, or accepting both changes. I reviewed both versions and chose to keep both changes, then cleaned up the conflict markers manually and committed the resolved file.

## What did I learn?

I learned that merge conflicts are a normal part of working with Git, especially when multiple people edit the same file or same section of code. I also learned that VS Code makes it easier to identify and resolve conflicts visually. The main lesson is to communicate clearly in teams and pull the latest changes regularly to reduce conflicts.


# Advanced Git Commands Reflection

## git checkout main -- <file>

This command restores a specific file from the main branch without affecting other files or changes. It is useful when I accidentally modify a file and want to reset only that file instead of resetting the whole project.

In a real project, I would use this when I want to discard unwanted changes in one file while keeping my other work safe.

---

## git cherry-pick <commit>

The git cherry-pick command applies one specific commit from another branch into the current branch without merging the entire branch. This is useful when I only need one change from another branch, but I do not want to bring all other changes from that branch.

In a real project, this is helpful when a bug fix exists on another branch and needs to be applied quickly to main or a release branch.

---

## git log

The git log command shows the commit history of the repository. It helps me understand what changes were made, when they were made, and by whom.

In a real project, I would use git log to track the history of changes, find specific commits, and understand how the code evolved over time.

---

## git blame <file>

The git blame command shows who last modified each line of a file and when. This is useful for understanding the history of specific lines of code.

In a real project, I would use this carefully to understand context, not to blame someone personally. It helps identify who to ask when I need more information about a specific change.

---

## What surprised me?

The most surprising command was git cherry-pick because it allows selecting only one commit from another branch instead of merging the whole branch. This showed me how flexible Git can be in long-running projects with multiple developers.

I also found git blame useful because it gives detailed line-by-line history, which can help when trying to understand why a specific change was made.