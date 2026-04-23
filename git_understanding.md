# Git Branching – Reflection


##  Why is pushing directly to main problematic?

Pushing directly to the main branch can be risky because it can introduce bugs or incomplete code into the production environment. It also makes it harder to track changes and review code properly. In a team setting, this can affect other developers and disrupt the workflow.


## How do branches help with reviewing code?

Branches allow developers to work on features or fixes independently without affecting the main codebase. Once the work is complete, it can be reviewed through pull requests before merging into main. This helps ensure code quality, catch mistakes early, and maintain a clean and stable main branch.


## What happens if two people edit the same file on different branches?

If two people edit the same file on different branches, Git will create a merge conflict when trying to combine the changes. This requires manual resolution to decide which changes to keep. While conflicts can be challenging, they help prevent accidental overwriting of someone else’s work.


## Reflection

Working with branches helps maintain a structured and safe development process. It allows experimentation without risk and improves collaboration by enabling proper code review and conflict management.