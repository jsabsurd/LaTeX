sum = 0

for i in range(1, 65):   # range(x, y)   x inkl., y exkl.
    sum += (2**(i-1))

print(sum)
sum = 0

for i in range(0, 64):
    sum += (2**i)

print(sum)
