# Code Smells Reflection

## What Are Code Smells?

Code smells are signs that code may be difficult to read, maintain, or extend. The code may still work, but it can become harder to debug or update later.

---

## 1. Magic Numbers & Strings

### Code Smell

```python
def calculate_discount(price):
    if price > 100:
        return price * 0.10
    return 0
Refactored Code
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.10

def calculate_discount(price):
    if price > DISCOUNT_THRESHOLD:
        return price * DISCOUNT_RATE
    return 0
```

## Improvement
- Using constants makes the code easier to understand and update.
## 2. Long Functions
## Code Smell
``` python
def process_order(order):
    total = sum(order["items"])
    discount = total * 0.10 if total > 100 else 0
    final_total = total - discount
    print("Total:", total)
    print("Discount:", discount)
    print("Final Total:", final_total)
```

## Refactored Code
``` python 
def calculate_total(order):
    return sum(order["items"])

def calculate_discount(total):
    return total * 0.10 if total > 100 else 0

def print_order_summary(total, discount):
    print("Total:", total)
    print("Discount:", discount)
    print("Final Total:", total - discount)
```

## Improvement
- Each function now has one clear responsibility.

## 3. Duplicate Code
## Code Smell
``` python 
def student_average(scores):
    return sum(scores) / len(scores)

def employee_average(scores):
    return sum(scores) / len(scores)
```

## Refactored Code
``` python
def calculate_average(scores):
    return sum(scores) / len(scores)
```

## Improvement
- The repeated logic is now reusable in one place.
## 4. Large Classes / God Objects
## Code Smell
``` python 
class AppManager:
    def login_user(self):
        pass

    def calculate_report(self):
        pass

    def send_email(self):
        pass
```

## Refactored Code
``` python 
class AuthService:
    def login_user(self):
        pass

class ReportService:
    def calculate_report(self):
        pass

class EmailService:
    def send_email(self):
        pass
```    

## Improvement
- Responsibilities are separated into smaller, focused classes.
## 5. Deeply Nested Conditionals
## Code Smell
``` python 
def can_access(user):
    if user:
        if user["active"]:
            if user["role"] == "admin":
                return True
    return False
```    
## Refactored Code
``` python 
def can_access(user):
    if not user:
        return False

    if not user["active"]:
        return False

    return user["role"] == "admin"
``` 
## Improvement
- Guard clauses make the logic easier to read.
## 6. Commented-Out Code
## Code Smell
``` python 
def greet_user(name):
    # print("Old greeting")
    print("Hello", name)
```

## Refactored Code
``` python 
def greet_user(name):
    print("Hello", name)
```
## Improvement
- Removing unused commented code keeps the file clean.
## 7. Inconsistent Naming
## Code Smell
``` python 
def calc(x):
    y = sum(x)
    return y
```
## Refactored Code
``` python
def calculate_total_score(scores):
    total_score = sum(scores)
    return total_score
```    
## Improvement
- Clear names make the purpose of the code easier to understand.
## Reflection
## What code smells did I find?
- The main code smells I worked with were magic numbers, long functions, duplicate code, large classes, deeply nested conditionals, commented-out code, and unclear naming. These issues can make code harder to read even if the code still works.
## How did refactoring improve readability and maintainability?
- Refactoring improved readability by making the code clearer and more organised. Constants explained hardcoded values, smaller functions reduced complexity, and better names made the purpose of each variable and function easier to understand.
- It also improved maintainability because future changes can be made in one place instead of updating repeated or messy code across multiple sections.
## How can avoiding code smells make future debugging easier?
- Avoiding code smells makes debugging easier because the code is simpler to follow. When each function or class has a clear responsibility, it is easier to identify where a problem is happening.
- Clean code also reduces confusion for future developers and makes it safer to update or extend the project.