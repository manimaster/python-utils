from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:")
    print(extracted_text)



# pip install pytesseract Pillow

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# brew install tesseract
