# Problem 12 : Capitalize!
# HackerRank link :
https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    words = s.split(' ')
    result = []
    for word in words:
        if word:
            result.append(word[0].upper()+word[1:])
        else:
            result.append('')
    return' '.join(result)
