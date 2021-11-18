'''
31. Write a Python program to print yesterday, today, tomorrow.
32. Write a Python program to print next 5 days starting from today.
33. Write a Python program to get days between two dates.
34. Write a Python program to count the number of characters (character frequency) in a
string.
35. Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string
length of the given string is less than 3, leave it unchanged.
36. Write a Python program to find the first appearance of the substring 'not' and 'poor'
from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring
with 'good'. Return the resulting string.
37. Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!' Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
38. Write a Python program to remove the nth index character from a nonempty string.
39. Write a Python script that takes input from the user and displays that input back in
upper and lower cases.
40. Write a Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form (alphanumerically).
'''

# 31

from datetime import date, timedelta
from collections import Counter


def yes_tod_tomo():
    current = date.today()
    previous = current - timedelta(1)
    tomorrow = current + timedelta(+1)

    print('today:', current, 'yesterday:', previous, 'tomorrow:', tomorrow)

# 32


def nxt_five():

    current = date.today()
    print('today:', current)
    for i in range(1,5):

        print('next will be:', current + timedelta(i))


nxt_five()


# 33


def nums_days(d1, d2):

    a = date(*d1)
    b = date(*d2)
    print('number of days in-between are:', (a-b).days)


nums_days([2018, 12, 13], [2019, 12, 13])


# 34


def count_chars(word):
    return Counter(word)


count_chars('hello')

# 35


def add_ing(word):

    if len(word) < 3:

        return word
    elif len(word) >= 3 and word.endswith('ing'):
        word = word+'ly'
        return word

    elif len(word) >= 3:
        word = word + 'ing'
        return word


add_ing('cating')

# 36, 37


def find_np(word):
    s1 = word.find('not')
    s2 = word.find('poor')

    if s1 < s2:
        word = word.replace(word[s1:s2 + 4], 'good')
        return word


find_np('this dish is not soo poor')

# 38


def rem_str(word, c):

    if word is not None:
        word = [i for i in word]
        #print(word)
        word.remove(c)
        return ''.join(word)


rem_str('hey', 'e')


# 39

def up_low():

    word = input('enter any string:')

    print('upper case of word is :', word.upper())
    print('lower case of word is :', word.lower())


up_low()

# 40


def word_sort():

    word = input().split(',')
    return sorted(set(word))


word_sort()

