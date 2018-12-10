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

num = 0
pre_val = [0,]
start_time = time.time()
duplicate = False
iterations = 0

while not duplicate:
    iterations += 1
    with open(sys.argv[1]) as fh:
        for line in fh:
            if line != '':
                num = num + int(line)
                if num in pre_val:
                    print('Reached twice:{}'.format(num))
                    duplicate = True
                    break
                else:
                    pre_val.append(num)

print('Iterated {} times over {}'.format(iterations, (time.time() - start_time)))
print('Valued reached twice: {}'.format(num))
