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

# crea un array de un tamano especifico con numeros aleatorios de 1 a 1000
def create_array(size):
    array = []
    for i in range(size):
        random_number = random.randint(1, 1000)
        array.append(random_number)
    return array

# tamanos solicitados de cada arreglo para pruebas
sizes = [10, 100, 1000]

for size in sizes:
    array = create_array(size)
    total_time_taken = timeit.timeit(lambda: chatgpt_selection_sort(array.copy()), number=5)
    print(f"Promedio de 5 ejecuciones -> Tamaño Array {size}: {(total_time_taken / 5)*1000:.3f} ms.")
