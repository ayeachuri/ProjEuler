#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Term 1: 1^2 + 2^2 + .... + 100^2
# Term 2: (1 + 2 + ... + 100)^2

x=0
y=0
for i in range(101):
    x += i**2
    y += i
print(x - y**2)
print((y==101*50))