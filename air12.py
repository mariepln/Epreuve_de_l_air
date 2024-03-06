import sys 

def my_quick_sort (array):
    new_array = []
    pivot = array[-1]
    less_pivot = []
    greater_pivot = []

    for i in range (len(array)):
        if i < pivot:
            less_pivot.append(array[i])
        else:
            greater_pivot.append(array[i])
    
    return less_pivot + [pivot] + greater_pivot

arg = sys.argv[1:]

result = my_quick_sort(arg)
print(result)
