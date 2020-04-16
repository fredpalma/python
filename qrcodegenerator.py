# QR code generator
# Check/install first qrcode Library
# https://github.com/lincolnloop/python-qrcode
# https://pypi.org/project/qrcode/
# pip install qrcode

# Import library
import qrcode

# Generates QR code
img =  qrcode.make("https://github.com/lincolnloop/python-qrcode")

# Save as PNG File
img.save('qrcode.png','PNG')

