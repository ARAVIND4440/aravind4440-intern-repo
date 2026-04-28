# CI/CD Reflection

## What is the purpose of CI/CD?

CI/CD helps automate the process of checking and deploying code. Continuous Integration ensures that code changes are tested and validated automatically whenever changes are pushed or a pull request is created. Continuous Deployment or Delivery helps in automatically releasing the application once the checks are passed.

This improves code quality and reduces manual effort.

## How does automating style checks improve project quality?

Automating style checks ensures that all code follows a consistent format. Tools like markdown linting and spell check help maintain readability and professionalism in the project. It also reduces human errors and avoids the need for manual review of formatting issues.

## What are some challenges with enforcing checks in CI/CD?

One challenge is that strict rules can sometimes slow down development, especially if small issues block commits or pull requests. Another challenge is setting up the tools correctly and ensuring that all team members follow the same configuration.


## How do CI/CD pipelines differ between small projects and large teams?

In small projects, CI/CD pipelines are usually simple and focus on basic checks like linting and testing. In large teams, pipelines are more complex and may include multiple stages such as testing, security checks, performance checks, and deployment.

## Reflection

From this task, I learned how CI/CD helps automate code quality checks and maintain consistency across a project. It also showed me how tools like GitHub Actions and Husky can be used together to enforce good coding practices both locally and in the repository.