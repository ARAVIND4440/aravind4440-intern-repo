# Clean Code Reflection

## Clean Code Principles

### Simplicity
Simplicity means keeping code as straightforward as possible. Code should solve the problem without unnecessary complexity or over-engineering. Simple code is easier to test, debug, and improve later.

### Readability
Readable code is easy for another developer to understand. Good variable names, clear structure, and proper spacing make a big difference. Clean code should explain itself as much as possible.

### Maintainability
Maintainable code is easy to update in the future. This is important because code is often changed many times after it is first written. Future developers, including myself, should be able to understand and safely modify it.

### Consistency
Consistency means following the same naming style, formatting, and project conventions throughout the codebase. This makes the code feel organised and easier to review.

### Efficiency
Efficient code performs well, but it should not be over-optimised too early. The goal is to write code that is reasonably fast while still being simple and readable.

---

## Messy Code Example

python
def calc(x):
    t=0
    for i in x:
        if i>50:
            t=t+i
    print(t)


## Updated clear version 

PASS_MARK = 50

def calculate_total_passing_score(scores):
    total_score = 0

    for score in scores:
        if score > PASS_MARK:
            total_score += score

    return total_score


### Why This Version Is Better

The cleaner version uses meaningful names such as calculate_total_passing_score, scores, and total_score. The constant PASS_MARK explains what the number 50 means. The function also returns the result instead of printing it directly, which makes it easier to reuse and test.

## Reflection

From this task, I learned that clean code is not just about making code work. It is about writing code that other people can read, understand, and maintain. In team projects, clean code reduces confusion and makes collaboration easier.
I also learned that small improvements like better variable names, proper spacing, and avoiding hardcoded values can make code much easier to work with.
    

