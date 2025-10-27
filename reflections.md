Reflection

1. Which issues were the easiest to fix, and which were the hardest? Why?
	•	Easiest fixes: The formatting and naming issues were the easiest to fix. Adding missing blank lines (Flake8 E302/E305) and renaming functions to follow snake_case conventions were straightforward because they did not affect the program logic.
	•	Hardest fixes: The most challenging issue was replacing the eval() function and implementing proper exception handling. These required understanding the program’s intent and modifying logic safely without introducing new errors. Additionally, configuring proper logging instead of simple print statements took extra care to ensure clarity and correct log levels.

2. Did the static analysis tools report any false positives? If so, describe one example.

No major false positives were found, but some style-related warnings (like missing blank lines) could be considered overly strict for small scripts. These did not impact functionality but were flagged as per PEP8 guidelines. However, addressing them still improved code readability.

3. How would you integrate static analysis tools into your actual software development workflow?
	•	Local checks: Run tools like flake8, pylint, and bandit locally before each commit to catch errors early.
	•	Pre-commit hooks: Configure Git pre-commit hooks to automatically run static analysis and prevent committing code with style or security issues.
	•	Continuous Integration (CI): Integrate these tools into a CI pipeline (e.g., GitHub Actions) to automatically analyze every pull request. This ensures code consistency, prevents regression, and enforces quality standards across the team.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
	•	Improved readability: Using snake_case naming and consistent spacing made the code easier to read and maintain.
	•	Better robustness: Adding input validation, proper exception handling, and with open() for file operations reduced the risk of crashes and data corruption.
	•	Enhanced security: Removing eval() eliminated a major security risk flagged by Bandit.
	•	Professional logging: Implementing the logging module provided structured and informative feedback, replacing unstructured print statements.

Overall, the code is now cleaner, safer, and more maintainable—ready for production-level practices.