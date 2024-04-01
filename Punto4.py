def suma_numeros_pares(lista_numeros):
    """
    Función para calcular la suma de los números pares en una lista.
    
    Args:
    lista_numeros (list): Lista de números
    
    Returns:
    int: Suma de los números pares
    """
    suma_pares = sum(numero for numero in lista_numeros if numero % 2 == 0)
    return suma_pares

# Solicitar al usuario que ingrese los números
print("Ingrese los números uno por uno. Presione Enter para finalizar.")
numeros = []
while True:
    numero_str = input("Número: ")
    if numero_str == "":
        break
    numeros.append(int(numero_str))

# Calcular la suma de los números pares
suma_pares = suma_numeros_pares(numeros)

# Mostrar la suma de los números pares
print(f"La suma de los números pares es: {suma_pares}")
