# Bon Appetit

# https://www.hackerrank.com/challenges/bon-appetit/problem

# Author: Miguel Anguita

#!/bin/python3

import math
import random
import re

def bonAppetit(bill, k, b):
    print(b - (sum(bill)-bill[k])//2 or "Bon Appetit")

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
