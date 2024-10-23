def es_primo(n):
    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ingreso del número
entrada = input("Ingresa un número: ")

try:
    numero = int(entrada)
    if es_primo(numero):
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")
except ValueError:
    print(f"Error: '{entrada}' no es un número válido. Por favor, ingresa un número entero.")
