from pyzbar.pyzbar import decode
from PIL import Image
import cv2 
d = decode(Image.open("1.png"))
print(frame[0].data.decode())

