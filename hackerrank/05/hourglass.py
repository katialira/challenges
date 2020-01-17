#!/bin/python3

import math
import random
import re
import sys

# Complete the hourglassSum function below.

def hourglassSum(arr):
    return max(max_hourglass(arr))

def max_hourglass(arr):
    num_rows = len(arr)
    num_cols = len(arr[0])
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            yield (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                   arr[i + 1][j + 1] +
                   arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
    

if __name__ == '__main__':
    #arr = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]
    arr = [[-1, -1, 0, -9, -2, -2],[-2, -1, -6, -8, -2, -5],[-1, -1, -1, -2, -3, -4],[-1, -9, -2, -4, -4, -5],[-7, -3, -3, -2, -9, -9],[-1, -3, -1, -2, -4, -5]]
    result = hourglassSum(arr)
    print(result)

