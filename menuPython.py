import subprocess
import os
#!/usr/bin/python3

def SUMA():
    numSuma = int (input("Introduce un número para sumar: "))
    SUMA = numSuma + numero
    print(SUMA)

def RESTA():
    numResta = int (input("Introduce un número para restar: "))
    RESTA = numero - numResta 
    print(RESTA)

def MULTIPLICAR():
    numMult = int (input("Introduce un factor: "))
    MULTIPLICAR = numMult * numero
    print(MULTIPLICAR)

def DIVISION():
    numDiv = int (input("Introduce un divisor: "))
    if numDiv != 0:
        DIVISION = numDiv // numero
        print(DIVISION)
    else:
        print("No se puede dividir entre cero")

def LISTARDIRECTORIO():
    range = os.listdir(os.getcwd())
    lista =[]
    for archivo in range:
        lista.append(archivo)
    print(", ".join(lista))

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
                
                while eleccion != 6:
                    print ("¿Qué quieres hacer?: ")
                    print ("1. Introducir número")
                    print ("2. Sumar")
                    print ("3. Restar")
                    print ("4. Multiplicar")
                    print ("5. Dividir")
                    print ("6. Atrás")
                    eleccion = int (input(" "))

                    match eleccion:
                        case 1:
                            global numero
                            numero = int(input("Introduce un número: "))
                        case 2:
                            SUMA()
                            
                        case 3:
                            RESTA()
                           
                        case 4:
                            MULTIPLICAR()
                            
                        case 5:
                            DIVISION()
                            
                        case 6:
                            print("Volviendo")
                        case other:
                            print ("Opción no válida")
                            
                        
            case 2:
                
                while eleccion != 5:
                    print ("1. Cambiar de directorio")
                    print ("2. Listar directorio")
                    print ("3. Comprobar permisos de usuario sobre un archivo")
                    print ("4. Establecer permisos a un archivo")
                    print ("5. Atrás")
                    
                    eleccion = int(input(":"))

                    match eleccion:
                        case 1:
                            dir = input("Introduce el nombre del directorio al que te quieres cambiar")
                            os.chdir(dir)
                            print("Ahora estás en:"+os.getcwd())
                            
                        case 2:
                            LISTARDIRECTORIO()
                            
                        case 3:
                            LISTARDIRECTORIO()
                            arch = input ("¿De qué archivo quieres comprobar los permisos?")
                            print("Tienes permisos de:")
                            if os.access(arch, os.R_OK):
                                print ("    Lectura")
                            if os.access(arch, os.W_OK):
                                print ("    Escritura")
                            if os.access(arch, os.X_OK):
                                print ("    Ejecución")
                        case 4:
                            LISTARDIRECTORIO()
                        case 5:
                            print ("Volviendo")
                            
                        case other:
                            print ("Opción no válida")
                    
if __name__ == "__main__":
    main()