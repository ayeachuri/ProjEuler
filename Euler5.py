# Euler P5:

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Ans: Just the merging of all prime factors of numbers from 1-20.
# It's the product of elements in this list:
[2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]
# Just by inspection, any number from 1 to 20 is a product of a subset of these terms, and hence is a divisor
#       of the full product of all terms. 
# It is also a minimal list because the removal of any of these primes means either:
#       A. one of the unique primes is removed => The product is no longer divisible by all elements in [1,20]
# or    B. one of the repeated primes is removed => Either 9 or 16 no longer divides the product.

