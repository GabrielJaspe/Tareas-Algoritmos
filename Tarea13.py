def fibonacci(n):
    # Caso base: si n es 0 o 1, devuelve n
    if n <= 1:
        return n
    # Llamadas recursivas para calcular el valor de Fibonacci
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    # Bienvenida al usuario
    print("Bienvenido al programa de cálculo de números Fibonacci.")
    print("Este programa calcula el n-ésimo número de Fibonacci de forma recursiva.")
    
    # Solicitar al usuario un número n
    while True:
        try:
            n = int(input("Introduce un número entero no negativo: "))
            if n < 0:
                raise ValueError("El número debe ser no negativo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, intenta de nuevo.")
    
    # Calcular el n-ésimo número de Fibonacci
    resultado = fibonacci(n)
    
    # Mostrar el resultado
    print(f"El número Fibonacci en la posición {n} es {resultado}.\n")
    
    # Información adicional sobre la secuencia de Fibonacci
    print("La secuencia de Fibonacci es una serie de números en la que cada número es la suma de los dos anteriores.")
    print("Por ejemplo, los primeros números de la secuencia son: 0, 1, 1, 2, 3, 5, 8, 13, ...")
    print("Esta secuencia tiene aplicaciones en matemáticas, computación y la naturaleza.\n")
    
    # Despedida
    print("Gracias por usar el programa. ¡Que tengas un buen día!")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()

