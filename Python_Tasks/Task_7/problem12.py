# Problem 12 : Making Anagrams
# HackerRank link :
https://www.hackerrank.com/challenges/making-anagrams/problem

import math
import os
import random
import re
import sys
from collections import Counter

def makingAnagrams(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    return sum((c1-c2).values())+sum((c2-c1).values())
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
