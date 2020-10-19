import pytesseract
from os import path
try:
    from PIL import Image
except ImportError:
    import Image


def handler(gray, threshold=160):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    anti = gray.point(table, '1')
    return anti


image = path.join(path.dirname(path.abspath(__file__)), 'image/words.png')
gray = Image.open(image).convert('L')
image = handler(gray)
image.show()
print(pytesseract.image_to_string(image))
