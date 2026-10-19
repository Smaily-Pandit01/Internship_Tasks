# Problem 19 : Weighted Uniform Strings
# HackerRank link : 
https://www.hackerrank.com/challenges/weighted-uniform-string/problem

import math
import os
import random
import re
import sys


def weightedUniformStrings(s, queries):
    weights = set()
    prev = ''
    count = 0
    
    for ch in s:
        if ch == prev:
            count += 1
        else:
            count = 1
            prev = ch
            
        weights.add((ord(ch) - ord('a') + 1)*count)
    
    return ["Yes" if q in weights else "No" for q in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
