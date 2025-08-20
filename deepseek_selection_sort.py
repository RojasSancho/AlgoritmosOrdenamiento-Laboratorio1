import random, timeit

def deepseek_selection_sort(array, elements_amount):
    for step in range(elements_amount - 1):
        minimum_index = step
        
        for current_index in range(step + 1, elements_amount):
            if array[current_index] < array[minimum_index]:
                minimum_index = current_index
        
        if minimum_index != step:
            array[step], array[minimum_index] = array[minimum_index], array[step]

'''
Optimizaciones aplicadas:

Reducción de iteraciones: Cambié range(0, elements_amount) a range(elements_amount - 1) ya que en la última iteración el último elemento ya estará en su posición correcta.

Evitar intercambios innecesarios: Agregué una condición if minimum_index != step: para solo realizar el intercambio cuando sea realmente necesario, evitando operaciones redundantes.

Eliminación de parámetro redundante: Aunque mantuve la firma de la función, en la práctica elements_amount podría calcularse dentro de la función con len(array) si se desea simplificar.

Mejor legibilidad: Eliminé comentarios obvios que no aportaban información adicional, manteniendo solo la estructura clara del algoritmo.

El algoritmo mantiene exactamente la misma funcionalidad pero es más eficiente al reducir iteraciones innecesarias y evitar intercambios redundantes.
'''