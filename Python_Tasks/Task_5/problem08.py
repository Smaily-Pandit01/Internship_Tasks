# Problem 08 : Set .add()
# HackerRank link :
https://www.hackerrank.com/challenges/py-set-add/problem

N = int(input())
countries = set()

for i in range(N):
    countries.add(input())
    
print(len(countries))
