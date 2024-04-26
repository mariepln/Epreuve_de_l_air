import sys
import error_handling

def my_quick_sort (array):
    if len(array) <= 1:
        return array
    
    pivot = array[-1]
    less_pivot = []
    greater_pivot = []

    for i in range (len(array)- 1):
        if int(array[i]) <= int(pivot):
            less_pivot.append(array[i])
        else:
            greater_pivot.append(array[i])

    less_pivot = my_quick_sort(less_pivot)
    greater_pivot = my_quick_sort(greater_pivot)

    return less_pivot + [pivot] + greater_pivot

error_handling.check_arguments_less_than_1()

arg = sys.argv[1:]

error_handling.check_number_only(arg)

result = my_quick_sort(arg)
print(' '.join(map(str, result)))
