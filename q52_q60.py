'''
52. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
53. Write a Python program to find the repeated items of a tuple.
54. Write a Python program to find those numbers which are divisible by 7 and multiple of
5, between 1500 and 2700 (both included).
55. Write a Python program to count the number of even and odd numbers from a series of
numbers.
56. Write a Python program to get the Fibonacci series between 0 to 50.
57. Write a Python program that accepts a string and calculate the number of digits and
letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2
58. Write a Python function to multiply all the numbers in a list.
59. Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
60. Write a Python function that accepts a string and calculate the number of upper case
letters and lower case letters.
'''


# 52

from collections import Counter


def word_dic(word):

    return Counter(word)


word_dic('aabc')


# 53

def tup_cnt(tup,n):
    if tup.count(n)> 0 :
        print(n, 'has repeated ', tup.count(n), 'times')


tup_cnt((1, 1, 3, 456, 78, 1, 1), 1)


# 54


def multi_divi():

    print('numbers which are divisible by 7 and are multiple of 5 are:')

    for i in range(1500, 2700):
        if i % 7 == 0 and i % 5 == 0:
            print(i, end=' ')


multi_divi()


# 55


def eve_odd(n):

    eve, odd = 0, 0
    for i in range(n):
        if i % 2 == 0:
            eve += 1

        else:
            odd += 1

    print('count of even and odd are',eve, odd)


eve_odd(10)


# 56


def fib(n):

    n = 0
    n1 = 1

    if n == 1:
        print(n)

    else:
        print(n)
        print(n1)

        for i in range(2, n):

            n2 = n + n1
            n, n1 = n1, n2
            print(n2)


fib(50)


# 57


def cnt_ld(word):
    d = 0
    l = 0
    for i in word:
        if i.isdigit():
            d += 1
        elif i.isalpha():
            l += 1

    print('Letters:', l, 'Digits:', d)


cnt_ld('Python 3.2')


# 58, 59

def mul_lis(lit):
    mul = 1
    for i in lit:
        mul *= i
    return 'after multiplying the list:', mul


mul_lis([45,23,89,22])


# 60


def cnt_up(word):

    u = 0
    l = 0
    for i in word:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1

    print('Upper:', u, 'Lower:', l)


cnt_up('Python 3.2')


