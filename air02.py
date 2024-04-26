# -*- coding: utf-8 -*-

import sys
import error_handling

def array_to_string (array, separator):
    string = ""
    for element in array:
        string += element + separator

    return string

error_handling.check_arguments_less_than_2()

my_list = sys.argv[1:]
without_last_arg = my_list[0:-1]
separator = my_list[-1]

result = array_to_string(without_last_arg, separator)
print(result)


