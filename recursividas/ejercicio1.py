# sumaHasta(n) -> numero. Retorna la suma de los numeros desde el 0 hasta 
# el N. Por ejemplo. sumaHasta(5) = 5 + 4 + 3 + 2 + 1 + 0 => 15

def sumaHasta(n):
    return sum(range(n + 1))
resultado = sumaHasta(5)
print(f"La suma de los números desde 0 hasta 5 es: {resultado}")
