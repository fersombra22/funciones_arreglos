# Implemente un programa recursivo que sume dos números a + b. Considera que
# la suma a+b = a + 1 + 1 + …+ 1 (b veces)

def suma_recursiva(a, b):
    if b == 0:
        return a
    else:
        return suma_recursiva(a + 1, b - 1)

# Ejemplo de uso:
a = int(input("Ingresa el primer numero (a): "))
b = int(input("Ingresa el segundo numero (b): "))
resultado = suma_recursiva(a, b)
print(f"La suma de {a} + {b} es: {resultado}")
