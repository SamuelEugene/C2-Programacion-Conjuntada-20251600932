# Programa para realizar operaciones básicas entre dos números

# Solicita al usuario que ingrese dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Realiza las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Verifica si el segundo número es distinto de cero antes de dividir
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "Indefinida (no se puede dividir por cero)"

# Muestra los resultados
print(f"\nResultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
