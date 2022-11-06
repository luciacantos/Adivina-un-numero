import sys
import random
numero = random.randint(0,100)
sys.exit()

While True:
    numero = input("Intruduzca un número entre 1 y 99: ")
    try: 
        numero = int(numero)
    except:
        pass
    else:
        if 0 < numero < 100:
            break

print(intento)

