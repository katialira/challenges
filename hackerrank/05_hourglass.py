#!/bin/python3
# link: https://hackerrank-challenge-pdfs.s3.amazonaws.com/13581-2d-array-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1578965346&Signature=19e%2BJPSO3SeBALOm91SR5B7ELDI%3D&response-content-disposition=inline%3B%20filename%3D2d-array-English.pdf&response-content-type=application%2Fpdf

import math
import random
import re
import sys

# Complete the hourglassSum function below.

def hourglassSum(arr):
    clocks = []
    clock = 0
    l = 0

    for a in range(4):
        i = 0
        for b in range(4):
            c = 0
            c += arr[l][i] + arr[l][i+1] + arr[l][i+2] 
            c += arr[l+1][i+1]
            c += arr[l+2][i] + arr[l+2][i+1] + arr[l+2][i+2]
            clocks.append(c)
            if i == 0 and l == 0:
                clock = c
            elif c > clock:
                clock = c
            i += 1
        l+=1

    print('') 
    print(clocks, clock)

    return clock

if __name__ == '__main__':
    #arr = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]
    arr = [[-1, -1, 0, -9, -2, -2],[-2, -1, -6, -8, -2, -5],[-1, -1, -1, -2, -3, -4],[-1, -9, -2, -4, -4, -5],[-7, -3, -3, -2, -9, -9],[-1, -3, -1, -2, -4, -5]]
    result = hourglassSum(arr)
    # print(result)
