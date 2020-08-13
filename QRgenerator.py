import qrcode
import time

data = input("Hello, please enter the url that you would like your QR code to link to: \n")
print("You entered %s" % data)
time.sleep(1)
print("Beginning process now...")
time.sleep(1)

qr = qrcode.QRCode(
	version=1, 
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=10,
	border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

print("Done!")
