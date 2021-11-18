'''
1. Write a Python program which accepts the radius of a circle from the user and compute
the area.
2. Write a Python program to test whether a number is within 100 of 1000 or 2000.
3. Write a Python program to calculate the sum of three given numbers, if the values are
equal then return thrice of their sum.
4. Write a Python program to find whether a given number (accept from the user) is even
or odd, print out an appropriate message to the user.
5. Write a Python program that will accept the base and height of a triangle and compute
the area.
6. Write a Python program that will return true if the two given integer values are equal or
their sum or difference is 5.
7. Write a Python program to solve (x + y) * (x + y).
8. Write a python program to sum of the first n positive integers.
9. Write a Python function to check whether a number is divisible by another number.
Accept two integers values form the user.
10. Write a Python program to count the number of characters (character frequency) in a
string

'''

from collections import Counter

# 1


def cir_area():

    r = int(input())
    area = 2 * 3.14 * r
    print(area)


cir_area()

# 2


def check_dist():

    a = int(input())
    if abs(a-1000) <= 100 or abs(a-2000) <= 100:
        return True
    else:
        return False


check_dist()


# 3


def summ():

    li = []
    for i in range(3):
        val = int(input())
        li.append(val)

    print('sum of values are:', sum(li))

    if li[0] == li[1] == li[2]:
        print('three times of their sum is:', 3*sum(li))


summ()


# 4


def even_odd():

    num = int(input())
    if num%2 == 0:
        print(num, 'is even')
    else:
        print(num, 'is odd')


even_odd()


# 5


def triangle_area():

    base = int(input())
    height = int(input())

    print('area of triangle is:', 2*base*height)


triangle_area()


# 6


def diff():
    n = int(input())
    n1 = int(input())

    if n == n1 or (n + n1) == 5 or (n - n1) == 5:
        return True

    else:
        return False


diff()


# 7

def solve():
    x = int(input())
    y = int(input())

    return (x+y)*(x+y)


solve()


# 8

def summ_int(n):

    sum = 0
    for i in range(n):
        sum += i
    return sum


summ_int(8)


# 9

def check_divide():
    a = int(input())
    b = int(input())

    if a % b == 0:
        print('a is divisible by b')

    else:
        print('a is not divisible by b')


check_divide()

# 10


def cnt(word):

    print('occurrences of characters in the given string are:', Counter(word))


cnt('hello')