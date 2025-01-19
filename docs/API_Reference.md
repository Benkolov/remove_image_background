# API Reference

This document provides detailed information about the public interfaces, classes, and methods available in the Background Remover application.

## BackgroundRemoverGUI Class

The `BackgroundRemoverGUI` class provides the graphical user interface for the background removal application.

### Constructor

```python
BackgroundRemoverGUI(root)
```

**Parameters:**
- `root`: Tkinter root window instance

### Public Methods

#### _select_image()
Opens a file dialog for selecting an input image.
- Supported formats: PNG, JPG, JPEG, GIF, BMP
- Enables the "Remove Background" button upon successful selection
- Updates status bar with selected filename

#### _process_image()
Processes the selected image to remove its background.
- Creates a temporary output file
- Calls the `process_image` function
- Displays the processed image
- Enables the "Save Image" button
- Updates status bar with processing status

#### _save_image()
Opens a save dialog to save the processed image.
- Default format: PNG
- Updates status bar with save status

### Properties

- `input_path`: Path to the selected input image
- `output_image`: Processed image with background removed
- `status_var`: StringVar containing current status message

## Image Processing Functions

### process_image

```python
process_image(input_path: str, output_path: str) -> None
```

Removes the background from an image using the rembg library.

**Parameters:**
- `input_path`: String path to the input image file
- `output_path`: String path where the processed image will be saved

**Raises:**
- `FileNotFoundError`: If the input file doesn't exist
- `Exception`: For other processing errors

**Example Usage:**
```python
process_image("input.jpg", "output.png")
```

## Error Handling

The application implements comprehensive error handling:

1. File Operations:
   - Validates input file existence
   - Handles file read/write errors
   - Manages temporary file cleanup

2. Image Processing:
   - Catches and logs processing errors
   - Displays user-friendly error messages
   - Maintains application stability during errors

3. GUI Operations:
   - Validates button states
   - Handles window update errors
   - Manages memory for image display