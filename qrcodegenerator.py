import qrcode

# Data to encode
data = "https://example.com"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # Size of the QR code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Border size
)

# Add data to QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
qr_image = qr.make_image(fill="black", back_color="white")

# Save the image
qr_image.save("qrcode.png")

# Show the QR code
qr_image.show()
