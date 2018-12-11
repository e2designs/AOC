"""
Counting the number that have an ID containing exactly two of any letter and
then separately counting those with exactly three of any letter. You can
multiply those two counts together to get a rudimentary checksum and compare
it to what your device predicts.

For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly twice,
and three of them contain a letter which appears exactly three times. Multiplying
these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?
"""

import sys
DEBUG = False

def log(s):
    if DEBUG:
        print s

def main(filename):
    """
    - Read in file line by line
    - identify number of duplicates
    - increment counters for 2 and 3
    - multiply and return checksum
    """
    with open(filename) as fh:
        data = fh.read().splitlines()

    dual = 0
    triple = 0
    for line in data:
        log('Evaluating line:{}'.format(line))
        lineset = set()
        check2 = False
        check3 = False
        for char in line:
            lineset.add(char)
        log('Lineset:{}'.format(lineset))
        for char in lineset:
            char_count = line.count(char)
            if char_count == 2:
                check2 = True
            elif char_count == 3:
                check3 = True
            elif char_count > 3:
                log('Error {} appeared {} times for {}'.format(char,
                    char_count, line))
        dual += 1 if check2 else 0
        triple += 1 if check3 else 0
        log('Dual = {}, Triple = {}'.format(dual, triple))

    print('Dual = {}, Triple = {}, checksum ={}'.format(dual, triple, (dual *
        triple)))

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print('Missing file. USAGE: python puzzle3.py <inputfile>')

    main(filename)
