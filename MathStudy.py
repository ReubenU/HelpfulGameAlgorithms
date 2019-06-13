# Author:   Reuben Unicruz
# Date:     4/9/2019

import math


# Sigmoid logistical function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

print(sigmoid(1))
