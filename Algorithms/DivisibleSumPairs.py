# DivisibleSumPairs

# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?h_r=next-challenge&h_v=zen

# Author: Miguel Anguita

#!/bin/python3

import math
import random
import re

def divisibleSumPairs(n, k, ar):
    return sum(1 for x in range(n) for j in range(x+1,n) if (ar[x] + ar[j]) % k == 0)

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(result)
