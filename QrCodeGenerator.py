import qrcode
import image
qr = qrcode.QRCode(
	version = 15, #version means more complicated qrcode
	box_size = 10,#size of the box
	border = 5 #white part of the image
	)
data ="https://www.youtube.com/watch?v=dQw4w9WgXcQ"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("Qr.png")