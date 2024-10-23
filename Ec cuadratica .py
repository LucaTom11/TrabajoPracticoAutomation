import cmath  

def calcular_discriminante(a, b, c):
    """Calcula el discriminante de la ecuación cuadrática."""
    return b**2 - 4*a*c

def calcular_raices(a, b, discriminante):
    """Calcula las raíces de la ecuación cuadrática dadas las raíces y el discriminante."""
    raiz1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
    return raiz1, raiz2

def raices_ecuacion_cuadratica(a, b, c):
    """Calcula y retorna las raíces de la ecuación cuadrática ax^2 + bx + c = 0."""
    if a == 0:
        raise ValueError("El coeficiente 'a' no puede ser 0 en una ecuación cuadrática.")
    
    discriminante = calcular_discriminante(a, b, c)
    return calcular_raices(a, b, discriminante)

# Función principal para la interacción con el usuario
def main():
    try:
        a = float(input("Ingresa el coeficiente a: "))
        b = float(input("Ingresa el coeficiente b: "))
        c = float(input("Ingresa el coeficiente c: "))

        raices = raices_ecuacion_cuadratica(a, b, c)
        print(f"Las raíces de la ecuación son: {raices[0]} y {raices[1]}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    