import sys
import random
numero = random.randint(0,100)
sys.exit()

intento = input("Introduzca un número entre 1 y 99: ")
try:
    intento = int(intento)
except:
    numero = 0
while not 0 < intento <100:
    intento = input("Introduzca un número entre 1 y 99: ")
    try:
        intento = int(intento)
    except:
        intento = 0
    break
print(intento)
