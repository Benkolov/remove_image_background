# Troubleshooting Guide

This guide helps you resolve common issues you might encounter while using the Background Remover application.

## Installation and Dependency Issues

### Missing Dependencies
- **Error**: `ModuleNotFoundError: No module named 'rembg'`
- **Solution**: Install the required package using pip:
  ```
  pip install rembg
  ```

- **Error**: `ModuleNotFoundError: No module named 'PIL'`
- **Solution**: Install Pillow using pip:
  ```
  pip install Pillow
  ```

## Image Processing Issues

### Input File Errors
- **Error**: `File error: Input file not found`
- **Cause**: The specified input image file doesn't exist or the path is incorrect
- **Solution**: 
  - Verify that the image file exists in the specified location
  - Check if the file path is correct
  - Ensure you have read permissions for the file

### Processing Failures
- **Error**: `An error occurred during image processing`
- **Possible Causes**:
  - Corrupted image file
  - Unsupported image format
  - Insufficient memory
- **Solutions**:
  - Verify the image file isn't corrupted
  - Use supported image formats (PNG, JPG, JPEG, GIF, BMP)
  - Close other applications to free up memory

## GUI-Related Issues

### Image Display Problems
- **Issue**: Images not displaying in the application window
- **Solutions**:
  - Ensure the image file is in a supported format
  - Check if the image file size is reasonable (recommended under 10MB)
  - Try resizing large images before processing

### Save Failures
- **Error**: `Failed to save image`
- **Possible Causes**:
  - Insufficient disk space
  - No write permissions in the target directory
  - Invalid file name or path
- **Solutions**:
  - Free up disk space
  - Choose a different save location
  - Ensure the file name contains only valid characters

### Application Not Responding
- **Issue**: Application freezes during image processing
- **Solutions**:
  - Process smaller images
  - Ensure sufficient system resources are available
  - Restart the application
  - Update to the latest version of the application

## Performance Issues

### Slow Processing
- **Issue**: Image processing takes too long
- **Solutions**:
  - Use smaller image files
  - Close other resource-intensive applications
  - Ensure your system meets the minimum requirements
  - Consider upgrading your RAM if issues persist

## General Troubleshooting Steps

1. **Check Logs**
   - The application creates logs with detailed error information
   - Look for error messages in the console output
   - Check the status bar in the GUI for error messages

2. **Update Software**
   - Ensure you have the latest version of Python installed
   - Update all dependencies to their latest versions
   - Check for application updates

3. **System Requirements**
   - Minimum 4GB RAM recommended
   - Python 3.6 or higher
   - Sufficient disk space for image processing

4. **Clean Installation**
   If problems persist:
   - Uninstall the application
   - Remove all dependencies
   - Reinstall Python and all required packages
   - Reinstall the application

## Getting Additional Help

If you continue to experience issues:
- Check the GitHub repository for known issues
- Submit a new issue with:
  - Detailed description of the problem
  - Steps to reproduce the issue
  - Error messages
  - System information
  - Sample image (if applicable)