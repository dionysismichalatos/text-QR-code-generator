import qrcode
from PIL import Image

# Request the user to input the text to be converted into a QR code
user_text = input("Please enter the text you want to convert into a QR code: ")

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(user_text)
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image as a PNG file
img.save("qr_code.png")

print("QR code successfully saved as 'qr_code.png'")
