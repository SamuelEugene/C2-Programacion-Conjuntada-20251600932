# Programa que suma números ingresados por el usuario hasta que ingrese 0

suma_total = 0

while True:
    numero = float(input("Ingresa un número (0 para terminar): "))
    
    if numero == 0:
        break
    
    suma_total += numero

print(f"\nLa suma total es: {suma_total}")
