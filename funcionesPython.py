
import subprocess
import os
#!/usr/bin/python3


def LISTARDIRECTORIO():
    range = os.listdir(os.getcwd())
    lista =[]
    for archivo in range:
        lista.append(archivo)
    print(", ".join(lista))

def prueba():
    LISTARDIRECTORIO()
    arch = input ("¿De qué archivo quieres comprobar los permisos?")
    print("Tienes permisos de:")
    if os.access(arch, os.R_OK):
        print ("    Lectura")
    if os.access(arch, os.W_OK):
        print ("    Escritura")
    if os.access(arch, os.X_OK):
        print ("    Ejecución")

def prueba2():
    arch = input ("¿De qué archivo quieres cambiar los permisos?")
    de = input ("De quién quieres modificar los permisos: usuario, grupo, otros")
    permiso = input ("Qúe permiso quieres cambiar: lectura, escritura, ejecución")
    accion = input(f"¿Quieres añadir o quitar el permiso de{permiso}")
    permisos=["lectura","escritura", "ejecución"]
    accion = input(f"¿Quieres otorgar o quitar el permiso de {permiso}")
                  

def main ():
    print("Ahora estás en:"+os.getcwd())
    os.chmod("/home/ladmin/Sistemas_Informaticos/README.md", mode=777)

if __name__ == "__main__":
    main()
    