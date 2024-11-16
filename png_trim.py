#!/usr/bin/env python3

from PIL import Image
import sys
import os

def trim_image(image_path, output_path, pixels_top, pixels_bottom, pixels_left, pixels_right):
    """
    Trims the edges of a PNG image by the specified number of pixels.

    Args:
        image_path (str): Path to the input PNG image.
        output_path (str): Path to save the trimmed image.
        pixels_top (int): Number of pixels to trim from the top.
        pixels_bottom (int): Number of pixels to trim from the bottom.
        pixels_left (int): Number of pixels to trim from the left.
        pixels_right (int): Number of pixels to trim from the right.
    """
    try:
        # Open the image
        with Image.open(image_path) as img:
            width, height = img.size
            
            # Check if the trim amount is valid
            if (pixels_top + pixels_bottom >= height) or (pixels_left + pixels_right >= width):
                print("Error: Trim amounts are too large for the image dimensions.")
                return
            
            # Crop the image
            cropped_img = img.crop((
                pixels_left,                 # Left
                pixels_top,                  # Top
                width - pixels_right,        # Right
                height - pixels_bottom       # Bottom
            ))
            
            # Save the cropped image
            cropped_img.save(output_path)
            print(f"Image successfully trimmed and saved to {output_path}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print(f"Expected 7 arguments, got {len(sys.argv)}: {sys.argv}")
        print("Usage: ./trim_image.py <image_path> <output_path> <pixels_top> <pixels_bottom> <pixels_left> <pixels_right>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    output_path = sys.argv[2]
    try:
        pixels_top = int(sys.argv[3])
        pixels_bottom = int(sys.argv[4])
        pixels_left = int(sys.argv[5])
        pixels_right = int(sys.argv[6])
        if any(p < 0 for p in [pixels_top, pixels_bottom, pixels_left, pixels_right]):
            raise ValueError("Pixels must be non-negative integers.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    trim_image(image_path, output_path, pixels_top, pixels_bottom, pixels_left, pixels_right)
