# -*- coding: utf-8 -*-

import sys

if len(sys.argv) < 2:
    print("error")
else:
    file_name = sys.argv[1]
    try:
        with open(file_name, 'r') as file:
            result = file.read()
            print(result)
    except FileNotFoundError:
        print(f"error: '{file_name}' doesn't exist")

 