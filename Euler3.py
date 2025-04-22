# What is the largest prime factor of the number 600851475143?

x = 600851475143
# Solve by reduction of the number: Find a prime factor, factor it out, continue the process 
#     until there are no factors left (<=> x = 1)

# n tracks the current prime number; 2 is skipped since x is odd by inspection.
n = 3 
primes = [2, 3]
factors = []

# is_prime(n): Int -> Bool
# consumes an integer and returns True if it is prime; else returns False.
# Modifies the program state by appending to the list of primes 'primes'.
# This program is contingent on is_prime() only being called in sequential order of 'n', else  
#     some primes may be overlooked by the running storage in 'primes'.
def is_prime(n):
    for z in primes:
        if n%z==0:
            return False
    primes.append(n)
    return True

while x != 1: # Fundamental Theorem of Arithmetic // Prime factorization theorem
    if is_prime(n):
        while x%n == 0:
            factors.append(n)
            x = x/n
    n = n+2 # since we start at 3 and primes after 3 are all odd.
    
print(len(factors), factors)
print(71*839*1471*6857)
print(primes)

# Solution: Factors = [71, 839, 1471, 6857]; 6857 is the largest prime
# Quick verification: 71 * 839 * 1471 * 6857 = 600851475143