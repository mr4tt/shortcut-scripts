import os
from PIL import ImageGrab
import pytesseract
from dotenv import load_dotenv

def get_clipboard_image():
    load_dotenv() 
    try:
        clipboard_data = ImageGrab.grabclipboard()

        # Check if the data is an image; ImageGrab will have None if not an image
        # and check if it's not a list of file path or folder path 
        if clipboard_data and not isinstance(clipboard_data, list):
            # location of tesseract.exe; install w/ https://github.com/UB-Mannheim/tesseract/wiki
            pytesseract.pytesseract.tesseract_cmd = os.environ.get("tesseract_exe")
            return pytesseract.image_to_string(clipboard_data)
        else:
            return None
        
    except Exception as e:
        print(f"Error getting clipboard image: {e}")
        return None

if __name__ == "__main__":
    image = get_clipboard_image()
    if image:
        # image.show()
        print(image)
    else:
        print("No image found in clipboard.")