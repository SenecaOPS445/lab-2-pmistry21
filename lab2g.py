#!/usr/bin/env python3
# Author: Prasad Mistry
# Author ID: pmistry21
# Date Created: 2024/05/24

# Description: This script will countdown a rocket taking off using sys.

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
