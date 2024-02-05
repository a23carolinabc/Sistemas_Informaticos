import subprocess
import os
#!/usr/bin/python3

def SUMA(numero):
    numSuma = int (input("Introduce un número para sumar: "))
    SUMA = numSuma + numero
    print(SUMA)

def RESTA(numero):
    numResta = int (input("Introduce un número para restar: "))
    RESTA = numero - numResta 
    print(RESTA)

def MULTIPLICAR(numero):
    numMult = int (input("Introduce un factor: "))
    MULTIPLICAR = numMult * numero
    print(MULTIPLICAR)

def DIVISION(numero):
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
        print ("2. Archivos"),
        print ("3. Salir")

        opcion = int (input(" "))
        os.system('clear')
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
                            os.system('clear')
                            numero = int(input("Introduce un número: "))
                        case 2:
                            os.system('clear')
                            SUMA(numero)
                        case 3:
                            os.system('clear')
                            RESTA(numero)
                        case 4:
                            os.system('clear')
                            MULTIPLICAR(numero)
                            
                        case 5:
                            os.system('clear')
                            DIVISION(numero)                            
                        case 6:                            
                            print("Volviendo")
                            os.system('clear')
                        case other:
                            print ("Opción no válida")
                            os.system('clear')
                            
                        
            case 2:
                
                while eleccion != 6:
                    print ("1. Cambiar de directorio")
                    print ("2. Listar directorio actual")
                    print ("3. Comprobar permisos de usuario sobre un archivo")
                    print ("4. Comprobar permisos de usuario sobre un archivo")
                    print ("5. Establecer permisos a un archivo")
                    print ("6. Atrás")
                    
                    eleccion = int(input(":"))

                    match eleccion:
                        case 1:
                            os.system('clear')
                            dir = input("Introduce el nombre del directorio al que te quieres cambiar. Para ir hacia atrás introduzca ..")
                            os.chdir(dir)
                            print("Ahora estás en:"+os.getcwd())
                            
                        case 2:
                            os.system('clear')
                            LISTARDIRECTORIO()
                        
                        case 3: 
                        case 4:
                            os.system('clear')
                            LISTARDIRECTORIO()
                            arch = input ("¿De qué archivo quieres comprobar los permisos?")
                            print("Tienes permisos de:")
                            if os.access(arch, os.R_OK) is True:
                                print ("    Lectura")
                            elif os.access(arch, os.W_OK) is True:
                                print ("    Escritura")
                            elif os.access(arch, os.X_OK) is True:
                                print ("    Ejecución")
                            else:
                                print("No tienes permisos sobre este archivo")
                        case 5:
                            LISTARDIRECTORIO()
                        case 6:
                            print ("Volviendo")
                            
                        case other:
                            print ("Opción no válida")
                    
if __name__ == "__main__":
    main()