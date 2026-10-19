# Problem 06 : Pangrams
# HackerRank link :
https://www.hackerrank.com/challenges/pangrams/problem

import math
import os
import random
import re
import sys

def pangrams(s):
    if len(set(s.lower())-{" "})==26:
        return "pangram"
    return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
