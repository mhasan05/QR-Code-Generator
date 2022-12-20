import pyqrcode
from pyqrcode import QRCode 

# String which represent the QR code 
s = "https://www.teamerror.net"

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "QrCode.svg" 
url.svg("QrCode.svg", scale = 8) 