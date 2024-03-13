import pytesseract
from PIL import Image
import subprocess


def scan_and_call():
    image_path = 'typed_out_image.jpg'
    img = Image.open(image_path)

    text = pytesseract.image_to_string(img)

    phone_numbers = [word for word in text.split() if word.isdigit() and len(word) >= 7]

    if phone_numbers:
        number_to_call = phone_numbers[0]
        subprocess.call(['xdg-open', 'tel://' + number_to_call])
    else:
        print("No phone numbers found in the image.")

scan_and_call()