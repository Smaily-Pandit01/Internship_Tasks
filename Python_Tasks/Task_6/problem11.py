# Problem 11 : String Formatting
# HackerRank link :
https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)

        print(decimal, octal, hexa, binary)

if __name__ == '__main__':
