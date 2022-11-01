import os
os.system("cls")

menu = """
Bienvenido al programa que te permite calcular cuantas barajitas te faltan:

Indica cuantas barajitas tienes pegadas?: """

cantidad = int(input(menu))


    

def run():


  figuritas_restantes = 670 - cantidad
  

  if figuritas_restantes == 0:
    print("TERMINASTE EL ALBUM!!!!!!")

  elif figuritas_restantes == 670:
    print(" comienza la aventura")

  elif figuritas_restantes < 0:
    print ( "No debes comprar mas barajita")

  elif figuritas_restantes >= 1 <=670:
    
    figuritas_restantes = 670 - cantidad
    print("te faltan" + str(figuritas_restantes) +  " {barajitas}")

  elif cantidad >= 670:
    print ( "No debes comprar mas barajita")

  


  
if __name__ == '__main__':
     run()
 