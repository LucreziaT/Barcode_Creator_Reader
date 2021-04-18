import qrcode 
import cv2
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
    )
data=input("Inserisci il nome del prodotto: ")
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("1.png")
x=cv2.imread("1.png")
cv2.imshow('',x)
cv2.waitKey(0)