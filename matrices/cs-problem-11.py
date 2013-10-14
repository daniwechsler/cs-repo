#
# CS Problem 11
# Author: Daniel Wechsler
#

from scipy.linalg import solve



# Solving equation 4.5

A = [
    [ 2,-1,-1, 0, 1, 0],
    [-1, 3,-1,-1, 0, 0],
    [-1,-1, 3,-1, 0, 0],
    [ 0,-1,-1, 2, 0, 1],
    [ 1, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 1, 0, 0]
    ]

B = [0, 0, 0, 0, 0, 1]
# Solve A*X = B
X = solve(A, B)

print "\nWheatstone bridge\n"
print ("V0 = %.2f V" % X[0])
print ("V1 = %.2f V" % X[1])
print ("V2 = %.2f V" % X[2])
print ("V3 = %.2f V" % X[3])
print ("I0 = %.2f A" % X[4])
print ("I1 = %.2f A" % X[5])


# Apply it to the resistor qube problem

#   |V0,V1,V2,V3,V4,V5,V6,V7    |I0,I7|
Q = [
    [ 3,-1,-1,-1, 0, 0, 0, 0,   1, 0],        #V0
    [-1, 3, 0, 0,-1,-1, 0, 0,   0, 0],        #V1
    [-1, 0, 3, 0,-1, 0,-1, 0,   0, 0],        #V2
    [-1, 0, 0, 3, 0,-1,-1, 0,   0, 0],        #V3
    [ 0,-1,-1, 0, 3, 0, 0,-1,   0, 0],        #V4
    [ 0,-1, 0,-1, 0, 3, 0,-1,   0, 0],        #V5
    [ 0, 0,-1,-1, 0, 0, 3,-1,   0, 0],        #V6
    [ 0, 0, 0, 0,-1,-1,-1, 3,   0, 1],        #V7
    
    [ 1, 0, 0, 0, 0, 0, 0, 0,   0, 0],        #I0
    [ 0, 0, 0, 0, 0, 0, 0, 1,   0, 0],        #I7
    ]

B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

X = solve(Q, B)
print "\nResistor Qube\n"

print ("V0 = %.2f V" % X[0])
print ("V1 = %.2f V" % X[1])
print ("V2 = %.2f V" % X[2])
print ("V3 = %.2f V" % X[3])
print ("V4 = %.2f V" % X[4])
print ("V5 = %.2f V" % X[5])
print ("V6 = %.2f V" % X[6])
print ("V7 = %.2f V" % X[7])

print ("I0 = %.2f A" % X[8])
print ("I7 = %.2f A" % X[9])
R = 1 / X[8]
print ("Total resistance %.2f Ohm" % R )



# Replacing some of the resistors with capacitors.
#
# As soon as all capacitors are loaded to C and the
# circuit   is s tabilized the capacitors  act like
# resistors of   infinite resistance. Thus if there
# is no connection between nodes connected   with a
# capacitor. In the the matrix defining the circuit
# we have to set zeros at the corresponding
# intersection points. (And adapt the values in the
# diagonal such that rows and columns  still sum up
# to zero.
#
# In the following example I replaced the resistors
# between V1/V4 and V7/V6 with capacitors.
#


#   |V0,V1,V2,V3,V4,V5,V6,V7    |I0,I7|
Q = [
    [ 3,-1,-1,-1, 0, 0, 0, 0,   1, 0],        #V0
    [-1, 2, 0, 0, 0,-1, 0, 0,   0, 0],        #V1
    [-1, 0, 3, 0,-1, 0,-1, 0,   0, 0],        #V2
    [-1, 0, 0, 3, 0,-1,-1, 0,   0, 0],        #V3
    [ 0, 0,-1, 0, 2, 0, 0,-1,   0, 0],        #V4
    [ 0,-1, 0,-1, 0, 3, 0,-1,   0, 0],        #V5
    [ 0, 0,-1,-1, 0, 0, 2, 0,   0, 0],        #V6
    [ 0, 0, 0, 0,-1,-1, 0, 2,   0, 1],        #V7
    
    [ 1, 0, 0, 0, 0, 0, 0, 0,   0, 0],        #I0
    [ 0, 0, 0, 0, 0, 0, 0, 1,   0, 0],        #I7
    ]
B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

X = solve(Q, B)

print "\nResistor Qube (with capacitors)\n"
print ("V0 = %.2f V" % X[0])
print ("V1 = %.2f V" % X[1])
print ("V2 = %.2f V" % X[2])
print ("V3 = %.2f V" % X[3])
print ("V4 = %.2f V" % X[4])
print ("V5 = %.2f V" % X[5])
print ("V6 = %.2f V" % X[6])
print ("V7 = %.2f V" % X[7])

print ("I0 = %.2f A" % X[8])
print ("I7 = %.2f A" % X[9])
R = 1 / X[8]
print ("Total resistance %.2f Ohm" % R )


# Replace some of the resistors with inductors.
#
# Replacing a   resistor  between two nodes acts as if
# the two nodes are directly connected (As soon as the
# inductor is charged).
#
# One was to   adapt the Kirchhoff    matrix is to add
# relatively   high values   at the intersection point
# (connecting twonodes with a inductor). As higher the
# values are as closer  we reach the final I0 and I7
# the circuit converges to.
#
# In   the following example   I replaced the resistor
# between   node V0 and V1 with an inductor. (Adding a
# relatively   high  number and adapting the values in
# the diagonal).


# Apply it to the resistor qube problem

#   |V0,V1,V2,V3,V4,V5,V6,V7    |I0,I7|
Q = [
    [-98,  100,-1,-1, 0, 0, 0, 0,   1, 0],        #V0
    [ 100,-98,  0, 0,-1,-1, 0, 0,   0, 0],        #V1
    [-1,   0,   3, 0,-1, 0,-1, 0,   0, 0],        #V2
    [-1,   0,   0, 3, 0,-1,-1, 0,   0, 0],        #V3
    [ 0,  -1,  -1, 0, 3, 0, 0,-1,   0, 0],        #V4
    [ 0,  -1,   0,-1, 0, 3, 0,-1,   0, 0],        #V5
    [ 0,   0,  -1,-1, 0, 0, 3,-1,   0, 0],        #V6
    [ 0,   0,   0, 0,-1,-1,-1, 3,   0, 1],        #V7
    
    [ 1,   0,   0, 0, 0, 0, 0, 0,   0, 0],        #I0
    [ 0,   0,   0, 0, 0, 0, 0, 1,   0, 0],        #I7
    ]

B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

X = solve(Q, B)
print "\nResistor Qube\n"

print ("V0 = %.2f V" % X[0])
print ("V1 = %.2f V" % X[1])
print ("V2 = %.2f V" % X[2])
print ("V3 = %.2f V" % X[3])
print ("V4 = %.2f V" % X[4])
print ("V5 = %.2f V" % X[5])
print ("V6 = %.2f V" % X[6])
print ("V7 = %.2f V" % X[7])

print ("I0 = %.2f A" % X[8])
print ("I7 = %.2f A" % X[9])
R = 1 / X[8]
print ("Total resistance %.2f Ohm" % R )




