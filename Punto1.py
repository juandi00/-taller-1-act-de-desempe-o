def contar_vocales(frase):
    """
    Función para contar las vocales en una frase dada.
    
    Args:
    frase (str): La frase ingresada por el usuario
    
    Returns:
    dict: Diccionario con el conteo de cada vocal
    """
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for caracter in frase:
        if caracter.lower() in 'aeiou':
            conteo_vocales[caracter.lower()] += 1
    
    return conteo_vocales

# Solicitar al usuario que ingrese una palabra o frase
palabra_frase = input("Ingrese una palabra o frase: ")

# Llamar a la función para contar las vocales
resultado = contar_vocales(palabra_frase)

# Mostrar el conteo de cada vocal por separado
for vocal, conteo in resultado.items():
    print(f"La vocal '{vocal}' aparece {conteo} veces.")
