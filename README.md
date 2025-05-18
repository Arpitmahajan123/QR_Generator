# QR Code Generator
A minimal, pure‑Python script that converts any text or URL into a QR code image file.

# Simulation
https://github.com/user-attachments/assets/92bb2ce7-ee0d-4095-bb9c-02304da2c6c0

# Features
Interactive Input
Prompts you to enter the data (text or URL) and desired output filename.

Customizable Output
Uses a box size of 10 and a border of 5 for clear, scannable codes.

Zero External Scripts
Single-file implementation—just install prerequisites and run.

Standard Colors
Generates black-on-white QR codes by default.

# Prerequisites
Python 3.6 or higher

qrcode library

Pillow (automatically installed as a dependency of qrcode)

Install Dependencies

pip install qrcode

Clone or download this repository.

Run the script:

python qr_code_generator.py

# Follow the prompts:

Enter the text or URL to encode.

Enter the desired filename (e.g. mycode.png).

Find your QR code saved in the current directory.

Example Session

Enter The Text or URL to be converted into QR Code: https://www.apple.com
Enter The File Name: apple.jpg
QR Code generated and saved as apple.jpg

# Customization
To change the size of each QR “box,” edit the box_size parameter.

To adjust the border thickness, edit the border parameter.

To use different colors, modify fill_color and back_color in the make_image() call.

#
