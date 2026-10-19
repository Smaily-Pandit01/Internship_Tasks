# Problem 01 : Set .symmetric_difference() Operation
# HackerRank link :
https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

m = int(input())
A = set(map(int,input().split()))

n = int(input())
B = set(map(int,input().split()))

result = A^B

print(len(result))
