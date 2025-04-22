# Find the 10,001st prime

primes = [2,3]
n = len(primes)
p = 3 #the last prime found

#is_prime: int->bool
# Returns if a number is prime. 
# Requires z to be a positive integer; requires z to be no larger than max(primes) + 2.
def is_prime(z):
    for x in primes:
        if z%x == 0:
            return False
    return True

while n < 10002:
    p = p+2
    if is_prime(p):
        primes.append(p)
        n = n + 1
        
print(primes[10000])

print("Primes:", primes)
#Quick note: You ran primes[10001] earlier, which gave you index 100002. The wrong answer.