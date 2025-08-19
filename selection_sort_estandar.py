def selection_sort(array, elements_amount):
    # ciclo for externo (numero de pasadas totales)
    for step in range(0, elements_amount):
        minimum_index = step
        # ciclo for interno (recorre desde el step en adelante para encontrar un valor 
        # menor o minimo)
        for current_index in range(step+1, elements_amount):
            #verifica si el valor del indice actual es menor que el del indice del minimo
            if array[current_index] < array[minimum_index]:
                minimum_index = current_index
        #intercambia el valor que se tiene en el indice step con el valor que 
        #esta en el indice del minimo
        array[step], array[minimum_index] = array[minimum_index], array[step]


test_array = [6,5,2,8,9,10,1,3,7,4,1,1,1,4,21]
print(test_array)

selection_sort(test_array, len(test_array))
print(test_array)
