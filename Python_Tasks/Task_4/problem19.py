# Problem 19 : Collections.Counter()
# HackerRank :
https://www.hackerrank.com/challenges/collections-counter/problem

X = int(input())
shoes = list(map(int,input().split()))

N = int(input())
money = 0

for i in range(N):
    size, price = map(int,input().split())
    
    if size in shoes:
        money += price
        shoes.remove(size)
        
print(money)
