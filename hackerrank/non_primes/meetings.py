#!/bin/python3

import math
import os
import random
import re
import sys



# Explicación https://www.dropbox.com/s/unn8beeffk6l6zm/Screen%20Shot%202020-02-09%20at%2012.48.37.png?dl=0

def countMeetings(arrival, departure):
    # primer solución 
    meetings = []
    for m in range(len(arrival)):
        if arrival[m] not in meetings:
            meetings.append(arrival[m])
        elif departure[m] not in meetings:
            meetings.append(departure[m])

    # intento con list comp
    m = []
    a = [ m.append(i) for i in arrival if i not in m ]
    d = [ m.append(f) for f in departure if f not in m ]

    return len(m)

if __name__ == '__main__':
    result = countMeetings([1,2,1,2,2], [3,2,1,3,3])
    print(str(result))
    result = countMeetings([1,2,3,3,3], [2,2,3,4,4])
    print(str(result))
    result = countMeetings([1,1,2], [1,2,2])
    print(str(result))
