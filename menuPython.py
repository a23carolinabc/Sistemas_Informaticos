import subprocess
import os
#!/usr/bin/python3
def clear():
    temp = subprocess.Popen(clear, stdout = subprocess.PIPE)
def SUMA():
    numSuma = int (input("Introduce un número para sumar"))
    SUMA = numSuma + numero
    print(SUMA)

def RESTA():
    numResta = int (input("Introduce un número para restar"))
    RESTA = numResta + numero
    print(RESTA)

def MULTIPLICAR():
    numMult = int (input("Introduce un factor"))
    MULTIPLICAR = numMult + numero
    print(MULTIPLICAR)

def DIVISION():
    numDiv = int (input("Introduce un divisor"))
    DIVISION = numDiv + numero
    print(DIVISION)

def main():
    opcion = 0
    eleccion = 0
    while opcion != 3:
        print ("MENÚ"),
        print ("¿Qué quieres hacer?: "),
        print ("1. Usar la calculadora"),
        print ("2. Comprobar funciones"),
        print ("3. Salir")

        opcion = int (input(":"))

        match opcion:
            case 1:
                clear()
                while eleccion != 6:
                    print ("¿Qué quieres hacer?: ")
                    print ("1. Introducir número")
                    print ("2. Sumar")
                    print ("3. Restar")
                    print ("4. Multiplicar")
                    print ("5. Dividir")
                    print ("6. Atrás")
                    eleccion = int (input(":"))

                    match eleccion:
                        case 1:
                            global numero
                            numero = int(input("Introduce un número: "))
                        case 2:
                            SUMA()
                            clear()
                        case 3:
                            RESTA()
                            clear()
                        case 4:
                            MULTIPLICAR()
                            clear()
                        case 5:
                            DIVISION()
                            clear()
                        case 6:
                            clear()
                        case other:
                            print ("Opción no válida")
                            clear()
                        
            case 2:
                clear()
                while eleccion != 5:
                    print ("1. Comprobar función SUMA")
                    print ("2. Comprobar función RESTA")
                    print ("3. Comprobar función MULTIPLICAR")
                    print ("4. Comprobar función DIVISION")
                    print ("5. Atrás")
                    
                    eleccion = int(input(":"))

                    match eleccion:
                        case 1:
                            print(SUMA())
                            clear()
                        case 2:
                            print(RESTA())
                            clear()
                        case 3:
                            print(MULTIPLICAR())
                            clear()
                        case 4:
                            print(DIVISION())
                            clear()
                        case 5:
                            clear
                        case other:
                            print ("Opción no válida")
                            clear()
                    
