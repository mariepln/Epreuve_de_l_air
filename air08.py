# -*- coding: utf-8 -*-

import sys
import error_handling

def sorted_fusion(array1, array2):
    new_array = []
    i, j = 0, 0
    
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            new_array.append(array1[i])
            i += 1
        else:
            new_array.append(array2[j])
            j += 1

    new_array.extend(array1[i:])
    new_array.extend(array2[j:])

    return new_array

error_handling.check_arguments_less_than_2()

separator = "fusion"
arguments = sys.argv[1:]  # Exclut le nom du script (premier élément)
array1 = []
array2 = []
after_separator = False

if separator not in arguments:
    print("separator error")
    sys.exit(1)

for arg in arguments:
    if arg == separator:
        after_separator = True
    elif after_separator:
        array1.append(int(arg))
    else:
        array2.append(int(arg))

if not array1 or not array2:
        print("error")
        sys.exit(1)

for i in range (len(array1) - 1):
    if array1[i] > array1[i+1]:
        print("sorted error")
        sys.exit(1)

for j in range (len(array2) - 1):
    if array2[j] > array2[j+1]:
        print("sorted error")
        sys.exit(1)

result = sorted_fusion(array1, array2)
result_str = " ".join(map(str, result))
print(result_str)