# Breaking records

# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

# Author: Miguel Anguita

#!/bin/python3

import math
import random
import re

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max = scores[0]
    min = scores[0]
    count_max = count_min = 0
    number_records = []

    for i in range(1,len(scores)):
        if(scores[i] > max):
            max = scores[i]
            count_max += 1
        elif(scores[i] < min):
            min = scores[i]
            count_min +=1
    number_records.extend([count_max,count_min])

    return number_records

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(result)
