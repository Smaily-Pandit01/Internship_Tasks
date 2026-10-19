# Problem 08 : Gemstones
# HackerRank link :
https://www.hackerrank.com/challenges/gem-stones/problem

def gemstones(arr):
    common = set(arr[0])
    
    for s in arr[1:]:
        common = common.intersection(set(s))
        
    return len(common)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
