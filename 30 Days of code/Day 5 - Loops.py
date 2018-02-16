"""
Objective 
In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.

Task 
Given an integer, , print its first  multiples. Each multiple  (where ) should be printed on a new line in the form: n x i = result.
"""

#!/bin/python3

import sys


n = int(input().strip())

for i in range (1,11):
    print(n,'x',i,'=',n*i)
