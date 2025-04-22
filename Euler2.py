#Find the sum of even-valued fibonacci terms under 4 million


# Note: This was solved in a brute-force manner but there's a cleaner way to do it
#       The distribution of even numbers is predictable: 1, 1, 2, 3, 5, 8, 13, 21, 34
#       Odd - odd - even - odd - odd -even is the recurring pattern
#       We just need every third fibonacci number


x=0 # The summation counter
a = 1
b = 1
while a < 4000000:
    b = b + a
    a = b - a #increment process
    if a%2 == 0: # This can be skipped by just looking for every 3rd fibonacci term
        x += a #add to the total
print(x)
        