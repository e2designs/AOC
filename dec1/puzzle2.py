"""
Dec 1, 2018 puzzle #2

You notice that the device repeats the same frequency change list over and over.
To calibrate the device, you need to find the first frequency it reaches twice.

For example, using the same list of changes above, the device would loop as follows:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
(At this point, the device continues from the start of the list.)
Current frequency  3, change of +1; resulting frequency  4.
Current frequency  4, change of -2; resulting frequency  2, which has already
been seen.

In this example, the first frequency reached twice is 2.

Note that your device might need to repeat its list of frequency changes many
times before a duplicate frequency is found, and that duplicates might be found
while in the middle of processing the list.

Here are other examples:

+1, -1 first reaches 0 twice.
+3, +3, +4, -2, -4 first reaches 10 twice.
-6, +3, +8, +5, -6 first reaches 5 twice.
+7, +7, -2, -7, -4 first reaches 14 twice.
What is the first frequency your device reaches twice?
"""

from __future__ import absolute_import
import sys
import time



def store_list(filename):
    """ Brute force inefficient way with a poor data structure"""
    num = 0
    pre_val = [0,]
    start_time = time.time()
    duplicate = False
    iterations = 0

    while not duplicate:
        iterations += 1
        with open(filename) as fh:
            for line in fh:
                if line != '':
                    num = num + int(line)
                    if num in pre_val:
                        print('Reached twice:{}'.format(num))
                        duplicate = True
                        break
                    else:
                        pre_val.append(num)

    execution_time = time.time() - start_time
    print('Iterated {} times over {}'.format(iterations, execution_time))
    print('Valued reached twice: {}'.format(num))
    return iterations, execution_time, num

def read_once(filename):
    """ Same sort of Brute force and inefficient, but only read the file one
    time"""
    num = 0
    pre_val = [0,]
    start_time = time.time()
    duplicate = False
    iterations = 0
    with open(filename) as fh:
        data = fh.read().splitlines()

    while not duplicate:
        iterations += 1
        for line in data:
            if line != '':
                num = num + int(line)
                if num in pre_val:
                    print('Reached twice:{}'.format(num))
                    duplicate = True
                    break
                else:
                    pre_val.append(num)

    execution_time = time.time() - start_time
    print('Iterated {} times over {}'.format(iterations, execution_time))
    print('Valued reached twice: {}'.format(num))
    return iterations, execution_time, num

def read_int(filename):
    """ Same sort of Brute force and inefficient, but only read the file one
    time and typecast as int"""
    num = 0
    pre_val = [0,]
    start_time = time.time()
    duplicate = False
    iterations = 0
    with open(filename) as fh:
        data = map(int, fh.read().splitlines())

    while not duplicate:
        iterations += 1
        for line in data:
            num = num + line
            if num in pre_val:
                print('Reached twice:{}'.format(num))
                duplicate = True
                break
            else:
                pre_val.append(num)

    execution_time = time.time() - start_time
    print('Iterated {} times over {}'.format(iterations, execution_time))
    print('Valued reached twice: {}'.format(num))
    return iterations, execution_time, num


def store_set(filename):
    """ Store numbers as a set vs list so that a value in statement is
    efficient"""
    num = 0
    pre_val = set()
    pre_val.add(num)
    start_time = time.time()
    duplicate = False
    iterations = 0

    while not duplicate:
        iterations += 1
        with open(filename) as fh:
            for line in fh:
                if line != '':
                    num = num + int(line)
                    if num in pre_val:
                        print('Reached twice:{}'.format(num))
                        duplicate = True
                        break
                    else:
                        pre_val.add(num)

    execution_time = time.time() - start_time
    print('Iterated {} times over {}'.format(iterations, execution_time))
    print('Valued reached twice: {}'.format(num))
    return iterations, execution_time, num

def all_together(filename):
    """ Should be the most efficient:
        - Read file one time
        - Type cast to int
        - store previous results as a set
        """
    num = 0
    pre_val = set()
    pre_val.add(num)
    start_time = time.time()
    duplicate = False
    iterations = 0
    with open(filename) as fh:
        data = map(int, fh.read().splitlines())

    while not duplicate:
        iterations += 1
        for line in data:
            num = num + int(line)
            if num in pre_val:
                print('Reached twice:{}'.format(num))
                duplicate = True
                break
            else:
                pre_val.add(num)

    execution_time = time.time() - start_time
    print('Iterated {} times over {}'.format(iterations, execution_time))
    print('Valued reached twice: {}'.format(num))
    return iterations, execution_time, num

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print('Missing input file. USAGE: python puzzle2.py <inputfile>')
    results = {}
    results['list'] = store_list(filename)
    results['set'] = store_set(filename)
    results['read_one'] = read_once(filename)
    results['read_int'] = read_int(filename)
    results['efficient'] = all_together(filename)
    print results
