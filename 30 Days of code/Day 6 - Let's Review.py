"""
Objective 
Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given a string, S, of length N that is indexed from N to N-1, print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

Note:  is considered to be an even index.
"""

#!/bin/python3

N=int(input())
for i in range(0, N):
    Str=input()
    for j in range(0,len(Str)):
        if (j%2) == 0: 
            print (Str[j],end='')
    print(' ',end='')
    for j in range(0,len(Str)):
        if (j%2) != 0: 
            print (Str[j],end='')
    print(' ')