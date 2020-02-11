#!/bin/python3

import math
import os
import random
import re
import sys

def consumer():
    while True:
        x = yield
        print(x)

def producer(n):
    for _ in range(n):
        x = int(input())
        yield x

# Complete the 'rooter', 'squarer', and 'accumulator' function below.

def rooter():
    # Receive one number
    # Yield the square root of that number
    # Take the floor after doing the square root of the input
    n = yield
    while True:
        n = yield math.floor(math.sqrt(n))

def squarer():
    # Receive one number
    # Yield the square of that number
    n = yield
    while True:
        n = (yield n*n)

def accumulator():
    # Starts from zero
    # Receive one number
    # Add to the previously kept answer
    t = 0
    while True:
        n = (yield t)
        if n is not None:
            t += n

# Recibe
# 1. Arreglo de operaciones [square, accumulate]
# 2. cantidad de números
# 3. Numero1 - procesa las operaciones - da resultado

# Error
# Recibe el arreglo de las operaciones  - [square, accumulate]
# Recibe los numeros a evaluar          - 2
# Recibe el primer números              - 9
# Da un resultado                       - 81
# Espera el segundo número              - 1
# StopIteration

# [square, accumulate]
# 2
# 9
# 81
# 1
# Traceback (most recent call last):
#   File "hackerrank/non_primes/square_root_a.py", line 78, in <module>
#     pipeline(prod, eval(order), cons)
#   File "hackerrank/non_primes/square_root_a.py", line 54, in pipeline
#     num = w.send(num)
# StopIteration

def pipeline(prod, workers, cons):
    for num in prod:
        for i, w in enumerate(workers):
            num = w.send(num)
        cons.send(num)
    for worker in workers:
        worker.close()
    cons.close()

if __name__ == '__main__':
    order = input().strip()
    n = int(input())

    prod = producer(n)

    cons = consumer()
    next(cons)
    
    root = rooter()
    next(root)

    accumulate = accumulator()
    next(accumulate)

    square = squarer()
    next(square)

    pipeline(prod, eval(order), cons)
