# -*- coding: utf-8 -*-

import sys

def string_to_array (string_to_cut, string_separator):
    array = []
    words = ""
    for char in string_to_cut:
        if char not in string_separator:
            words += char
        else:
            if words:
                array.append(words)
                words = "" 
                              
    if words:
        array.append(words)
        
    return array


argument = sys.argv[1]
separator = " \t\n"

result = string_to_array(argument, separator)
for word in result:
    print(word)

 