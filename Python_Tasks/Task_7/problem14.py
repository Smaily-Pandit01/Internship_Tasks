# Problem 14 : Anagram
# HackerRank link :
https://www.hackerrank.com/challenges/anagram/problem

import math
import os
import random
import re
import sys
from collections import Counter

def anagram(s):
    n = len(s) 
    
    if n % 2 != 0:
        return - 1
        
    a = s[:n//2]
    b = s[n//2:]
    
    return sum((Counter(a) - Counter(b)).values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
