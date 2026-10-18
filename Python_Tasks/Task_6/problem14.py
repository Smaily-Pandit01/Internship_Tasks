# Problem 14 : Set .intersection() Operation
# HackerRank link :
https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

n = int(input())
a = set(map(int,input().split()))

m = int(input())
b = set(map(int,input().split()))

print(len(a.intersection(b)))
