import random, timeit

# realiza un selection sort estandar (pseudocodigo dado en clase)
def classic_selection_sort(array, elements_amount):
    # ciclo for externo (numero de pasadas totales)
    for step in range(0, elements_amount):
        minimum_index = step
        
        # ciclo for interno (recorre desde el step en adelante para encontrar un valor 
        # menor o minimo)
        for current_index in range(step+1, elements_amount):
            # verifica si el valor del indice actual es menor que el del indice del minimo
            if array[current_index] < array[minimum_index]:
                minimum_index = current_index
                
        # intercambia el valor que se tiene en el indice step con el valor que 
        # esta en el indice del minimo
        array[step], array[minimum_index] = array[minimum_index], array[step]

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
    total_time_taken = timeit.timeit(lambda: classic_selection_sort(array.copy(), len(array.copy())), number=5)
    print(f"Promedio de 5 ejecuciones -> Tamaño Array {size}: {(total_time_taken / 5)*1000:.3f} ms.")
