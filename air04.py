# -*- coding: utf-8 -*-

import sys

def only_one(string_with_double):
    double = ""
    string = ""
    for i in range(len(string_with_double) - 1):
        if string_with_double[i] == string_with_double[i + 1]:
            double += string_with_double[i + 1]
        else:
            string += string_with_double[i]

    # Ajouter manuellement le dernier caractère à 'string'
    string += string_with_double[-1]

    return string

string = sys.argv[1]

result = only_one(string)
print(result)


