# -*- coding: utf-8 -*-

import sys

def no_pair(arg):
    odd_arg = ""

    for i in range(len(arg)):
        found_pair = False

        for j in range(len(arg)):
            if i != j and arg[i] == arg[j]:
                found_pair = True
                break

        if not found_pair:
            odd_arg += arg[i]
    
    return odd_arg

argument = sys.argv[1:]

result = no_pair(argument)
print(result)


    