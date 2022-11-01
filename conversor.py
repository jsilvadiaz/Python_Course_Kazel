import os
os.system("cls")


def calculo_moneda(pesos, valor_dolar):
   pesos = input(pesos)
   pesos = float(pesos)
   dolares = pesos / valor_dolar
   dolares = round(dolares, 1)
   dolares = str(dolares)
   print("tienes $" + dolares +  " dolares")

menu = """
Bienvenido al conversor de monedas de Jorge Silva, selecciona el numero de la moneda que desees calcular 

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Chilenos
4- Pesos Mexicanos
5- Bolivares

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
   calculo_moneda(("Ingresa tu cantidad de pesos colombianos: "), 4174)
   
  

elif opcion == 2:
    calculo_moneda(("Ingresa  tu cantidad de pesos argentinos: "), 295)
   

elif opcion == 3:
    calculo_moneda(("Ingresa tu cantidad de pesos  chilenos : "), 920)

elif opcion == 4:
   calculo_moneda(("Ingresa tu cantidad de pesos  mexicanos : "), 24)

elif opcion == 5:
   calculo_moneda(("Ingresa tu cantidad de bolivares: "), 9)
else:
    print ("la opcion indicada no es valida")


# pesos = input("Ingresa tu cantidad de pesos argentinos: ")
# pesos = float(pesos)
# valor_dolar = 300
# dolares = pesos / valor_dolar
# dolares = round(dolares, 1)
# dolares = str(dolares)
# print("tienes $" + dolares +  " dolares")
