import sys
import random
numero = random.randint(0,100)
sys.exit()

while True:
    while True:
        intento = input("Introduzca un número entre 0 y 99:")

        try:
            intento = int(intento)
        except:
            pass
        else:
            if 0 <= intento <= 99:
                break
    if intento > numero:
        print("Demasiado grande")
    elif intento < numero:
        print("Demasiado pequeño")
    else:
        print("Ha ganado")
        break
