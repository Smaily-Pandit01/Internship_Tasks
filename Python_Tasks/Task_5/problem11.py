# Problem 11 : Text Wrap
# HackerRank link :
https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
