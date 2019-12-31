#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #10 20 20 10 10 30 50 10 20
    pairs = 0
    alones = []
    for p in ar:
        if p not in alones:
            alones.append(p)
        else:
            pairs += 1
            alones.remove(p)
    print(pairs)
    print(alones)
    return pairs

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result, '\n')