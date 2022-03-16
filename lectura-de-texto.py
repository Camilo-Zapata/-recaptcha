import urllib
# import  cv2 
from PIL import Image
import pytesseract
import requests
from flask import Flask
# import cv2  
  
# using imread('path') and 0 denotes read as  grayscale image  


app = Flask(__name__)

# Testing Route
@app.route('/', methods=['GET'])
def ping():
   
    
    url = "https://modelcenter.livejasmin.com/en/captcha/login/captcha_79276fa049d961301a25d3b2a756ac85/display"    
    urllib.request.urlretrieve(url, "imagen.png")

    response = requests.get(url)
    
    with open("imagen.png", "wb") as code:
        code.write(response.content)
        
    img  = Image.open("imagen.png")
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\PC3\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    
    text = pytesseract.image_to_string(img)
    print(text)
    return text

if __name__ == '__main__':
    app.run(debug=True, port=6000)


#Imagen.open("imagen.png")