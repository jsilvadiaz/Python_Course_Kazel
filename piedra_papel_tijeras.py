import os
os.system("cls")


import random




menu = """
Bienvenido al juego virtual de piedra papel o tijeras: 

1- Piedra
2- Papel
3- tijeras

Elige una opcion: """

opcion = int(input(menu))





numero = random.randint(1, 3)

if opcion == 1 and numero == 1:
    print("la opcion de la maquina es " + str(numero))
    print("empate :) ")
elif opcion == 1 and numero ==  2:
    print("la opcion de la maquina es " + str(numero))
    print("Gana la computadora :) ")
elif opcion == 1 and numero ==  3:
    print("la opcion de la maquina es " + str(numero))
    print("Gana el usuario :) ")
elif opcion == 2 and numero ==  1:
    print("la opcion de la maquina es " + str(numero))
    print("Gana el usuario :) ")
elif opcion == 2 and numero ==  2:
    print("la opcion de la maquina es " + str(numero))
    print("empate :) ")
elif opcion == 2 and numero ==  3:
    print("la opcion de la maquina es " + str(numero))
    print("Gana la computadora :) ")
elif opcion == 3 and numero == 1:
    print("la opcion de la maquina es " + str(numero))
    print("Gana la computadora:) ")
elif opcion == 3 and numero == 2:
    print("la opcion de la maquina es " + str(numero))
    print("Gana el usuario:) ")
else:
    print("la opcion de la maquina es " + str(numero))
    print("empate")

    