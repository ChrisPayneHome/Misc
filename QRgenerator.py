import qrcode

data = input("Please paste the url you would like to generate a QR code for:\n")
filename = "QR.png"
img = qrcode.make(data)
img.save(filename)