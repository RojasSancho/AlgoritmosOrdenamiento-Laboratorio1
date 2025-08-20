import random, timeit

def chatgpt_selection_sort(array):
    left = 0
    right = len(array) - 1

    while left < right:
        min_index = left
        max_index = right

        for i in range(left, right + 1):
            if array[i] < array[min_index]:
                min_index = i
            elif array[i] > array[max_index]:
                max_index = i

        # Intercambiar mínimo con la izquierda
        if min_index != left:
            array[left], array[min_index] = array[min_index], array[left]
            # Si movimos el max al lugar del min, actualizar índice
            if max_index == left:
                max_index = min_index

        # Intercambiar máximo con la derecha
        if max_index != right:
            array[right], array[max_index] = array[max_index], array[right]

        left += 1
        right -= 1
