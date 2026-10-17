# Problem 13 : Nested Lists
# HackerRank link : 
https://www.hackerrank.com/challenges/nested-list/problem

    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    scores = sorted(set(score for name, score in students))
    second = scores[1]
    
    for name, score in sorted(students):
        if score == second:
            print(name)          
