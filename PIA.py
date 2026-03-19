import numpy as np
import math

# Método: Eliminación Gaussiana
def eliminacion_gaussiana_simple():
    n = int(input("Ingrese el número de ecuaciones (n): "))
    A = np.zeros((n, n+1))
    
    print("Ingrese los coeficientes del sistema de ecuaciones (incluyendo el término independiente) separados por espacios:")
    for i in range(n):
        A[i] = list(map(float, input(f"Ecuación {i+1}: ").split()))
    
    def print_matriz(A):
        print("\nMatriz:")
        for row in range(n):
            ecuacion = " + ".join(f"{A[row, col]:.6f}x{col+1}" for col in range(n))
            print(f"{ecuacion} = {A[row, n]:.6f}")
    
    print_matriz(A)
    
    for i in range(n):
        A[i] = A[i] / A[i, i]
        for j in range(i+1, n):
            A[j] = A[j] - A[i] * A[j, i]
        print_matriz(A)
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = round(A[i, n] - sum(A[i, j] * x[j] for j in range(i+1, n)), 6)
    
    print("\nSolución del sistema:")
    for i in range(n):
        print(f"x{i+1} = {x[i]}")

# Método: Bisección
def f(x, func):
    return eval(func, {
        "x": x,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "exp": math.exp,
        "cot": lambda x: 1 / math.tan(x) if math.tan(x) != 0 else float('inf'),
        "sec": lambda x: 1 / math.cos(x) if math.cos(x) != 0 else float('inf'),
        "csc": lambda x: 1 / math.sin(x) if math.sin(x) != 0 else float('inf')
    })

def biseccion(func, x1, xu, error_tolerance):
    if f(x1, func) * f(xu, func) > 0:
        print("Error: No hay una raíz en el intervalo dado. Intente con otro intervalo.")
        return None
    
    xr_old = 0
    error = float("inf")
    iter_count = 0
    
    while error > error_tolerance:
        xr = (x1 + xu) / 2
        f_x1 = f(x1, func)
        f_xr = f(xr, func)
        
        if f_x1 * f_xr < 0:
            xu = xr
        else:
            x1 = xr
        
        if iter_count >= 1:
            error = abs((xr - xr_old) / xr) * 100
        
        print(f"Iteración {iter_count + 1}: xr = {xr}, Error = {error:.3f}%")
        
        xr_old = xr
        iter_count += 1
    
    return xr

# Método: Diferencias Divididas
def dif_divididas(x, y):
    n = len(y)
    coef = np.array(y, dtype=float)
    
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    
    return coef

def polinomio_newton(x, coef, val):
    n = len(coef)
    resultado = coef[0]
    producto = 1.0
    
    for i in range(1, n):
        producto *= (val - x[i - 1])
        resultado += coef[i] * producto
    
    return resultado

# PIA
def main():
    print("Seleccione el método a ejecutar:")
    print("1. Eliminación Gaussiana")
    print("2. Bisección")
    print("3. Diferencias Divididas")
    
    opcion = input("Ingrese una opción (1/2/3): ")

    if opcion == "1":
        eliminacion_gaussiana_simple()
    elif opcion == "2":
        func = input("Ingrese la función f(x): ")
        x1 = float(input("Ingrese el valor inicial x1: "))
        xu = float(input("Ingrese el valor inicial xu: "))
        error_tolerance = float(input("Ingrese el error menor esperado en %: "))
        raiz = biseccion(func, x1, xu, error_tolerance)
        if raiz is not None:
            print(f"La raíz aproximada encontrada es: {raiz}")
    elif opcion == "3":
        tamano = int(input("Ingrese la cantidad de valores: "))
        x = np.zeros(tamano)
        y = np.zeros(tamano)

        for i in range(tamano):
            x[i] = float(input(f"Ingrese el valor de x[{i}]: "))
            y[i] = float(input(f"Ingrese el valor de y[{i}]: "))

        coeficientes = dif_divididas(x, y)
        valor_evaluar = float(input("Ingrese el valor de x a evaluar: "))
        resultado = polinomio_newton(x, coeficientes, valor_evaluar)
        print(f"\ny({valor_evaluar}): {resultado}")
    else:
        print("Opción no válida.")

main()
