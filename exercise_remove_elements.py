# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista después de remover los elementos indicados
    """
    resultado = lista[1:]

    # Ahora eliminamos posiciones 4 y 5 (originales)
    # En la nueva lista corresponden a índices 3 y 4
    resultado = resultado[:3] + resultado[5:]

    return resultado
