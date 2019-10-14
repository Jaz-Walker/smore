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

