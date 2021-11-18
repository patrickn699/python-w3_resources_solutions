'''
41. Write a Python program to sum all the items in a list.
42. Write a Python program to multiplies all the items in a list.
43. Write a Python program to get the largest number from a list.
44. Write a Python program to get a list, sorted in increasing order by the last element in
each tuple from a given list of non-empty tuples.
45. Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
46. Write a Python program to create a list by concatenating a given list which range goes
from 1 to n.

47. Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
48. Write a Python script to check if a given key already exists in a dictionary.
49. Write a Python script to print a dictionary where the keys are numbers between 1 and
15 (both included) and the values are square of keys.
50. Write a Python program to combine two dictionary adding values for common keys.
'''


# 41

def sum_list(lit):
    return 'sum of list is:', sum(lit)


sum_list([45, 23, 89, 22])


# 42

def mul_lis(lit):
    mul = 1
    for i in lit:
        mul *= i
    return 'after multiplying the list:', mul


mul_lis([45, 23, 89, 22])


# 43

def largest(lit):
    return 'largest number of the list is:', max(lit)


largest([45, 23, 89, 22])


# 44, 45

def las(lit):
    return lit[-1]


def sor(lit):
    new_l = sorted(lit, key=las)
    return new_l


sor([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])


# 46, 47

def p_q(n):

    lit = []

    for i in range(1, n+1):
        lit.extend(['p'+str(i), 'q'+str(i)])

    print(lit)


p_q(4)


# 48

def check_keys(dit, k):
    for i in dit.keys():
        if i == k:
            print('given key exist')
            break

        else:
            print('given key does nto exist')
            break


check_keys({1:1, 2:45, 3:22}, 3)


# 49

def dic_kv():

    dic = {i:i**2 for i in range(1, 16)}
    return dic


dic_kv()


# 50, 51

def combine_dic(d1, d2):

    com_dic = {}
    for i in d1.keys():
        if i in d2.keys():
            com_dic.update({i:d1[i]+d2[i]})

        else:
            com_dic.update(d1.items())
            com_dic.update(d2.items())

    return com_dic


combine_dic({'a': 100, 'b': 200, 'c':300}, {'a': 300, 'b': 200, 'd':400})





