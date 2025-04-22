import sys

#################################################################
##################      HELPER FUNCTIONS   ######################

### HELPER 1:
# colLength(n): int -> int
# Recursive function to determine length of Collatz chain
# for given integer n
# Also modifies global dictionary D1 along the way (memoized)
# D1 contains the collatz chain length values for each n 
D1 = {1:0}

def colLength(n):
    # First, check if n has been calculated previously
    if n in D1:
        return D1[n]
    else:
        if n == 1:
            D1[n] = 0
        elif n%2 == 0:
            D1[n] = 1 + colLength(n//2)
        else:
            D1[n] = 1 + colLength(3*n + 1)
        return D1[n]

### HELPER 2:
# maxCol(N) is another recursive function that returns
# the integer n<=N with longest Collatz sequence
# maxCol(N): int -> int
# Modifies a global dictionary D2,
# D2[N] = {n<=N | for all m<=N, colLength(n) >= colLength(m)}
D2 = {1:1}
cMax = 1 # Global var, Tracks largest known N (i.e. D2[i] known for all i<=N)

def maxCol(N):
    global cMax
    if N>cMax:
        # Updating protocol:
        # D2[cMax] = n, n has longest colLength 
        # Evaluate D2[cMax+1], increment cMax
        # Repeat until cMax = N, return D2[cMax]
        while cMax < N:
            cMax = cMax + 1
            cmLen = colLength(cMax)
            if cmLen >= colLength(D2[cMax-1]) :
                D2[cMax] = cMax
            else:
                D2[cMax] = D2[cMax-1] 
    return D2[N]
                
    
#################################################################
#################################################################

# Read in T lines, each with some integer N
# Given N, print the integer n<=N w/ longest Collatz chain
T = int(input().strip())


for i in range(T):
    N = int(input().strip())
    # Find the maximum number n<=N with the longest Collatz chain
    print(maxCol(N))