#!/usr/bin/env python3

# Description: This program will use sys to output the user's name and age, as well as output a usage message.
import sys

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit()

name = sys.argv[1]
age = int(sys.argv[2])

print("Hi " + str(name) + ", you are " + str(age) + " years old.")