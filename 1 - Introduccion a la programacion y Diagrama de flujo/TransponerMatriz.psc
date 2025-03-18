//Crear una matriz 2x3 y luego transponerla (convertir filas en columnas y viceversa).
Algoritmo TransponerMatriz
    Definir matriz, transpuesta, i, j Como Real
    Dimension matriz[2,3]
    Dimension transpuesta[3,2]
	
    // Asignamos valores a la matriz 2x3
    matriz[0,0] = 1
    matriz[0,1] = 2
    matriz[0,2] = 3
    matriz[1,0] = 4
    matriz[1,1] = 5
    matriz[1,2] = 6
	
    // Mostramos la matriz original
    Escribir "Matriz original (2x3):"
    Para i = 0 Hasta 1 Hacer
        Para j = 0 Hasta 2 Hacer
            Escribir Sin Saltar matriz[i,j], " "
        FinPara
        Escribir ""  // Salto de línea
    FinPara
	
    // Transponemos la matriz (convertimos filas en columnas)
    Para i = 0 Hasta 1 Hacer
        Para j = 0 Hasta 2 Hacer
            transpuesta[j,i] = matriz[i,j]
        FinPara
    FinPara
	
    // Mostramos la matriz transpuesta (3x2)
    Escribir "Matriz transpuesta (3x2):"
    Para i = 0 Hasta 2 Hacer
        Para j = 0 Hasta 1 Hacer
            Escribir Sin Saltar transpuesta[i,j], " "
        FinPara
        Escribir ""  // Salto de línea
    FinPara
FinAlgoritmo
