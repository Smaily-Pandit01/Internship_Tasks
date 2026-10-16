# Problem 20 : No Idea!
# HackerRank link :
https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
arr = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(sum(1 if x in A else -1 if x in B else 0 for x in arr))
