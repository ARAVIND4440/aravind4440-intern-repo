# Environment Variables & Credentials – Reflection

## Why is it more secure to use a .env file for database credentials instead of hardcoding them?

Using a `.env` file is more secure because sensitive information like database credentials is stored separately from the main code. If credentials are hardcoded, they can be exposed when code is shared or uploaded to version control platforms like GitHub. Using a `.env` file reduces this risk and helps protect confidential information.

## How can python-dotenv simplify managing environment variables in Jupyter?

The `python-dotenv` package makes it easier to load environment variables from a `.env` file into Jupyter Notebook. This helps keep the notebook clean and secure, because credentials do not need to be written directly in the code. It also makes updating variables simpler, since changes can be made in one place without modifying the notebook itself.

## Practical Implementation

I created a `.env` file to store database credentials, used `python-dotenv` to load them into Jupyter Notebook, and added `.env` to `.gitignore` so it would not be included in version control.

## Key Learning

A key learning from this task is that storing sensitive information separately from the code is a security best practice. It improves safety, keeps the code cleaner, and reduces the chance of accidental exposure.