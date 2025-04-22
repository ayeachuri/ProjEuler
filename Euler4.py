# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is $9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Initial thoughts:
# The largest number would be 999*999 < 1000^2 = 1 mil.
# We're looking at 6-digit numbers abccba

# Approach 1:
# Iterate across 10^3 instances counting down from 999: abc-cba; try to factorize it into two 3-digit numbers
# Requires (prime) decomposition of numbers, computationally costly

# Approach 2:
# Iterate across 899^2 products of 3-digit numbers until the first palindrome is found.

# Approach 3:
# Include some intuitive guesses. Since we're looking for the largest palindrome, look at numbers
#   beginning with 9 first. 9-bccb-9. For this combination, the last digit must be 9 IFF the two factors
#   are products of one of {3x3, 7x7, 9x1}
# This also requires the first digit = 9 (necessary, not sufficient condition).

# ##################################
# Approach #3 found no palindromes somehow. Running approach #2.

# is_palindrome(x): int -> bool
# Checks if a given number is a palindrome
# requires: x is a 6-digit number.
def is_palindrome(x):
    xstr = str(x)
    if x<100000:
        return False
    elif x>999999:
        return False
    elif (xstr[0] == xstr[5]) & (xstr[1] == xstr[4]) & (xstr[2] == xstr[3]):
        return True
    else: 
        return False

# Need to check all products 9a1 * 9b9; 9a3 * 9b3; 9a7 * 9b7
# Trying to figure out the product size so we find the largest palindrome first is tedious;
# This function will just find them all, throw them in a list and then find max(list).

pals = [] 
factors = [] # List of lists of factor pairs and product


# The following code yielded the wrong answer
# Testing it later it was because range(9) goes from 0-8, not 0-9. Solved later by 0-10, got the right answer.
#for a1 in range(1,9):
#    for b1 in range(9):
#        for c1 in range(9): 
#            n = 100*a1 + 10*b1 + c1
#            for a2 in range(1,9):
#                for b2 in range(9):
#                    for c2 in range(9):
#                        m = 100*a2 + 10*b2 + c2
#                        z = n*m
#                        if is_palindrome(z):
#                            pals.append(z)
#                            factors.append([n,m])
#res = max(pals)
#print(res)
#ind = pals.index(res)
#print(res, factors[ind])

# This code fixed it (and is a lot simpler)
for a in range(100,999): 
    for b in range(100,999):
        z = a * b
        if is_palindrome(z):
            pals.append(z)
            factors.append([a,b])
res = max(pals)
print(res)
ind = pals.index(res)
print(res, factors[ind])