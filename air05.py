# -*- coding: utf-8 -*-

import sys
import error_handling

def operation_on_each(number_list, operation):
    new_list = []
    for i in range(len(number_list)):
        new_number = int(number_list[i]) + int(operation)
        new_list.append(new_number)

    return new_list

error_handling.check_arguments_less_than_2()

args = sys.argv[1:]
last_arg = args[-1]
without_last_arg = args[:-1]

error_handling.check_number_only(args)

result = operation_on_each(without_last_arg, last_arg)
result_str = " ".join(map(str, result))
print(result_str)
