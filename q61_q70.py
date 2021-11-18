'''
61. Write a Python program that accepts a hyphen-separated sequence of words as input
and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow

62. Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the
players want to start a new game)
63. Remember the rules:
64. Rock beats scissors
65. Scissors beats paper
66. Paper beats rock

67. Write a program that takes a list and returns a new list that contains all the elements of
the first list minus all the duplicates.
68. Write a Python script to display the
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
69. Write a Python program to determine whether a given year is a leap year.
70. Write a Python program to convert a string to datetime.
'''


from datetime import date
import datetime

# 61


def hyphen():

    word = input().split('-')

    word = sorted(word)
    return 'after sorting:', '-'.join(word)


hyphen()


# 62,63,64,65,66

def rock_paper_scissors():

    p1 = input('enter your move:')
    p2 = input('enter your move:')

    if p1 == 'rock' and p2 == 'scissors':
        print('p1 wins')

    elif p1 == 'rock' and p2 == 'paper':
        print('p2 wins')

    elif p1 == 'rock' and p2 == 'rock':
        print('draw')

    elif p1 == 'scissors' and p2 == 'rock':
        print('p2 wins')

    elif p1 == 'scissors' and p2 == 'paper':
        print('p1 wins')

    elif p1 == 'scissors' and p2 == 'scissors':
        print('draw')

    elif p1 == 'paper' and p2 == 'rock':
        print('p1 wins')

    elif p1 == 'paper' and p2 == 'paper':
        print('draw')

    elif p1 == 'paper' and p2 == 'scissors':
        print('p2 wins')


rock_paper_scissors()


# 67


def lit_duplicates(l1):

    l3 = [i for i in l1 if l1.count(i) == 1]
    return l3


lit_duplicates([1, 3, 6, 8, 1])


# 68


def time_current():

    curr_date = date.today()
    print("todays date: ", curr_date)
    print("current year:", curr_date.year)
    print("current month:", curr_date.month)
    print("current day:", curr_date.day, 'th')
    print("curr day name: ", curr_date.today().strftime("%A"))


time_current()


# 69

def check_leap(year):

    if year % 4 == 0 and year % 100 != 0:
        print(year, 'is a leap year')

    elif year % 400 == 0:
        print(year, 'is a leap year')
    else:
        print(year, 'is not a leap year')


check_leap(2006)


# 70


def str_to_datetime(word):

    format = '%b %d %Y %I:%M%p'
    today = datetime.datetime.strptime(word, format)

    return today


wor = 'Nov 16 2021 12:28PM'
print(str_to_datetime(wor))


