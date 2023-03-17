from PIL import Image, ImageEnhance
import pytesseract
import glob

Images = glob.glob("*.png")

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

lines = []

for imgx in Images:
    img = Image.open(f"{imgx}")
    text = pytesseract.image_to_string(img, lang="eng")
    text = [ x.replace("\n", " ") for x in text.split("\n\n") if len(x) >10]
    try:
        with open("Questions.txt", 'r') as fp:
            lines = [x for x in fp.read().split("\n") if len(x)>5]
    except:
        pass
    with open("Questions.txt", 'w') as fp:
        for quest in lines:
            fp.write(quest)
            fp.write("\n")
        fp.write(f"{imgx.split('.')[0]}")
        fp.write("\n")
        fp.write("\n")
        fp.write("\n")
        for quest in text:
            fp.write(quest)
            fp.write("\n")
        fp.write("\n")