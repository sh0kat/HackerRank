"""
Objective 
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.
"""

#!/bin/python3

num = int(input())

phone_book = {}

for i in range(0, num):
    entry = str(input()).split(" ")

    name = entry[0]
    phone = entry[1]
    phone_book[name] = phone

for j in range(0, num):
    name = str(input())

    if name in phone_book:
        phone = phone_book[name]
        print(name + "=" + str(phone))
    else:
        print("Not found")
