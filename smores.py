# we are looking at approximation of pi
# as well as looking at the math module

print(22/7)
print(355/113)

import math

print(9801 / (2206 * math.sqrt(2)))


def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSidesS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSidesS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(4))
print(archimedes(8))

for sides in range(40, 400, 40):
    print(sides, archimedes(sides))


# see the loop above. In addition to the value of pi, print the difference between the values calculated by the archimedes function and by math.pi
# how many sides does it take to make the two close?

print(math.pi)
#
# it takes 360000000

# Accumulators

acc = 0
for val in range(1, 6):
    acc = acc + val

print(acc)

# the range is from and including the first number to but not including the next number
# the last number indicates

#heres the sum of first 100 even numbers

acc = 0
for val in range(0, 201, 2):
    acc = acc + val
print (acc)

# the sum of the first 50 odd numbers

acc = 0
for val in range(1, 101, 2):
    acc = acc + val
print(acc)

# First 100 odd numbers average

acc = 0
for val in range(1, 201, 2):
    acc = acc + val / 100

print(acc)

# function for the average of N numbers where N is a parameter

def average(N):
    acc = 0
    for average in range(0, 37, N):
        acc = acc + average
    print(acc/N)

print(average(6))

# this function finds the product of N numbers where N is a parameter
def factorial(N):
    acc = 1
    for factorial in range(1, N+1, 1):
        acc = acc * factorial
    print(acc)

print(factorial(6))


