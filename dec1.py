#!/usr/bin/env python

"""
December 1, 2018 Advent puzzle

A value like +6 means the current frequency increases by 6; a value like -3
means the current frequency decreases by 3.

For example, if the device displays frequency changes of +1, -2, +3, +1, then
starting from a frequency of zero, the following changes would occur:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
In this example, the resulting frequency is 3.

Here are other example situations:

+1, +1, +1 results in  3
+1, +1, -2 results in  0
-1, -2, -3 results in -6
Starting with a frequency of zero, what is the resulting frequency after all of
the changes in frequency have been applied?
"""

import sys

START_VAL = 0

def main():
    """ Main function"""
    num = START_VAL
    with open(sys.argv[1], 'r') as fh:
        data = fh.read()
        for line in data.split('\n'):
            if line != '':
                num = num + int(line)

    print('Final num = {}'.format(num))


if __name__ == '__main__':
    main()
