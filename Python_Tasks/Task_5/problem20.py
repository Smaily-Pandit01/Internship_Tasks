# Problem 20 : Piling Up!
# HackerRank link :
https://www.hackerrank.com/challenges/piling-up/problem

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    
    left,right = 0, n-1
    last = float('inf')
    
    while left <= right:
        if a[left] >= a[right]:
            curr = a[left]
            left += 1
        else:
            curr = a[right]
            right -= 1
            
        if curr > last:
            print("No")
            break
        last=curr
    else:
        print("Yes")
