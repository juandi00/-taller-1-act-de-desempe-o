def ordenar_nombres(lista_nombres):
    """
    Función para ordenar una lista de nombres alfabéticamente.
    
    Args:
    lista_nombres (list): Lista de nombres
    
    Returns:
    list: Lista de nombres ordenada alfabéticamente
    """
    lista_nombres.sort()  # Ordena la lista alfabéticamente
    return lista_nombres

# Solicitar al usuario que ingrese los nombres
print("Ingrese los nombres uno por uno. Presione Enter para finalizar.")
nombres = []
while True:
    nombre = input("Nombre: ")
    if nombre == "":
        break
    nombres.append(nombre)

# Llamar a la función para ordenar los nombres
nombres_ordenados = ordenar_nombres(nombres)

# Mostrar la lista de nombres ordenada alfabéticamente
print("Lista de nombres en orden alfabético:")
for nombre in nombres_ordenados:
    print(nombre)
