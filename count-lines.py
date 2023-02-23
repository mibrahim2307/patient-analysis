""" this module counts the number of lines in a standard input
input: string from the system standard input
""""

import sys

count=0
for line in sys.stdin:
    count += 1

print(count, ' lines in standard input')
