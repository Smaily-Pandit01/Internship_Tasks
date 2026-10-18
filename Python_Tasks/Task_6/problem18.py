# Problem 18 : Set Mutations
# HackerRank link : 
https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
A = set(map(int,input().split()))

for _ in range(int(input())):
    command, size = input().split()
    B = set(map(int,input().split()))
    
    if command == 'update':
        A.update(B)
    elif command == 'intersection_update':
        A.intersection_update(B)
    elif command == 'difference_update':
        A.difference_update(B)
    elif command == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
        
print(sum(A))
