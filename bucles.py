



# contador = 0
# print("2 elevado a " + str(contador) + " es igual a "+ str(2**contador))

# contador = 1
# print("2 elevado a " + str(contador) + " es igual a "+ str(2**contador))

# contador = 2
# print("2 elevado a " + str(contador) + " es igual a "+ str(2**contador))

# contador = 3
# print("2 elevado a " + str(contador) + " es igual a "+ str(2**contador))

# contador = 4
# print("2 elevado a " + str(contador) + " es igual a "+ str(2**contador))

# contador = 5
# print("2 elevado a " + str(contador) + " es igual a "+ str(2**contador))

def run():
    LIMITE = 300000

    contador = 0
    potencia_3 = 3**contador
    while potencia_3 < LIMITE:
        print("3 elevado a "+ str(contador) + " es igual a " + str(potencia_3))
        contador = contador + 1
        potencia_3 = 3**contador



if __name__ == "__main__":
    run()
