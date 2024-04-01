def palabras_que_comienzan_con_letra(lista_palabras, letra):
    """
    Función para filtrar palabras que comienzan con una letra específica.
    
    Args:
    lista_palabras (list): Lista de palabras
    letra (str): Letra con la que deben comenzar las palabras
    
    Returns:
    list: Lista de palabras que comienzan con la letra especificada
    """
    palabras_filtradas = [palabra for palabra in lista_palabras if palabra.startswith(letra)]
    return palabras_filtradas

# Solicitar al usuario que ingrese las palabras
print("Ingrese las palabras una por una. Presione Enter para finalizar.")
palabras = []
while True:
    palabra = input("Palabra: ")
    if palabra == "":
        break
    palabras.append(palabra)

# Solicitar al usuario que ingrese la letra para filtrar las palabras
letra_a_filtrar = input("Ingrese la letra para filtrar las palabras que comienzan con ella: ")

# Llamar a la función para filtrar las palabras
palabras_filtradas = palabras_que_comienzan_con_letra(palabras, letra_a_filtrar)

# Mostrar la lista de palabras que comienzan con la letra especificada
print(f"Palabras que comienzan con la letra '{letra_a_filtrar}':")
for palabra in palabras_filtradas:
    print(palabra)
