#dynamic Array sum and retrieval

import math
import os
import random
import re
import sys


def dynamicArray(n, queries):
    result = []
    lastAnswer = 0
    sequences = [[] for i in range(n)]
    for data in queries:
        if int(data[0]) == 1:
            seq = sequences[(int(data[1]) ^ lastAnswer)% n]
            seq.append(int(data[2]))

        else:
            seq = sequences[(int(data[1]) ^ lastAnswer)% n]
            size = int(data[2]) % len(seq)

            lastAnswer = seq[size]
            result.append(lastAnswer)

    return result


def main():
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print(result)

if __name__ == '__main__':
    main()
