import math

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

def raiz_cuadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"

def potencia(a, b):
    return math.pow(a, b)

# Función principal para ejecutar la calculadora
def calculadora():
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raíz cuadrada")
    print("6. Potencia")
    
    # Solicita al usuario elegir una operación
    operacion = input("Selecciona la operación (1/2/3/4/5/6): ")

    # Solicita al usuario ingresar los números
    if operacion in ['1', '2', '3', '4', '6']:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
    
    elif operacion == '5':
        numero1 = float(input("Ingresa el número para calcular la raíz cuadrada: "))
    
    # Realiza la operación seleccionada
    if operacion == '1':
        print(f"El resultado de la suma es: {sumar(numero1, numero2)}")
    elif operacion == '2':
        print(f"El resultado de la resta es: {restar(numero1, numero2)}")
    elif operacion == '3':
        print(f"El resultado de la multiplicación es: {multiplicar(numero1, numero2)}")
    elif operacion == '4':
        print(f"El resultado de la división es: {dividir(numero1, numero2)}")
    elif operacion == '5':
        print(f"El resultado de la raíz cuadrada es: {raiz_cuadrada(numero1)}")
    elif operacion == '6':
        print(f"El resultado de {numero1} elevado a la potencia de {numero2} es: {potencia(numero1, numero2)}")
    else:
        print("Operación no válida")

# Ejecuta la calculadora
calculadora()
