import os, os.path, sys
from SimpleCV import *
import matplotlib.pyplot as plt
import time
import pip 
#import matplotlib.image as mpimg
from sklearn import preprocessing
#from scipy import misc

#from sklearn import *

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
#gray.show()
## peaks = img.huePeaks()
## hist = img.hueHistogram()
hist = gray.histogram()
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

#face = misc.face()
#plt.imshow(face)
#misc.imsave('face.png', face)
#face = misc.imread('face.png')
#gray.save("fotTTo_gray.jpg")
#im_gray=mpimg.imread('fotTTo_gray.jpg')



#binarizer = preprocessing.Binarizer(im_gray)
#binarizer = preprocessing.Binarizer()
#binarizer.transform(gray)

img4 = gray.binarize(105)
img4.save("fotTTo_img4.jpg")

