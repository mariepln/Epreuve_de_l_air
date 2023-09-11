# -*- coding: utf-8 -*-

import sys

def sort_with_letter(string_array, string):
    my_new_array = []
    with_string = []
    for i in range(len(string_array) - 1):
        if string in string_array[i]:
            with_string.append(string_array[i])
        else:
            my_new_array.append(string_array[i])

    return my_new_array

array = sys.argv[1:]
last_arg = array[-1]

result = sort_with_letter(array, last_arg)

if len(result) > 1:
    result_str = ", ".join(result)
else:
    result_str = result[0]

print(result_str)
