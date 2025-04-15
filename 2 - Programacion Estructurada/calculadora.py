# Funciones para las operaciones matemáticas

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"

# Función principal para ejecutar la calculadora
def calculadora():
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    # Solicita al usuario elegir una operación
    operacion = input("Selecciona la operación (1/2/3/4): ")

    # Solicita al usuario ingresar dos números
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))

    # Realiza la operación seleccionada
    if operacion == '1':
        print(f"El resultado de la suma es: {sumar(numero1, numero2)}")
    elif operacion == '2':
        print(f"El resultado de la resta es: {restar(numero1, numero2)}")
    elif operacion == '3':
        print(f"El resultado de la multiplicación es: {multiplicar(numero1, numero2)}")
    elif operacion == '4':
        print(f"El resultado de la división es: {dividir(numero1, numero2)}")
    else:
        print("Operación no válida")

# Ejecuta la calculadora
calculadora()
