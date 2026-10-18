# Problem 15 : Set .difference() Operation
# HckerRank link :
https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(input())
a = set(map(int,input().split()))

m = int(input())
b = set(map(int,input().split()))

print(len(a.difference(b)))
