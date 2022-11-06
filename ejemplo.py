# Adivina un número entre 0 y 99 (incluidos) generando un número al azar

import random
numero = random.randint(-1,100)

while True:
    while True:
        intento = input("Introduzca un número entre 0 y 99: ")
        try:
            intento = int(intento)
        except:
            pass
        else:
            if -1 < intento < 100:
                break
    if intento > numero:
        print("Demasiado grande")
    elif intento < numero:
        print("Demasiado pequeño")
    else:
        print("Ha ganado")
        break



