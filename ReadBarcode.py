#pip3 install pyzbar 
#pip3 install cv2
import pyzbar
import cv2
import requests
from pyzbar.pyzbar import decode

def get_barcode_info(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    barcodes = decode(gray_img)
    #print('barcodes: ',barcodes)

    if len(barcodes) == 1:
        code = barcodes[0].data
        url = "https://it.openfoodfacts.org/api/v0/product/{}.json".format(code)
        data = requests.get(url).json()
        if data["status"] == 1:
            product = data["product"]
            brand = product["brands"]
            return "produttore: {}    nome: {}".format(product["brands"], product["product_name"])
        else:
            return "Prodotto non trovato!"
    else:
        return "Codice a barre non trovato!"

cap = cv2.VideoCapture(0)
while(True):
  ret, frame = cap.read()
  info = get_barcode_info(frame)
  cv2.putText(frame, info, (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

  cv2.imshow('Codice a Barre', frame)
  code = cv2.waitKey(30)
  if code == ord('q'):
      break
