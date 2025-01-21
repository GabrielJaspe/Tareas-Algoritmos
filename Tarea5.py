import random 

# Generador de cartas
def generar_cartas():
    palos = ["Corazones", "Diamantes", "Treboles", "Picas"]
    cartas = [f"{numero} de {palo}" for numero in range(1, 14) for palo in palos]
    return cartas 

# Barajar cartas 
def barajar_cartas(cartas):
    mazo_barajado = []
    while cartas:
        carta = random.choice(cartas)
        mazo_barajado.append(carta)
        cartas.remove(carta)
    return mazo_barajado

# Repartidor de cartas
def repartir_cartas(mazo_barajado):
    jugador_puntos = 0
    computadora_puntos = 0
    anterior_valor = None 

    while mazo_barajado:
        input("Presiona enter para sacar una carta")
        carta_actual = mazo_barajado.pop(0)
        print(f"Tu carta es: {carta_actual}")

        # Obtener valor de la carta 
        valor_actual = int(carta_actual.split()[0])

        if anterior_valor == valor_actual:
            respuesta = input("¡Cartas consecutivas iguales! Escribe 'batalla' o presiona Enter para continuar:").strip().lower()
            if respuesta == "batalla":
                print("Ganaste un punto")
                jugador_puntos += 1
            else:
                print("Ganó la computadora")
                computadora_puntos += 1

            anterior_valor = valor_actual

    # Resultado final
    print("\n--- Game over ---")
    print(f"Puntos del jugador: {jugador_puntos}")
    print(f"Puntos de la computadora: {computadora_puntos}")
    if jugador_puntos > computadora_puntos:
        print("¡Felicidades, ganaste!")
    elif jugador_puntos < computadora_puntos:
        print("¡Ganó la computadora suerte para la proxima!")
    else:
        print("¡Un empate!")

# Programa principal
def main():
    cartas = generar_cartas()
    mazo_barajado = barajar_cartas(cartas)
    repartir_cartas(mazo_barajado)

if __name__ == "__main__":
    main()