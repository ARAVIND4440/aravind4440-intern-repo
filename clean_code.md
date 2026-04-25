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


---

# Code Formatting and Linting Reflection

## Why is code formatting important?

Code formatting is important because it makes the codebase easier to read, review, and maintain. When everyone follows the same style, developers do not waste time arguing about spacing, indentation, quotes, or semicolons. It also makes the project look more professional and consistent.

## What issues did the linter detect?

While testing ESLint and Prettier, the main issues were related to formatting and style consistency, such as spacing, quote style, semicolons, and general code structure. These are small issues, but fixing them makes the code easier to read and keeps it consistent with the project style.

## Did formatting the code make it easier to read?

Yes, formatting made the code easier to read because the structure became cleaner and more consistent. Prettier automatically handled spacing and formatting, while ESLint helped identify style issues. This showed me how useful these tools are in team projects because they reduce manual effort and keep the codebase clean.

## Reflection

I learned that formatting and linting are not just about making code look nice. They help teams maintain a shared coding standard and reduce confusion during code reviews. In a real project, tools like ESLint and Prettier allow developers to focus more on logic and functionality instead of spending time on formatting issues.


## poor version 

def f(a):
    r = 0
    for i in a:
        if i > 10:
            r += i
    return r

- Function name f is meaningless
- Variable a does not explain what it holds
- Variable r is unclear
- Difficult to understand without reading entire code    

## Better version 

MINIMUM_VALUE = 10

def calculate_sum_of_values_above_minimum(numbers):
    total_sum = 0

    for number in numbers:
        if number > MINIMUM_VALUE:
            total_sum += number

    return total_sum

- Function name clearly describes purpose
- Variable names are meaningful
- Constant explains the condition
- Code is self-explanatory    

# Reflection
## What makes a good variable or function name?

A good name clearly describes the purpose of the variable or function. It should be easy to understand without needing extra explanation. Names should be meaningful, consistent, and reflect what the code is doing.

## What issues can arise from poorly named variables?

Poor naming can lead to confusion and make the code harder to understand. It increases the time needed for debugging and makes collaboration difficult. Developers may misunderstand the logic or make mistakes when modifying the code.

## How did refactoring improve code readability?
Refactoring improved readability by replacing unclear names with meaningful ones, improving formatting, and removing ambiguity. The updated code is easier to understand at a glance without needing additional explanation.

## Overall Learning
From this task, I learned that clean code is not just about functionality but also about clarity. Writing clear and meaningful code makes it easier to maintain, debug, and collaborate with others.
