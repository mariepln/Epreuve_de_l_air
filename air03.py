# -*- coding: utf-8 -*-

import sys
import error_handling

def no_pair(arg):
    odd_arg = []
    even_arg = []

    for i in range(len(arg)):
        found_pair = False

        for j in range(len(arg)):
            if i != j and arg[i] == arg[j]:
                found_pair = True
                even_arg.append(arg[i])

        if not found_pair:
            odd_arg.append(arg[i])
    
    return odd_arg

error_handling.check_arguments_less_than_2()

argument = sys.argv[1:]

result = no_pair(argument)
for word in result:
    print(word)


    