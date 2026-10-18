# Problem 20 : Validating the Phone Number
# HackerRank link :
https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com

import re

n = int(input())

for _ in range(n):
    s = input()
    if re.fullmatch(r'[789]\d{9}', s):
        print("YES")
    else:
        print("NO")
