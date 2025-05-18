import qrcode

data = input("Enter The Text or URL to be converted into QR Code: ").strip()
filename = input('Enter The File Name: ').strip()


# For Creating QR Code
qr = qrcode.QRCode(box_size=10, border=5)

# Now Add Data To The QR Code
qr.add_data(data)

# Customize the QR Code
image = qr.make_image(fill_color="black", back_color="white")

# Save the QR Code To A File
image.save(filename)

# Display the QR Code

print(f'QR Code generated and saved as {filename}')

