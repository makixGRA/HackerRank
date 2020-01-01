# Kangaroo

# https://www.hackerrank.com/challenges/kangaroo/problem

# Author: Miguel Anguita

#!/bin/python3

import math
import random
import re

def kangaroo(x1, v1, x2, v2):
    s = "NO"
    if(v2 >= v1):
        s = "NO"
    else:
        if((x2-x1) % (v1-v2) == 0):
            s = "YES"
        else:
            s = "NO"
    return s

if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
