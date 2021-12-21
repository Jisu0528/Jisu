from PIL import Image
from gtts import gTTS
import pytesseract
import playsound

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open("test2.jpg")
result = pytesseract.image_to_string(image)

print(result)

with open("text.txt", "w", encoding="utf8") as x:
    x.write(result)
    x.write("\n\n\n")
    x.write(result)
    

txtfile = "text.txt"
y = open(txtfile, 'r', encoding='utf8')
text = y.read()

def speak(text) :
    tts = gTTS(text=text)
    soundfile='voice.mp3'
    tts.save(soundfile)
    playsound.playsound(soundfile)
    
speak(text)