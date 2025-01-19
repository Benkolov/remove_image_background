import argparse
import logging
from pathlib import Path
from PIL import Image
from rembg import remove

"""Background removal module.

This module provides functionality to remove backgrounds from images using the rembg library.
It can be used both as a command-line tool and as an imported module.
"""

# Configure logging for both CLI and GUI usage


def setup_logging():
    """Configure logging settings."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

setup_logging()


def process_image(input_path: str, output_path: str) -> None:
    """Process the image by removing its background.

    Args:
        input_path: Path to the input image file
        output_path: Path where the processed image will be saved
    """
    try:
        logging.info(f"Starting to process image: {input_path}")
        
        # Ensure input file exists
        if not Path(input_path).is_file():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        # Process the image using context manager
        with Image.open(input_path) as inp:
            logging.info("Removing background...")
            output = remove(inp)
            
            logging.info(f"Saving processed image to: {output_path}")
            output.save(output_path)
            
        logging.info("Image processing completed successfully")
        
    except FileNotFoundError as e:
        logging.error(f"File error: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred during image processing: {e}")
        raise
if __name__ == "__main__":
    # Parse command line arguments when run directly
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Remove background from an image")
    parser.add_argument("--input", required=True, help="Path to input image")
    parser.add_argument("--output", required=True, help="Path for output image")
    args = parser.parse_args()
    
    # Process the image
    process_image(args.input, args.output)