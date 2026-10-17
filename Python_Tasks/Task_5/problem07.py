# Problem 07 : Symmetric Difference
# HackerRank link :
https://www.hackerrank.com/challenges/symmetric-difference/problem

def symmetric_difference(M, A, N, B):
    return sorted(set(A) ^ set(B))


M = int(input())
A = list(map(int, input().split()))

N = int(input())
B = list(map(int, input().split()))

result = symmetric_difference(M, A, N, B)

for x in result:
    print(x)
