# Programar un algoritmo recursivo que determine
# si un número es impar utilizando recursividad cruzada.
def impar(n):
    if n == 0:
        return False
    else:
        return par(n - 1)

def par(n):
    if n == 0:
        return True
    else:
        return impar(n - 1)

try:
    numero = int(input("Ingresa un numero: "))
    if impar(numero):
        print(f"{numero} es impar.")
    else:
        print(f"{numero} es par.")
except ValueError:
    print("Por favor, ingresa oto numero.")


