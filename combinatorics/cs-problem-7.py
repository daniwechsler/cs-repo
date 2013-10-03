#
# CS Problem 7
# Author: Daniel Wechsler
#

import sys


#
# Returns true if the filed given by a complex number 
# is attacked by a queen to the left of column (column
# is the index in the list representing the board.
#
def fieldIsAttacked (state, column, field):

    if column == 0: return False #  We only check if there is a queen attacking us from the left (if left most -> no problem)
    
    for col in range(0, column):
        
        # Check if the queen at col is on the same row or column as field. Its the case if the queens
        # position has same real or imaginary part as the new position.
        queen = state[col]
        if field.real == queen.real or field.imag == queen.imag :
            return True

        # Check if the queen at col is on a diagonal though field. Is the case if sum or difference
        # of real part and imag of queen position is equeal to sum or diff of real and imaginary part
        # of filed.
        if (field.real+field.imag == queen.real+queen.imag or field.real-field.imag == queen.real-queen.imag) :
            return True
        
    return False

#
# Rotates complex number c around (0,0).
# Factor is meant to be i|-1|i
#
def rotate (c, factor) :
    return c * factor

#
# Compute complex complement of c (reflection)
#
def complexComplement (c) :
    return complex(c.real, c.imag*-1)

#
# Used to sort the lists of complex numbers
#
def compare (cA, cB) :
    if cA.real > cB.real:
        return 1
    return -1

#
# Returns true if the two chess board sates A and B
# are equal. This is the case if both contain the same
# elements (order does not matter).
#
def isSameState (stateA, stateB) :
    stateA = sorted(stateA, cmp=compare)
    stateB = sorted(stateB, cmp=compare)

    for n in range (0, len(stateA)) :
   
        if stateA[n] != stateB[n] :
            return False
 
    return True


#
# Returns true if solution is independent from all solutions in
# the list independentSolutions.
#
def isIndependentSolution (independentSolutions, solution):
    
    sDep            = []    # Holds all dependent solutions of solution (reflections / rotations)

    # Compute all possible rotations / reflections (combinations)
    ref         = [ complexComplement(c) for c in solution ]            # Reflection on X
    refRot90    = [ rotate(c, -1) for c in ref]
    refRot180   = [ rotate(c, complex(0, 1)) for c in ref ]
    refRot270   = [ rotate(c, -1*complex(0, 1)) for c in ref ]  
    rot90       = [ rotate(c, -1) for c in solution ]                   # Rotation 90 degree
    rot180      = [ rotate(c, complex(0, 1)) for c in solution ]        # Rotation 180 degree
    rot270      = [ rotate(c, -1*complex(0, 1)) for c in solution ]     # Rotation 270 degree

    sDep.append(solution)
    sDep.append(rot90)
    sDep.append(rot180)
    sDep.append(rot270)
    sDep.append(ref)
    sDep.append(refRot90)
    sDep.append(refRot180)
    sDep.append(refRot270)    
   
    # Go through all independent solutions we have so far and check wheather the solution
    # under test is independent of those in the list.
    for independentSolution in independentSolutions :
        for dep in sDep :
            if isSameState (dep, independentSolution):
                return False
     
    return True
    

size            = 24                    # The size of the chess board e.g 8x8
k               = size-1                # The maximum value of b and a (real and im part)
state           = [None]*size           # Holds the state of the board (size entries)
solutions       = []                    # Will hold all solutions to the size-Queen problem
indepSolutions  = []                    # Will hold all independent solutions to the size-Queen problem
columnIndex     = 0                     # Holds the current column index of the state (List)



  
while True:
    
    if state[columnIndex] == None : # There is no queen on the current column. Put it at lowest row on column
        
        realPart    = columnIndex * 2 - k # Compute real part from column index
        newPosition = complex (realPart, -k)
        state[columnIndex] = newPosition
    else :
   
        # There is a queen on the current column -> we move it up one field
        newPosition = state[columnIndex] + complex(0, 2)

        # If new position is out of the boeard go back to left column
        if newPosition.imag > k:

            if columnIndex == 0: # If there is no left column we are done
                break
            
            
            state[columnIndex] = None # Remove the queen from current column
            columnIndex -= 1
            continue
        else:
          
            state[columnIndex] = newPosition

    # Check wheather the new position is under attack
    # (Thus no queen on the left columns attacks the new position)
    if fieldIsAttacked (state, columnIndex, newPosition):
        continue # Try other position
    else :
        if columnIndex == size - 1: # We got a solution
            #print("Solution %s" % format(state))
            solutions.append(state[:]) # Store a copy of the state in our result list
            
            if isIndependentSolution(indepSolutions, state):
                indepSolutions.append(state[:])
                
            continue
        else :   
            columnIndex += 1 # Go to next column     


print("%i Queens Problem" % size)
print("--------------------")

print("Number of solutsions for %ix%i board: %i" % (size, size, len(solutions)))
print("Number of independent solutsions for %ix%i board: %i\n" % (size, size, len(indepSolutions)))

print ("Independent solutions are:")

for solution in indepSolutions :
    print ("%s" % format(solution))

