###############################################
# Solving: https://www.hackerrank.com/contests/projecteuler/challenges/euler014/problem
##### Thought process ######

#As a data structures problem: Longest Collatz sequence beginning under a million

#- Conjecture: all numbers eventually converge; finish at 1.
#- As a tree; rooted at 1


# ###### Method 1: Populating a tree top-down (with 1 at the top)
# V1: Keep a dictionary ~~ Keys = 1:1e6 ~~  Values = chain length
# A dictionary offers O(1) lookup; the array is O(n). Use Dict.

# Using claim: There is a unique chain from any integer to 1 (if such a chain exists)
# Beginning with 1, determine for each n what integers 'point' to it (always 2n, possibly (n-1)/3 if it is an integer)
# Assign the chain(n)+1 as the chain length to the 1 or 2 integers pointing to n, then queue those integers and repeat
#    until all million numbers have an assigned chain length (use a counter each time a length is assigned)


# ###### Method 2: Beginning with 1e6 and counting down, follow the collatz iteration until 1, then assign each
# element in the chain its corresponding length. Need to generate the complete chain or until the first known value
# in the dictionary is seen (but then need to keep checking if each element of the dictionary is in the chain).

# Neither method avoids the issue of having an unknown upper limit on intermediate terms in the chain 
# climbing arbitrarily high above 1 million
# - Option 1 requires fewer lookups but will take up more memory (long recursion).

######### Queue implementation: 
# We use a FIFO system, arrays will be O(n); use Python collections.deque Class (doubly-linked list)
from collections import deque
#########################################

# Implementation: Store the data in a dictionary, not a list. There's no use in order.
# Using a recursive approach, top-down populating a tree of collatz chains, stored in an array

# nextCol returns a list of one or two elements
# nextCol: int -> listof(int)
def nextCol(n):
    # Forced to include a ~O(1) lookup because 4->1 created a cycle/inf. loop
    if ((n-1)%3 == 0) & (((n-1)//3)%2 == 1) & ((n-1)//3 not in collatzDict): # (1) Test (n-1)/3 is an integer; (2) test it is odd
        return [(n-1)//3, 2*n] # It seems prudent to queue the smaller number first
    elif (2*n not in collatzDict): 
        return [2*n]


# Keep a counter until all the first 10^6 integers have known chain lengths
upLim = 10**2
filled = 0  # The number of integers in the range [1,upLim] which have known lengths
#highest = 0 # Was thinking of recording the highest known chain length but it's redundant.
# The queue structure is a doubly-linked list; O(1) pop and append operations
q = deque()

# A dictionary initialized with all values at 0
# More keys will be introduced to the dictionary as the recursion branches beyond 10**6
# collatzDict = dict(zip(range(1,upLim + 1), [0]*upLim))   # Looks nice but counterproductive
collatzDict = {}

collatzDict[1] = 0 # Trivial chain has length 0: from 1->1
collatzDict[2] = 1 # The only integer pointing to 1
collatzDict[4] = 2
collatzDict[8] = 3
q.append(8)
filled = 4
Steps = 0


#while (filled < upLim):
    #current = q.popleft()
    #curChainLength = collatzDict[current]
    #nextVals = nextCol(current)
    ## Debug:
    ##Steps = Steps + 1
    ##print(["Stepno:" + str(Steps), current, nextVals, q])
    ## Two cases follow:
    #if len(nextVals)==1:
        #q.extend(nextVals) # extend for a list, not append
        ## We only add to the filled counter if the next values are in range[1,10**6 + 1]
        #if nextVals[0] <= upLim:
            #filled = filled + 1
        #collatzDict[nextVals[0]] = curChainLength + 1
    #else: 
        #q.extend(nextVals) # Two element list
        #if nextVals[0] <= upLim:
            #filled = filled + 1
        #collatzDict[nextVals[0]] = curChainLength + 1
        #if nextVals[1] <= upLim:
            #filled = filled + 1
        #collatzDict[nextVals[1]] = curChainLength + 1

# At the end of the while loop, all 10**6 values in the dictionary should be filled
# The last value to have been assigned a length will lead to the next two nodes
#left = []
#for i in list(range(1,101)):
    #if i not in collatzDict:
        #left = left + [i]
#print([len(left),left, collatzDict])


### Method 1 ran into memory exceptions ###
###########################################

### Attempt 2 / Method 2: Takes less memory, more time ###
### SOLVED: [837799, 525]; fairly short run time (< 2 mins) ###


# Now running the bottom-up approach
# collatz: int -> int
# Returns the next value in the Collatz procedure
def collatz(n):
    if (n%2 == 0):
        return n//2
    else: 
        return (3*n + 1)    

# Returns the whole chain of integers an integer takes to reach 1 
#    via the Collatz procedure (assuming such a chain exists).
# colChain: int -> listof(int)
def colChain(n):
    nxt = n
    chain = [n]
    while nxt > 1:
        nxt = collatz(nxt)
        chain = chain + [nxt]
    return chain
    

lenmax = 0
nmax = 1

for i in range(1,2 * 10**5 + 1):
    print(i)
    j = 10**6 - i #(working from largest to smallest)
    lenj = len(colChain(j))
    if lenj > lenmax:
        lenmax = lenj
        nmax = j
    
print([nmax, lenmax])

