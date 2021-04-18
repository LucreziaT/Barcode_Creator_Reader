#pip3 install python-barcode
import barcode
from barcode.writer import ImageWriter 
hr = barcode.get_barcode_class('ean13')
Hr = hr('1234567891012')
qr = Hr.save('123')
hr1 = barcode.get_barcode_class('Code39')
Hr1 = hr1('abcde',writer=ImageWriter())
qr1 = Hr1.save('1234')