# Migratory Birds

# https://www.hackerrank.com/challenges/migratory-birds/problem

# Author: Miguel Anguita

#!/bin/python3

!/bin/python3

import math
import random
import re

def migratoryBirds(arr):
    count = [0] * len(arr)
    for i in arr:
        count[i] += 1
    return(count.index(max(count)))


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
