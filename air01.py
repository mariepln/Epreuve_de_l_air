# -*- coding: utf-8 -*-

import sys

def string_to_array(string_to_cut, string_separator):
    array = []
    start = 0
    separator_length = len(string_separator)
    string_length = len(string_to_cut)
    
    while start < string_length:
        index = -1
        for i in range(start, string_length):
            if string_to_cut[i:i + separator_length] == string_separator:
                index = i
                break
        
        if index == -1:
            index = string_length
        
        array.append(string_to_cut[start:index])  # Ajoutez la partie avant le séparateur
        start = index + separator_length  # Mettez à jour le point de départ pour la prochaine itération
    
    return array

argument = sys.argv[1]
separator = sys.argv[2]

result = string_to_array(argument, separator)
for word in result:
    print(word)

