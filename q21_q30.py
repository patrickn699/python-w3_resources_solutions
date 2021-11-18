'''
21. Write a Python program to reverse a tuple.
22. Write a Python program to find those numbers which are divisible by 7 and multiple of
5, between 1500 and 2700 (both included).
23. Write a Python program which iterates the integers from 1 to 50. For multiples of three
print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers
which are multiples of both three and five print "FizzBuzz".
24. Write a Python class to reverse a string word by word.
25. Write a Python class named Rectangle constructed by a length and width and a method
which will compute the area of a rectangle.
26. Write a Python function that takes a number as a parameter and check the number is
prime or not.
27. Write a Python program to print the even numbers from a given list.
28. Write a Python function to check whether a number is perfect or not
According to Wikipedia : In number theory, a perfect number is a positive integer that is
equal to the sum of its proper positive divisors, that is, the sum of its positive divisors
excluding the number itself (also known as its aliquot sum). Equivalently, a perfect
number is a number that is half the sum of all of its positive divisors (including itself).
29. Write a Python program to determine whether a given year is a leap year.
30. Write a Python program to subtract five days from current date.
'''

from datetime import date, timedelta

# 21


def reverse_tup(tup):
    return tup[::-1]


reverse_tup((2, 45, 78, 89))


# 22

def multi_divi():

    print('numbers which are divisible by 7 and are multiple of 5 are:')

    for i in range(1500, 2700):
        if i % 7 == 0 and i % 5 == 0:
            print(i, end=' ')


multi_divi()


# 23

def fizz_buzz():
    for i in range(50):
        if i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')

        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')


fizz_buzz()


# 24


class rev:

  def rever(self, word):
    return list(reversed(word.split()))


r = rev()
r.rever('this is a test sentence')


# 25

class Rectangle:

  def rect_are(self, length, breadth):
    return length*breadth


r1 = Rectangle()
r1.rect_are(10, 20)


# 26

def check_prime(n):

    for i in range(2, n):
        if n % i == 0:
            print(n, 'is not a prime number')
            break
        else:
            print(n, 'is a prime number')
            break


check_prime(7)


# 27

def print_even(lit):

    for i in lit:
        if i % 2 == 0:
            print(i, 'is even')


print_even([i for i in range(20)])


# 28


def check_perfect(n):

    perfect = 0
    for i in range(1, n):
        if n % i == 0:
            perfect += i

    if perfect == n:
        print(n, 'is a perfect number')

    else:
        print(n, 'is a perfect number')


check_perfect(6)


# 29

def check_leap(year):

    if year % 4 == 0 and year % 100 != 0:
        print(year, 'is a leap year')

    elif year % 400 == 0:
        print(year, 'is a leap year')
    else:
        print(year, 'is not a leap year')


check_leap(2006)

# 30


def sub_five_days():

    current = date.today()
    t = timedelta(5)
    print('five days ago the date was:', current - t)


sub_five_days()
