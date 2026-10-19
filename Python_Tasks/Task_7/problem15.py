# Problem 15 : Game of Thrones - I
# HackerRank link :
https://www.hackerrank.com/challenges/game-of-thrones/problem

import math
import os
import random
import re
import sys
from collections import Counter

def gameOfThrones(s):
    freq = Counter(s)
    odd = sum(1 for count in freq.values() if count % 2 != 0)
    
    if odd <= 1:
        return "YES"
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
