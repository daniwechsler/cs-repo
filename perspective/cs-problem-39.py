#
# CS Problem 39
# Author: Daniel Wechsler
#


import numpy as np
import math
import Image 
import ImageTk
import Tkinter as tk
import random as rn
import matplotlib.pyplot as plt
from time import time, strftime
from datetime import datetime
import datetime


class Daylight :


    position    = None

    positionOrg = None

    
    def __init__(self) :
        self.reset()

    def reset (self) :
        # Initial position: longitude, latitude zero at equinox
        if self.position == None :
           self.position = np.matrix([[1],[0],[0]])   # uniti vector along x
        else :
           self.position = self.positionOrg

    def rotateLongitude (self, angle) :

        cos = math.cos(math.radians(angle))
        sin = math.sin(math.radians(angle))
        Ry  = np.matrix(((cos, 0, -sin), (0, 1, 0), (sin, 0, cos)))

        self.position = Ry*self.position
        return self.position
       

    def rotateLatitude (self, angle) :
        cos = math.cos(math.radians(angle))
        sin = math.sin(math.radians(angle))      
        Rz  = np.matrix(((cos, sin, 0), (-sin, cos, 0), (0, 0, 1)))

        self.position = Rz*self.position
        return self.position


    def rotateEarthInclination (self, angle) :
        
        cos = math.cos(math.radians(angle))
        sin = math.sin(math.radians(angle))        
        Rx  = np.matrix(((1, 0, 0), (0, cos, sin), (0, -sin, cos)))
        self.position = Rx*self.position
        
        return self.position



##################################
# Plotting functions
##################################

def getDaylightContours () :

    GRID = 40
    latitude    = np.linspace(-180, 180, GRID)
    longitude   = np.linspace(-90, 90, GRID)
    brightness  = np.zeros( (GRID, GRID) )
    for i in xrange(GRID):
        for j in xrange(GRID):
            d.reset()
            rot = d.rotateLongitude(latitude[i])
            rot = d.rotateLatitude(longitude[j])
            brightness[j,i] = d.position[0]       

    return latitude, longitude, brightness


def showMap (latitude, longitude, brightness) :

    fig = plt.figure()

    # Scale to match image map
    scale_w = 1200/360 + 0.35
    scale_h = 600/180 + 0.35
    latitude = latitude * scale_h+600
    longitude = longitude * scale_w+300

    # Plotting settings
    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    # Draw world map in plot
    im      = plt.imread('equirectangular-projection_small.jpg')
    implot  = plt.imshow(im, origin="lower")

    # Draw brightness contours
    plt.contour(latitude, longitude,  brightness, np.arange(0.0, 1.0, .05))



##################################
# Set time
##################################

def getAngleForDay (time) :
   secondsADay = 60*60*24
   angle = 360.0/secondsADay*time
   return angle
def getAngleForYear (time) :
   year = 31560000
   return 360.0 / year * time



d                 = Daylight()
d.cardWidth       = 1200
d.cardHeight      = 600
center            = np.array([1200/2, 600/2])


# Get current time
t = int(time()) - 1363867200


secondsThisDay = t % (3600 * 24)
yearAngle      =  getAngleForYear(t)
dayAngle       = getAngleForDay(secondsThisDay)


d.rotateLongitude(yearAngle)              # Rotate according to time elapsed today
d.rotateEarthInclination(23)              # Earth inclination
d.rotateLongitude(-yearAngle+dayAngle)    # Rotate according to time elapsed since march 21 2013

d.positionOrg = d.position                # Store current position and compute daylight map
                                          # from that position.


ts                               = datetime.datetime.now().strftime('%b-%d-%G @ %H:%M')
latitude, longitude, brighness   = getDaylightContours()
img                              = showMap(latitude, longitude, brighness)
plt.title("Daylight map at current time [%s]" % ts)
plt.show()





















