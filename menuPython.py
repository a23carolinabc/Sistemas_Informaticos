#!/usr/bin/python3
def primo():
    num = int (input("Introduce un entero"))
    flag = 0
    while flag >= 0:
        for i in range (2, num, 1):
            if (num%i == 0):
                flag = 1
                print ("No es primo")
            if (flag == 0):
                flag = -1
                print ("Es primo")

if __name__ == "__main__":
