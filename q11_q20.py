'''
11. Write a Python program to get a string made of the first 2 and the last 2 chars from a
given a string. If the string length is less than 2, return “empty string”.
12. Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
13. Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string
length of the given string is less than 3, leave it unchanged.
14. Write a Python program to count the occurrences of each word in a given sentence.
15. Write a Python program to sum all the items in a list.
16. Write a Python program to remove duplicates from a list.
17. Write a Python function that takes two lists and returns True if they have at least one
common member.
18. Write a Python program to find the second smallest number in a list.
19. Write a Python program to get the maximum and minimum value in a dictionary.
20. Write a Python program to print all unique values in a dictionary.
'''

from collections import Counter

# 11


def get_str():
    word = input()
    length = len(word)
    if length < 2:
        return 'empty string'

    else:
        nw_word = word[:2] + word[-2:]
        return nw_word


get_str()


# 12

def new_str(word):
    first = word[0]
    word = word.replace(first, '$')
    word = first + word[1:]

    return word


new_str('restart')


# 13


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


# 14


def count_word(word):

    word = word.split()
    print('count of each word in the sentence is:', Counter(word))


count_word('this is a sentence sentence')


# 15

def sum_list(lis):
    return sum(lis)


sum_list([1, 5, 20, 30])


# 16

def remove_duplicate(lis):

    lis = set(lis)
    lis = list(lis)
    return lis


remove_duplicate([1, 1, 34, 56, 56, 89])


# 17

def common_member(lis1, lis2):

    for i in lis1:
        if i in lis2:
            return True
        else:
            return False


common_member([1, 4, 8], [1, 3, 6])


# 18

def second_smallest(lis):

    temp = min(lis)
    lis.remove(temp)
    return min(lis)


second_smallest([1, 2, 45, 67])

# 19


def min_max_dict(dic):

    maxx = max(dic.values())
    minn = min(dic.values())

    print('max value is:', maxx, ' min value is:', minn)


min_max_dict({1: 1, 2: 10, 3: 23})


# 20

def uniq_dict(dic):
    return set(dic.values())


uniq_dict({1: 2, 2: 2, 3: 4, 4: 5})