# Contributing to Background Remover

Thank you for your interest in contributing to the Background Remover project! This guide will help you understand how to contribute effectively to the project.

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/remove_image_background.git
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Code Style Guidelines

We follow PEP 8 Python style guidelines with the following specifics based on our existing codebase:

- Use 4 spaces for indentation (as seen in `main.py`, `gui.py`, and `sors.py`)
- Include docstrings for modules and functions (reference `sors.py` for examples)
- Use type hints for function parameters and return values
- Keep lines under 100 characters
- Use meaningful variable and function names
- Organize imports in the following order:
  1. Standard library imports
  2. Third-party imports
  3. Local application imports

## Git Workflow

1. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-fix-name
   ```

2. Make your changes in small, logical commits:
   ```bash
   git commit -m "Clear description of your changes"
   ```

3. Keep your branch updated with main:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

## Pull Request Process

1. Update your fork with the latest changes from the main repository
2. Ensure your code follows our style guidelines
3. Test your changes thoroughly
4. Create a pull request with:
   - Clear title and description
   - Reference to any related issues
   - Screenshots for UI changes
   - List of major changes made

## Testing Requirements

- Add appropriate unit tests for new functionality
- Ensure all existing tests pass
- Test GUI changes manually across different platforms
- Verify error handling and edge cases

## Documentation

- Update relevant documentation for any new features
- Add inline comments for complex logic
- Include docstrings for new functions and classes
- Update README.md if necessary

## Project Structure Reference

Key files to review for understanding the codebase:

- `main.py`: Application entry point
- `gui.py`: GUI implementation using tkinter
- `sors.py`: Core background removal functionality

## Need Help?

- Review existing code in the repository
- Check open and closed issues
- Create a new issue for discussions
- Join our community chat (if available)

## Code of Conduct

Please note that this project follows a Code of Conduct. By participating, you are expected to uphold this code.