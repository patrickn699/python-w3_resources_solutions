'''
71. Write a Python program to subtract five days from current date.
72. Write a Python program to print yesterday, today, tomorrow.
73. Write a Python program to get days between two dates.
74. Write a Python program calculates the date six months from the current date using the
datetime module.
75. Write a Python program to convert two date difference in days, hours, minutes,
seconds.
76. Write a Python program to read first n lines of a file.
77. Write a Python program to read a file line by line and store it into a list.
78. Write a Python program to count the number of lines in a text file.
79. Write a Python program to count the frequency of words in a file.
80. Write a Python program to copy the contents of a file to another file .
81. Write a Python program to write a list to a file.
82. Write a Python program to assess if a file is closed or not.
'''

# 71

from datetime import date, timedelta, datetime
from collections import Counter


def sub_five_days():
    current = date.today()
    t = timedelta(5)
    print('five days ago the date was:', current - t)


sub_five_days()


# 72

def yes_tod_tomo():

    current = date.today()
    previous = current - timedelta(1)
    tomorrow = current + timedelta(+1)

    print('today:', current, 'yesterday:', previous, 'tomorrow:', tomorrow)


yes_tod_tomo()


# 73


def day_inbetween(d1, d2):

    dd1 = date(*d1)
    dd2 = date(*d2)
    in_days = dd1 - dd2
    print('nos of days in between are:', in_days.days)


day_inbetween([2021, 11, 16],[2021, 10, 16])


# 74


def months_6():

    days = 6*365//12
    print('6 months after the date will be:', (datetime.date.today() + datetime.timedelta(days)).isoformat())


months_6()


# 75


def date_diff_seconds(d2, d1):

    diff = d2 - d1
    print('the differences are:', diff.days * 24 * 3600 + diff.seconds)
    return diff.days * 24 * 3600 + diff.seconds


def dhms_from_seconds(seconds):

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return days, hours, minutes, seconds


date1 = datetime.strptime('2021-11-01 01:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()

print("\n%d days, %d hours, %d minutes, %d seconds" % dhms_from_seconds(date_diff_seconds(date2, date1)))
print()

# 76


def read_n(fil, n):

    with open(fil, "r+") as f:

        for i in range(3):
            op = f.readline()

            print(op)
      #f.close()


read_n('demo.txt', 5)


# 77

def read_add(fil):

    lit = []

    with open(fil, "r+") as f:
        op = f.readlines()
        lit.append(op)
        f.close()

    print(lit)


read_add('demo.txt')


# 78

def read_count(fil):

    with open(fil, "r+") as f:
        op = len(f.readlines())
        print('nos of lines are:',op)
        f.close()


read_count('demo.txt')


# 79


def freq_count(fil):

    with open(fil, "r+") as f:
        op = f.read().split()
        print('frequency of words in the file are:',Counter(op))
        f.close()


freq_count('demo.txt')


# 80

def cop_write(fil, nw_fil):
    # op = None
    with open(fil, "r+") as f, open(nw_fil, 'w+') as s:
        print('reading the file')
        op = f.read()
        print(op)
        print('writing to another file')
        s.write(op)
        f.close()


cop_write('demo.txt', 'ndemo.txt')


# 81


def lis_copy(fil, lit):

    with open(fil, 'w+') as s:
        print('writing to file from list')
        s.write(*lit)
        #print(s.readlines())
        s.close()


lis_copy('demo.txt', ['text in a list format!'])


# 82

def check_close(fil):

    with open(fil, 'r') as f:
        f.readlines()
        if not f.close():
            print('file is not closed')

        else:
            print('file is closed')


check_close('demo.txt')