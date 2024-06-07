
# Escriba un programa recursivo y otro no recursivo para calcular la sucesion de Fibonacci

#VERSION RECURSIVA
def fibonacci_recursivo(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

try:
    n = int(input("Ingresa un numero entero: "))
    resultado_recursivo = fibonacci_recursivo(n)
    print(f"El valor de Fibonacci para n={n} (recursivo) es: {resultado_recursivo}")
except ValueError:
    print("Por favor, ingresa un numero válido.")

#VERSION NO RECURSIVA

def fibonacci_no_recursivo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

try:
    n = int(input("Ingresa un numero entero: "))
    resultado_no_recursivo = fibonacci_no_recursivo(n)
    print(f"El valor de Fibonacci para n={n} (no recursivo) es: {resultado_no_recursivo}")
except ValueError:
    print("Por favor, ingresa un numero válido.")

