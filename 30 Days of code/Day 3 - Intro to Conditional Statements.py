"""
Objective 
In this challenge, we're getting started with conditional statements. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.
"""

#!/bin/python3

import sys

N = int(input().strip())
if (N % 2) != 0:
    print('Weird')
else:
    if (2 <= N) and (N <= 5):
        print("Not Weird")
    elif (6 <= N) and (N <= 20):
        print("Weird")
    else:
        print("Not Weird")
    
    
    