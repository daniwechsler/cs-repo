#
# CS Problem 340
# Author: Daniel Wechsler
#


import numpy as np
import math
import Image 
import ImageTk
import Tkinter as tk
import random as rn
import scipy.optimize as  sp
import sys, traceback




###########################################
# Determine window coordinates on image.
###########################################
window  = tk.Tk()
window.title("Vermeer")

image          = Image.open("vermeer_officer_laughing_girl_l.jpg") 
photo          = ImageTk.PhotoImage(image)

imageOverlay   = tk.Canvas(window, width=photo.width(), height=photo.height())
imageOverlay.create_image(0, 0, image = photo, anchor = tk.NW)
imageOverlay.pack(fill=tk.X)

width    = photo.width()
height   = photo.height()


# The points on the image defining the window (left to right, top to bottom)
A = np.array([59.0, 208.0])
B = np.array([76.0, 218.0])
C = np.array([91.0, 227.0])

D = np.array([59.0, 264.0])
E = np.array([76.0, 272.0])
F = np.array([91.0, 277.0])

G = np.array([59.0, 321.0])
H = np.array([76.0, 324.0])
I = np.array([91.0, 327.0])

# Draw the points on the image
imageOverlay.create_rectangle(A[0]-2, A[1]-2, A[0]+2, A[1]+2, fill="red")
imageOverlay.create_rectangle(B[0]-2, B[1]-2, B[0]+2, B[1]+2, fill="red")
imageOverlay.create_rectangle(C[0]-2, C[1]-2, C[0]+2, C[1]+2, fill="red")

imageOverlay.create_rectangle(D[0]-2, D[1]-2, D[0]+2, D[1]+2, fill="red")
imageOverlay.create_rectangle(E[0]-2, E[1]-2, E[0]+2, E[1]+2, fill="red")
imageOverlay.create_rectangle(F[0]-2, F[1]-2, F[0]+2, F[1]+2, fill="red")

imageOverlay.create_rectangle(G[0]-2, G[1]-2, G[0]+2, G[1]+2, fill="red")
imageOverlay.create_rectangle(H[0]-2, H[1]-2, H[0]+2, H[1]+2, fill="red")
imageOverlay.create_rectangle(I[0]-2, I[1]-2, I[0]+2, I[1]+2, fill="red")

#window.mainloop()

#
# Matrix defining the points of the window in 3D space.
#
#   x      y    z
window = np.matrix([
   [-1.0,  1.0, 0.0],      # A
   [ 0.0,  1.0, 0.0],      # B
   [ 1.0,  1.0, 0.0],      # C
   [-1.0,  0.0, 0.0],      # D
   [ 0.0,  0.0, 0.0],      # E
   [ 1.0,  0.0, 0.0],      # F   
   [-1.0, -1.0, 0.0],      # G
   [ 0.0, -1.0, 0.0],      # H
   [ 1.0, -1.0, 0.0]]      # I
   )

###########################################
# Functions to rotate and move the window
# in the room.
###########################################

def verticalRotation (window, angle=-90) :
  
   cos = math.cos(math.radians(angle))
   sin = math.sin(math.radians(angle))
   Ry  = np.matrix(((cos, 0, -sin), (0, 1, 0), (sin, 0, cos)))

   rotated = Ry * window.getT()
   return rotated.getT()

def moveInZDirection (window, amount) :
   moved = window + np.array([0.0, 0.0, amount])
   return moved   

def moveInXDirection (window, amount) :
   moved = window + np.array([amount, 0.0, 0.0])
   return moved

def moveInYDirection (window, amount) :
   moved = window + np.array([0.0, amount, 0.0])
   return moved

# Number of pixels per unit
PIXEL_PER_UNIT = 60

#
# Function used by least square method to determine the
# accuracy of current parameters.
#
def evalPos (params, W3d, W2d) :

   dObs     = params[0]
   dWall    = params[1]
   dImg     = params[2]
   h        = params[3]
   
   # Rotate the window.
   W3d      = verticalRotation(W3d, -90)
   
   # Move the window in the room according to given parameters
   W3d      = moveInZDirection(W3d, dObs+dImg)
   W3d      = moveInXDirection(W3d, dWall)
   W3d      = moveInYDirection(W3d, h)

   # Compute intersection with the image plane.
   def getIntersection (p) :
      X = p[0]*dObs/p[2]
      Y = p[1]*dObs/p[2]
      return np.array([X, Y])

   intersection   = np.apply_along_axis( getIntersection, axis=1, arr=W3d )

   # Compute distance between intersection points and measured points.
   W2d            = W2d / PIXEL_PER_UNIT
   diff           = intersection-W2d

   def distance (p) :
      return np.sqrt(p[0]*p[0] + p[1]*p[1])
   
   error          = np.apply_along_axis(distance, axis=1, arr=diff)
   return error

            
# Initial assumptions
dObs     = -10
dWall    = -5
dImg     = -20
h        = 1.5

# Do transformation on points on image such that (0/0) is
# the center of the image.
W        = np.array([A, B, C, D, E, F, G, H, I])
W        = np.array([width/2.0, (height/2.0)])-W
W        = W * np.array([-1.0, 1])

# Find parameters using least square method.
params   = np.array([dObs, dWall, dImg, h])
res = sp.leastsq(evalPos, params, args=(window, W), maxfev=5000)

dObsR    = res[0][0]
dWallR   = res[0][1]
dImgR    = res[0][2]
hR       = res[0][3]

#
# The position of the observer in the room relative
# from the center point of the window is:
print "Distance from window: %.2f units" % abs(dObsR + dImgR)
print "Distance to left wall: %.2f units" % abs(dWallR)
print "Vertical distance to window: %.2f units" % hR


sys.exit(1)



