# Problem 16 : Check Subset
# HackerRank link :
https://www.hackerrank.com/challenges/py-check-subset/problem

for _ in range(int(input())):
    a = int(input())
    A = set(map(int,input().split()))
    
    b = int(input())
    B = set(map(int,input().split()))
    

    print(A.issubset(B))
