import os, os.path, sys
from SimpleCV import Camera, Image, Display

c = Camera()
#c.live()

img = c.getImage()
img.save("fotTTo.jpg")

c.live()
