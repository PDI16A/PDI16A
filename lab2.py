import os, os.path, sys
from SimpleCV import *
import matplotlib.pyplot as plt
import time

#### CAPTURAR IMAGEN #####
c = Camera()
plt.ion()
time.sleep(2)

img = c.getImage()
#img.save("fotTTo.jpg")
#img.show()

#### OBTENER HISTOGRAMA ####
gray = img.toGray()
## gray = img.greyscale()
gray.show()
## peaks = img.huePeaks()
## hist = img.hueHistogram()
hist = gray.histogram()
#plt.bar()
plt.plot(hist)
plt.pause(-1)

#### DIVISION DE COLORES #####

(red, green, blue) = img.splitChannels(False)
red_hist = red.histogram(255)
green_hist = green.histogram(255)
blue_hist = blue.histogram(255)

#plt.plot(green_hist)
#plt.pause(-1)
