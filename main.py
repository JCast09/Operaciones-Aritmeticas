import math


def calcular_mcd(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números enteros utilizando la función gcd de la biblioteca math.

    Args:
        a (int): El primer número.
        b (int): El segundo número.

    Returns:
        int: El máximo común divisor de los dos números.
    """
    return math.gcd(a, b)


def main():
    """
    Función principal que solicita al usuario dos números enteros, calcula su máximo común divisor
    y muestra el resultado.
    """
    print("Calculadora de Máximo Común Divisor (MCD)")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    mcd = calcular_mcd(num1, num2)
    print(f"El MCD de {num1} y {num2} es: {mcd}")


if __name__ == "__main__":
    main()
