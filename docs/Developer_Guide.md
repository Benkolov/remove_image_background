# Developer Guide

## Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Key Modules](#key-modules)
- [Development Setup](#development-setup)
- [Coding Conventions](#coding-conventions)
- [Contributing Guidelines](#contributing-guidelines)
- [Testing and Debugging](#testing-and-debugging)

## Project Overview

The Background Remover application is a Python-based desktop tool that allows users to remove backgrounds from images using the `rembg` library. The application features a graphical user interface built with Tkinter and supports various image formats.

## Project Structure

```
remove_image_background/
├── main.py
├── gui.py
├── sors.py
├── docs/
│   ├── Developer_Guide.md
│   └── ...
├── requirements.txt
└── README.md
```

## Key Modules

### main.py
The entry point of the application that initializes the GUI. This module:
- Imports the main function from gui.py
- Handles the application startup

### gui.py
The graphical user interface implementation that:
- Creates the main application window using Tkinter
- Manages user interactions and image display
- Handles file operations (open/save)
- Coordinates with sors.py for image processing

Key classes:
- `BackgroundRemoverGUI`: Main GUI class that manages the application interface

### sors.py
The core background removal module that:
- Provides the image processing functionality
- Handles logging and error management
- Can be used both programmatically and via command line

Key functions:
- `process_image()`: Removes background from input image
- `setup_logging()`: Configures application logging

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/remove_image_background.git
cd remove_image_background
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Coding Conventions

### Python Style Guide
- Follow PEP 8 style guide
- Use 4 spaces for indentation
- Maximum line length: 79 characters
- Use meaningful variable and function names
- Add docstrings for modules, classes, and functions

### Code Organization
- Keep functions and methods focused and single-purpose
- Use classes for organizing related functionality
- Separate GUI logic from processing logic
- Handle errors appropriately with try-except blocks

### Documentation
- Add docstrings to all public functions and classes
- Include type hints for function parameters
- Document any non-obvious implementation details
- Keep comments up to date with code changes

## Contributing Guidelines

1. **Branch Management**
   - Create feature branches from `main`
   - Use descriptive branch names (e.g., `feature/new-filter-option`)
   - Keep branches up to date with `main`

2. **Commit Messages**
   - Write clear, descriptive commit messages
   - Use present tense ("Add feature" not "Added feature")
   - Reference issue numbers when applicable

3. **Pull Requests**
   - Create detailed PR descriptions
   - Include testing steps and screenshots if applicable
   - Ensure all tests pass
   - Request code review from maintainers

4. **Code Review Process**
   - Address all review comments
   - Keep PR scope focused
   - Update documentation as needed
   - Squash commits before merging

## Testing and Debugging

### Running Tests
- Use Python's unittest framework
- Run tests before submitting PRs
- Add tests for new features
- Maintain test coverage

### Debugging Tips
1. Use logging:
   - Check logs in the console
   - Add debug logging statements when needed
   - Use appropriate log levels

2. Common Issues:
   - Image loading errors: Check file paths and permissions
   - GUI responsiveness: Use threading for long operations
   - Memory issues: Monitor resource usage with large images

3. Development Tools:
   - Use an IDE with debugging capabilities
   - Enable Python warnings during development
   - Use linters (flake8, pylint) for code quality