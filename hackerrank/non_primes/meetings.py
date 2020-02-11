#!/bin/python3

import math
import os
import random
import re
import sys

# Mejor Explicación
# https://www.dropbox.com/s/v24ob1koh6daj49/exMeetings.jpg

def countMeetings(arrival, departure):
    # primer solución 
    # meetings = []
    # for m in range(len(arrival)):
    #     if arrival[m] not in meetings:
    #         meetings.append(arrival[m])
    #     elif departure[m] not in meetings:
    #         meetings.append(departure[m])
    print(arrival, departure)
    m = []
    c = list(filter(lambda x: x in arrival, departure))
    print(c)

    return len(m)

if __name__ == '__main__':
    result = countMeetings([1,2,1,2,2], [3,2,1,3,3])
    print(str(result))
    result = countMeetings([1,2,3,3,3], [2,2,3,4,4])
    print(str(result))
    result = countMeetings([1,1,2], [1,2,2])
    print(str(result))
