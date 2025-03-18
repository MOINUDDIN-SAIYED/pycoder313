import qrcode
from PIL import Image
link = input("Enter the link to generate a QR code: ")

qr = qrcode.QRCode(
    version=2,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,   
)
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="darkblue", back_color="white")
img.show()


