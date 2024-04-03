def calcular_mcd(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números enteros utilizando el algoritmo de Euclides.

    Args:
        a (int): El primer número.
        b (int): El segundo número.

    Returns:
        int: El máximo común divisor de los dos números.
    """
    while b != 0:
        a, b = b, a % b
    return a


def ingresar_numero(mensaje):
    """
    Solicita al usuario que ingrese un número entero desde la consola.

    Args:
        mensaje (str): El mensaje que se muestra al usuario.

    Returns:
        int: El número ingresado por el usuario.
    """
    while True:
        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")


def main():
    """
    Función principal que solicita al usuario dos números enteros, calcula su máximo común divisor
    y muestra el resultado.
    """
    print("Calculadora de Máximo Común Divisor (MCD)")
    num1 = ingresar_numero("Ingrese el primer número: ")
    num2 = ingresar_numero("Ingrese el segundo número: ")

    mcd = calcular_mcd(num1, num2)
    print(f"El MCD de {num1} y {num2} es: {mcd}")


if __name__ == "__main__":
    main()
