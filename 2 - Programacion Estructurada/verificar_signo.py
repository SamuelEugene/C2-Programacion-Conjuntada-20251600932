# Programa para determinar si un número es positivo, negativo o cero

# Solicita al usuario que ingrese un número
numero = float(input("Ingresa un número: "))

# Verifica si es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
