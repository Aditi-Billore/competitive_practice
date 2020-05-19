#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#
import collections
def mostActive(customers):
    # Write your code here
    list1 = []
    countDict = collections.Counter(customers)
    for index,key in enumerate(countDict):
        print("{}   {}  ".format(key,countDict[key]/len(customers)))
        if ((countDict[key]/len(customers))*100)>=5.00:
            list1.append(key)
            print(((countDict[key]/len(customers))*100))
    print(len(customers))
    list1.sort()
    return list1

def main():
    customers = ['Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 'Beta']
    result = mostActive(customers)
    print(result)

if __name__ == '__main__':
    main()
