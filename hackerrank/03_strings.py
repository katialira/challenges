#!/bin/python3

import math
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n, y):
    times = 0
    for letter in s:
        if letter == 'a':
            times += 1
    
    l = len(s)
    m = math.floor(n/l)
    a = times * m
    t = l * m
    r = n - t

    if n%l > 0 :
        for letter in s[:r]:
            if letter == 'a':
                a += 1
    return a

if __name__ == '__main__':
    repeatedString('aba', 10, 7)
    repeatedString('a', 1000000000000, 1000000000000)
    repeatedString('gfcaaaecbg', 547602, 164280)
    repeatedString('epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq', 549382313570, 16481469408)
    repeatedString('ojowrdcpavatfacuunxycyrmpbkvaxyrsgquwehhurnicgicmrpmgegftjszgvsgqavcrvdtsxlkxjpqtlnkjuyraknwxmnthfpt', 685118368975, 41107102139)
    repeatedString('babbaabbabaababaaabbbbbbbababbbabbbababaabbbbaaaaabbaababaaabaabbabababaabaabbbababaabbabbbababbaabb', 860622337747, 395886275361)
    repeatedString('bcbccacaacbbacabcabccacbccbababbbbabcccbbcbcaccababccbcbcaabbbaabbcaabbbbbbabcbcbbcaccbccaabacbbacbc', 649606239668, 162401559918)
    repeatedString('aadcdaccacabdaabadadaabacdcbcacabbbadbdadacbdadaccbbadbdcadbdcacacbcacddbcbbbaaccbaddcabaacbcaabbaaa', 942885108885, 330009788107)
    repeatedString('aedbdaeaddadddcedcbbabdccbecaecaccdbebeeadadcaabbaabbaeeeecaddbcdecbbdccdebaaebecdaaabbcdeccbabaabce', 731869010806, 168329872486)
