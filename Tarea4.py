# Función para verificar si un año es bisiesto
# Un año es bisiesto si es divisible entre 4, pero no entre 100, excepto si es divisible entre 400
def es_bisiesto(anio): 
    return (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0))

# Funcion para años bisiestos con ciclos
def contar_bisiestos_con_ciclo(anio):
# Validamos que el año ingresado este dentro del rango
    if anio < 1900 or anio > 2199:
        return "el rango del año debe ser entre 1900 y 2199"

    bisiestos = 0 # La variable utilizada para contar los años bisiestos
    # Iteramos desde 1900 hasta el año ingresado
    for i in range(1900, anio + 1): 
        if es_bisiesto(i): # Verificamos si el año es bisiesto
            bisiestos += 1 # Incrementamos si el año es bisiesto
    return bisiestos
        
# Funcion para años bisiestos sin ciclos
def contar_bisiestos_sin_ciclos(anio): 
# Validamos que el año ingresado este dentro del rango
  if anio < 1900 or anio > 2199:
     return "el año debe estar entre 1900 y 2199"

# Calculadora para años bisiestos usando operaciones matematicas
  total_anios = anio - 1900 + 1 # Total de años desde 1900 hasta el año ingresado
  bisiestos_div_4 = total_anios // 4 # Años bisiestos divisibles entre 4
  no_bisiestos_div_100 = (anio // 100) - (1900 // 100) # Años divisibles entre 100
  bisiestos_div_400 = (anio // 400) - (1900 // 400) # Años divisibles entre 400

# Ajustes de conteo restando los años no bisiestos y agregando los divisibles entre 400
  return bisiestos_div_4 - no_bisiestos_div_100 + bisiestos_div_400

# Funcion principal 
def main():
    print("Calculo de años bisiestos entre 1900 y el año ingresado")

    # Solicitamos el año al usuario
    anio_entrada = int(input("Ingrese un año entre 1900 y 2199: "))

    # Menu para que el usuario elija que metodo quiere utilizar
    print("\nElije el metodo a usar:")
    print("1. Con ciclos")
    print("2. Sin ciclos")

    # Recibimos el metodo seleccionado
    opcion = input("Ingresa el numero de tu eleccion:")
    
    # Segun la opcion, llamamos a la funcion correspondiente
    if opcion == "1":
        resultado = contar_bisiestos_con_ciclo(anio_entrada)
    elif opcion == "2":
        resultado = contar_bisiestos_sin_ciclos(anio_entrada)
    else:
        # Si la opcion es invalida, mostramos un mensaje de error
        print("Opcion invalida")
        return

    # Mostramos el resultado
    if isinstance(resultado, str):
        print(resultado)  # Mensaje de error
    else:
        print(f"\nNúmero de años bisiestos entre 1900 y {anio_entrada}: {resultado}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()