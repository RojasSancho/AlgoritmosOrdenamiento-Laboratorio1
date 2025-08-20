from classic_selection_sort import classic_selection_sort 
from chatgpt_selection_sort import chatgpt_selection_sort
import random, timeit

# crea un array de un tamano especifico con numeros aleatorios de 1 a 1000
def create_array(size):
    array = []
    for _ in range(size):
        random_number = random.randint(1, 1000)
        array.append(random_number)
    return array

# funcion para medir tiempo promedio de 5 ejecuciones
def measure_time(sort_function):
    sizes = [10, 100, 1000]

    for size in sizes:
        array = create_array(size)
        total_time_taken = timeit.timeit(lambda: sort_function(array.copy()), number=5)
        print(f"Promedio de 5 ejecuciones -> Tamaño Array {size}: {(total_time_taken / 5)*1000:.3f} ms.")

# se imprime tiempo promedio del selection sort clasico
print("Selection Sort clásico")
measure_time(lambda array: classic_selection_sort(array, len(array)))

# se imprime tiempo promedio del selection sort de chat gpt
print("\nSelection Sort de ChatGPT")
measure_time(lambda array: chatgpt_selection_sort(array))
