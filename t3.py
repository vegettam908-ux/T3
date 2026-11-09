import math
import random


def generar_punto(a, b):
    x = random.uniform(-a, a)
    y = random.uniform(-b, b)
    return x, y


def esta_en_elipse(x, y, a, b):
    return (x / a) ** 2 + (y / b) ** 2 <= 1


def esta_en_hiperbola(x, y, c, d):
    return (x / c) ** 2 - (y / d) ** 2 >= 1


def pedir_positivo(texto):
    while True:
        try:
            numero = float(input(texto))
            if math.isfinite(numero) and numero > 0:
                return numero
            print("Ingresa un número positivo y finito.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")


def pedir_cantidad(texto):
    while True:
        try:
            numero = int(input(texto))
            if numero > 0:
                return numero
            print("Ingresa un entero mayor que cero.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")


def main():
    print("=== CÁLCULO DEL ÁREA POR MONTE CARLO ===")

    a = pedir_positivo("Valor de a para la elipse: ")
    b = pedir_positivo("Valor de b para la elipse: ")
    c = pedir_positivo("Valor de c para la hipérbola: ")
    d = pedir_positivo("Valor de d para la hipérbola: ")
    cantidad = pedir_cantidad("Cantidad de puntos aleatorios: ")

    dentro_elipse = 0
    dentro_interseccion = 0

    for _ in range(cantidad):
        x, y = generar_punto(a, b)

        if esta_en_elipse(x, y, a, b):
            dentro_elipse += 1

            if esta_en_hiperbola(x, y, c, d):
                dentro_interseccion += 1

    area_elipse = math.pi * a * b

    print("\n=== RESULTADOS ===")
    print(f"Puntos generados: {cantidad}")
    print(f"Puntos dentro de la elipse: {dentro_elipse}")
    print(f"Puntos en la intersección: {dentro_interseccion}")
    print(f"Área de la elipse: {area_elipse:.4f}")

    if dentro_elipse == 0:
        print("Ningún punto cayó en la elipse. Intenta con más puntos.")
        return

    proporcion = dentro_interseccion / dentro_elipse
    area_interseccion = area_elipse * proporcion

    print(f"Proporción de intersección: {proporcion:.4f}")
    print(f"Área aproximada de la intersección: {area_interseccion:.4f}")


if __name__ == "__main__":
    main()