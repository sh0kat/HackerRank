"""
Day 9: Recursion
Objective 
Today, we're learning and practicing an algorithmic concept called Recursion. Check out the Tutorial tab for learning materials and an instructional video!

Recursive Method for Calculating Factorial 
Task 
Write a factorial function that takes a positive integer,  as a parameter and prints the result of  ( factorial).

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .
"""

#!/bin/python3

import sys

def factorial(n):
    # Complete this function
    return 1 if n == 1 else factorial(n - 1) * n
    
if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
