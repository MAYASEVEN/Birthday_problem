#!/usr/bin/sage -python
#Author : MaYaSeVeN
from sage.all import *

# p(n) is the probability of at least two of the n people sharing a birthday.
# p(n') is all n birthdays are different.
# 1 = P(n) + P(n')
# P(n') = 365!/[(365-n)!*365^n]
# P(n) = 1 - 365!/[(365-n)!*365^n]

Pn = [[n,(1.0 - factorial(365)/(factorial(365-n)*365**n))] for n in range(1,100)]
print str(Pn)
line = line(Pn, thickness=2, rgbcolor=(0.5,1,0.5))
text = text("The probability of at least two people in the room having the same birthday.", (0.6,0.2), axis_coords=True, fontsize="12")
show(line + text)
