# Apple and Orange

# https://www.hackerrank.com/challenges/apple-and-orange/problem

# Author: Miguel Anguita

#!/bin/python3

import math
import random
import re

def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_fruits = [0,0]
    for i in apples:
        if a + i >= s and a + i <= t:
            total_fruits[0]+=1
    for j in oranges:
        if b + j >= s and b + j <= t:
            total_fruits[1]+=1
    print(total_fruits[0])
    print(total_fruits[1])

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
