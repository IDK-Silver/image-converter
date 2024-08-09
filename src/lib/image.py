from typing import Union
from PIL import Image
from pillow_heif import register_heif_opener

# Register HEIF opener to support .heic files
register_heif_opener()

def open_image(file_path: str) -> Union[Image.Image, None]:
    """
    Open an image file and return a PIL Image object.
    Supports JPG, PNG, and HEIC formats.

    Args:
        file_path (str): The path to the image file.

    Returns:
        Union[Image.Image, None]: A PIL Image object if successful, None if the file cannot be opened.
    """
    try:
        with Image.open(file_path) as img:
            return img.copy()
    except (IOError, OSError):
        print(f"Error: Unable to open image file {file_path}")
        return None




