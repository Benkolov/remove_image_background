# Installation Guide

This guide will walk you through the process of setting up the Background Removal Tool on your system.

## System Requirements

- Python 3.7 or higher
- pip (Python package installer)
- At least 2GB of free disk space
- Minimum 4GB RAM recommended

## Prerequisites

Before installing the application, ensure you have Python and pip installed on your system. You can verify this by running:

```bash
python --version
pip --version
```

## Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/remove_image_background.git
cd remove_image_background
```

2. (Optional) Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

The following packages will be automatically installed:

- Pillow (v10.0.0) - Python Imaging Library for image processing
- rembg (v2.0.50) - Background removal library

## Verifying Installation

To verify that everything is installed correctly:

1. Ensure all dependencies are installed:
```bash
pip list
```

2. Try running the application:
```bash
python main.py
```

## Troubleshooting

If you encounter any issues during installation:

1. **Package Installation Errors**
   - Ensure you have the latest version of pip:
     ```bash
     python -m pip install --upgrade pip
     ```
   - Try installing packages individually:
     ```bash
     pip install Pillow==10.0.0
     pip install rembg==2.0.50
     ```

2. **Python Version Issues**
   - Make sure you're using Python 3.7 or higher
   - Check your Python version with `python --version`

3. **Virtual Environment Problems**
   - Delete the venv directory and create a new one
   - Ensure you've activated the virtual environment before installing dependencies

For additional help, please open an issue on the project's GitHub repository.