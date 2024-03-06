# -*- coding: utf-8 -*-

import sys

def to_the_left (array):
    shift = 1 
    i = 0

    while i < shift:
        first_element = array[0]
        for j in range(len(array) - 1):
            array[j] = array[j + 1]
        array[-1] = first_element
        i += 1
    
    return array

arguments = sys.argv[1:]

result = to_the_left(arguments)
result_str = ", ".join(result)
print(result_str)