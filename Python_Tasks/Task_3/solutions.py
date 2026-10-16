# Q1. Find the Frequency of Each Word in a Sentence
import re


def word_frequency(sentence):
    d = {}
    words = sentence.split()
    for word in words:
        d[word] = words.count(word)
    return d

# Q2. Find the Frequency of Each Character in a Word
def char_frequency(word):
    d = {}
    for char in word:
        d[char] = word.count(char)
    return d

# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating_char(word):
    for char in word:
        if word.count(char) == 1:
            return char
    return None

# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Q5. Find the First Repeating Character in a String
def first_repeating_char(string):
    for char in string:
        if string.count(char)  > 1:
            return char
        
# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(numbers):
    for i in numbers:
        if i == 0:
            numbers.remove(i)
            numbers.append(0)
    return numbers
    
# Q7. Find the Second Highest Distinct Number in a List
def second_highest_number(numbers):
    distinct_numbers = list(set(numbers))
    distinct_numbers.sort()
    if len(distinct_numbers) >= 2:
        return distinct_numbers[-2]
    return None

# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(numbers):
    list_without_duplicates = []
    for i in numbers:
        if i not in list_without_duplicates:
            list_without_duplicates.append(i)
    return list_without_duplicates
    
# Q9. Find the Missing Number from 1 to N
def find_missing_number(numbers, N):
    for i in range(1, N + 1):
        if i not in numbers:
            return i
        
# Q10. Find Two Numbers Whose Sum Equals a Target
def find_two_numbers_with_sum(numbers, target):
    for i in numbers:
        for j in numbers:
            if i != j and i + j == target:
                return (i, j)
    return None

# Q11. Find the Number Closest to Zero
def closest_to_zero(numbers):
    return min(numbers, key=lambda x: (abs(x), -x)) 

# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    list3 = []
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3
        
# Q13. Rotate a List to the Right by K Positions
def rotate_list(numbers, k):
    k = k % len(numbers)
    return numbers[-k:] + numbers[:-k]

# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_sum_of_consecutive_elements(numbers):
    x = [numbers[i] + numbers[i+1] for i in range(len(numbers)-1)]
    return max(x)

# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def find_all_pairs_with_sum(numbers, target):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append(sorted([numbers[i], numbers[j]]))
    return pairs