# User Guide - Background Remover Application

## Introduction
The Background Remover application is a user-friendly tool that allows you to easily remove backgrounds from images. This guide will walk you through all the features and functionality of the application.

## Getting Started

### Launching the Application
1. Ensure you have Python installed on your system
2. Navigate to the application directory
3. Run the application using: `python main.py`

## Main Interface
The application window consists of several key components:

- **Top Toolbar**: Contains the main action buttons
- **Left Panel**: Displays the input image
- **Right Panel**: Shows the processed image with removed background
- **Status Bar**: Provides feedback and current application status

## Using the Application

### Selecting an Image
1. Click the "Select Image" button in the top toolbar
2. In the file dialog, choose an image file (supported formats: PNG, JPG, JPEG, GIF, BMP)
3. The selected image will appear in the left panel
4. The status bar will display the name of the selected file

### Removing the Background
1. After selecting an image, the "Remove Background" button becomes active
2. Click "Remove Background" to start the process
3. Wait while the application processes your image
4. The result will appear in the right panel
5. The status bar will indicate when processing is complete

### Saving the Result
1. Once background removal is complete, the "Save Image" button becomes active
2. Click "Save Image" to open the save dialog
3. Choose a location and filename for your processed image
4. The image will be saved in PNG format to preserve transparency
5. The status bar will confirm when the image has been saved

## Tips and Best Practices
- Use high-quality images for better results
- Ensure the subject is clearly distinguishable from the background
- Images with good contrast between subject and background work best
- The application automatically resizes display images to fit the window while maintaining the original resolution for processing

## Troubleshooting

### Common Issues and Solutions

**Image Won't Load**
- Verify the file format is supported
- Check if the file is not corrupted
- Ensure you have read permissions for the file

**Processing Takes Too Long**
- Consider using a smaller image
- Check if your system has sufficient memory
- Ensure no other resource-intensive applications are running

**Save Operation Fails**
- Verify you have write permissions in the target directory
- Ensure sufficient disk space
- Try saving to a different location

## Keyboard Shortcuts
- `Ctrl+O` or `⌘+O`: Open image
- `Ctrl+S` or `⌘+S`: Save processed image
- `Ctrl+P` or `⌘+P`: Process image
- `Esc`: Cancel current operation

## Need Help?
If you encounter any issues not covered in this guide, please:
1. Check the application logs
2. Visit our GitHub repository for known issues
3. Submit a new issue with detailed information about your problem

---
*Note: Screenshots and specific visual elements may vary slightly depending on your operating system and theme settings.*