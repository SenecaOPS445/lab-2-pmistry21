#!/usr/bin/env python3

# Description: This program will use sys to output the user's name, as well as their age.
import sys

name = sys.argv[1]
age = int(sys.argv[2])

print("Hi " + str(name) + ", you are " + str(age) + " years old.")
