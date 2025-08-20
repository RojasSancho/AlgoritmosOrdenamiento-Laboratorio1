import random, timeit

def deepseek_selection_sort(array, elements_amount):
    for step in range(elements_amount - 1):
        minimum_index = step
        
        for current_index in range(step + 1, elements_amount):
            if array[current_index] < array[minimum_index]:
                minimum_index = current_index
        
        if minimum_index != step:
            array[step], array[minimum_index] = array[minimum_index], array[step]
            