# Un robot puede dar pasos de 1 o 2 metros. Escriba un programa para numerar
# todas las maneras en que el robot camina n metros.

def contar_caminos_recursivo(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return contar_caminos_recursivo(n - 1) + contar_caminos_recursivo(n - 2)

try:
    metros = int(input("Ingresa el numero de metros: "))
    maneras = contar_caminos_recursivo(metros)
    print(f"El robot puede caminar {maneras} maneras diferentes.")
except ValueError:
    print("Por favor, ingresa un número válido.")
