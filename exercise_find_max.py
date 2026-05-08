# Ejercicio 5: Encontrar el máximo en una lista

def find_max(lista):
    """
    Encuentra y retorna el valor máximo en una lista de números.
    Si la lista está vacía, retorna None.

    Args:
        lista: Una lista de números

    Returns:
        El valor máximo de la lista o None si está vacía
    """
    if len(lista) == 0:
        return None
    else:
        maximo=max(lista)
        """maximo = lista[0]
        for numero in lista:
            if numero > maximo:
                maximo = numero"""
        return maximo
