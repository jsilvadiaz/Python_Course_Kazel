import os
os.system("cls")

import random

numero = random.randint(1, 100)
intentos = 5

while(intentos > 0):
    eleccion = int(input("elige el numero "))    
    if eleccion > numero:
        print(" El numero es mas pequeño")
        intentos = intentos -1
    elif eleccion < numero:
        print("El numero es mas grande")
        intentos = intentos -1
    else:
        print("Ganaste")
        break

print("Se acabaron los intentos")