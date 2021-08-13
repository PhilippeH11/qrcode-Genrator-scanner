import pyqrcode
import png
from pyqrcode import QRCode

link='www.google.fr'
url=pyqrcode.create(link)
url.png('googleqrcode.png', scale=6)