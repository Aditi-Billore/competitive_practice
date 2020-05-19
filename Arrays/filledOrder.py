#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'filledOrders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k
#

def filledOrders(order, k):
    # Write your code here
    count = 0
    for i in order:
        if i<= k:
            k -= i
            count += 1
    return count

def main():
    order = [-2,10]
    k = 10
    print(filledOrders(order, k))

if __name__ == '__main__':
    main()
