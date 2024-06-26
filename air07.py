# -*- coding: utf-8 -*-

import sys
import error_handling

def sorted_insert(array, new_element):
    new_array = []
    inserted = False # vérifier si nouvel élement est inséré dans ma liste

    for element in array:
        if not inserted and element > new_element:
            new_array.append(new_element)
            inserted = True
        new_array.append(element)

    if not inserted:
        new_array.append(new_element)

    return new_array

error_handling.check_arguments_less_than_2()

try:
    my_array = [int(x) for x in sys.argv[1:-1]]
    last_element = int(sys.argv[-1])
except ValueError:
    print("error: integer only")
    sys.exit(1)



result = sorted_insert(my_array, last_element)

result_str = " ".join(map(str, result))
print(result_str)
