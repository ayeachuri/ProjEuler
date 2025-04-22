# Diophantine Equations
# Minimal solutions in positive integers to the problem << x^2 - D*y^2 = 1 >>

import math


## Part 1: Range of valid D values
# For D <= 1000, excluding perfect squares
Dmax = 1000

D = list(range(1,1001))
for n in range(1, int(math.sqrt(Dmax)) +1):
    D.pop(n**2 - n) #Because list size mutates, we decrement index by 1 per loop
nD = len(D)
print(str(31**2 in D))
minx = [0]*nD # the array of minimal x
maxx = 0      # Integer tracaking current max(minimal x)
maxD = 0      # The value of D which yields the max(minimal x)
maxy = 0      # The value of y which satisfies maxx^2 - maxD*maxy^2 = 1

## Part 2: Finding the minimal x for each D

import decimal
decimal.getcontext().prec = 20

# Iterate over each value of D (non-perfect-square positive integers)
for iD in range(0, nD):
    found = False # Have we found the minimal soln in x?
    y = 1
    # We check if x^2 - D*y^2 = 1 <-> x^2 = D * y^2 + 1
    while not found:
        # Need to use the decimal module to circumvent Python's float type limitations
        x= math.sqrt((D[iD] * y**2 + 1))
        if x%1 == 0:
            found = True
            minx[iD] = x
            print(str(minx[iD]) + "^2 - " + str(D[iD]) + "*" + str(y) + "^2 = 1")
            if x > maxx: # Record the supremum of minimal values of x for each D
                maxx = minx[iD]
                maxD = D[iD]
                maxy = y # Record the y-values to check result
        else:
            y = y+1
            
### Part 3: Finding the value of D returning largest minimal x
print(maxx, maxD, maxy)
print(max(minx))
print(minx.index(max(minx)))
print(D[minx.index(max(minx))])
### DEBUGGING ###

# Error 1: Program halts for iD = 53, D = 61
#iD = 53
#found = False # Have we found the minimal soln in x?
#import time # Just to observe results
#y = 1
## We check if x^2 - D*y^2 = 1 <-> x^2 = D * y^2 + 1
#while not found:
    #x= math.sqrt(D[iD] * y**2 + 1)
    #if (x%1 == 0):
        #found = True
        #minx[iD] = x
        #print(str(minx[iD]) + "^2 - " + str(D[iD]) + "*" + str(y) + "^2 = 1")
        #if x > maxx: # Record the supremum of minimal values of x for each D
            #maxx = minx[iD]
            #maxD = D[iD]
            #maxy = y # Record the y-values to check result
    #elif (x%1 < 1e-6):
        #print(x, D[iD], y)
        #break
    #else:
        #y = y+1
    #print(x, D[iD], y)
    #time.sleep(0.005)
    
## Verdict: Several observed values of the sqrt output are incorrect
## Printed:
# 14206.84419566851 61 1820
## Actual:
# (61 * 1820**2 + 1)**0.5
# >14214.654445325077
## Python FLOAT arithmetic imprecise for large numbers