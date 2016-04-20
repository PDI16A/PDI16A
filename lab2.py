import os, os.path, sys
from SimpleCV import *
import matplotlib.pyplot as plt
import time
import pip 
from sklearn import preprocessing
from sklearn.cluster import KMeans
import argparse
import utils
import cv2


#from sklearn import *

#### CAPTURAR IMAGEN #####
c = Camera()
plt.ion()
time.sleep(2)

img = c.getImage()
img.save("fotTTo.jpg")
#img.show()

#### OBTENER HISTOGRAMA ####
#img=Image("fotTTo.jpg")

gray = img.toGray()
gray.save("fotTTo_gray.jpg")
#gray = img.greyscale()
#gray.show()
## peaks = img.huePeaks()
## hist = img.hueHistogram()
hist = gray.histogram(255)
## plt.bar()
#plt.plot(hist)
#plt.pause(-1)

#### DIVISION DE COLORES #####

#(red, green, blue) = img.splitChannels(False)
#red_hist = red.histogram(255)
#green_hist = green.histogram(255)
#blue_hist = blue.histogram(255)

#plt.plot(green_hist)
#plt.pause(-1)

#### SEGMENTAR ####
## LETRAS
#img1 = gray.binarize(105)
#img1.save("fotTTo_img1.jpg")
#imLetras = gray*img1
#imLetras.save("1.jpg")

## FONDO
#img2 = gray.binarize(110)
#img3  = img2.invert()
#img3.save("fotTTo_img2.jpg")
#imFondo = gray*img3
#imFondo.save("2.jpg")

## CUADRICULAS
#img4 = gray.binarize()
#img4.save("fotTTo_img3.jpg")
#imFondo = gray*img4
#imFondo.save("3.jpg")

