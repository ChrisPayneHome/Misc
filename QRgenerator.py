import qrcode
import time

data = input("Hello, please enter the url that you would like your QR code to link to: \n")
print("You entered: %s" % data)
print("Beginning process now...")

qr = qrcode.QRCode(
	version=1, 
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=10,
	border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

filename = input("Now let me know what you would like to name the file, remember that it must end with .png: /n")
print("Your QR code is saved as %s" % filename)
img.save(filename)

print("Done!")
