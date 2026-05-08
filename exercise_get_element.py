# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    """
    Retorna el elemento en la posición indicada.
    Si el índice está fuera de rango, retorna None.

    Args:
        lista: Una lista de cualquier tipo de elementos
        indice: Índice del elemento a obtener

    Returns:
        El elemento en la posición indicada o None si está fuera de rango
    """
    if len(lista)==0:
        return None

    # Convertimos índice negativo a positivo equivalente
    if indice < 0:
        indice = len(lista) + indice

    # Verificamos rango válido
    if indice < 0 or indice >= len(lista):
        return None

    return lista[indice]
