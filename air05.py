# -*- coding: utf-8 -*-

import sys

def operation_on_each(number_list, operation):
    new_list = []
    for i in range(len(number_list)):
        new_number = int(number_list[i]) + int(operation)
        new_list.append(new_number)

    return new_list

args = sys.argv[1:]
last_arg = args[-1]
without_last_arg = args[:-1]

result = operation_on_each(without_last_arg, last_arg)
result_str = " ".join(map(str, result))
print(result_str)
