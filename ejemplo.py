#número aleatorio
import sys
import random
numero = random(0,100)
sys.exit()

#pida al usuario que introduzca un número (en una variable llamada intento)

while True:
# Se entra en un bucle infinito

    # Se pide introducir un número
    intento = input("Introduzca un número entre 1 y 99: ")
    try:
        intento = int(intento)
    except:
        pass
    else:
        # Realizar la comparación
        if 1 <= intento <= 99:
            # Tenemos lo que queremos, de modo que salimos del bucle
            break
print(intento)
