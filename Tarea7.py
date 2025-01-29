import random

# Funciones de ataques compartidos
def tacleada():
    return (5, -10)  # (defensa, daño)

def ataque_rapido():
    return (-5, -25)

# Funciones de ataques de Pikachu
def impactrueno():
    return (0, -20)

def onda_trueno():
    return (10, -15)

# Funciones de ataques de Charmander
def lanzallamas():
    return (-5, -25)

def ascuas():
    return (0, -20)

# Diccionario que mapea nombres de ataques a funciones
ataques = {
    "Tacleada": tacleada,
    "Ataque Rápido": ataque_rapido,
    "Impactrueno": impactrueno,
    "Onda Trueno": onda_trueno,
    "Lanzallamas": lanzallamas,
    "Ascuas": ascuas
}

# Definición de los Pokémon con sus ataques disponibles
pokemon_data = {
    "jugador": {
        "nombre": "Pikachu",
        "stats": (100, 0),  # (salud, defensa)
        "ataques": ["Impactrueno", "Onda Trueno", "Tacleada", "Ataque Rápido"]
    },
    "computadora": {
        "nombre": "Charmander",
        "stats": (100, 0),  # (salud, defensa)
        "ataques": ["Lanzallamas", "Ascuas", "Tacleada", "Ataque Rápido"]
    }
}

def mostrar_estado(jugador_stats, computadora_stats):
    """Muestra el estado actual de los Pokémon"""
    print(f"\nPikachu: {jugador_stats[0]} HP, {jugador_stats[1]} DEF")
    print(f"Charmander: {computadora_stats[0]} HP, {computadora_stats[1]} DEF")

def mostrar_ataques(ataques_disponibles):
    """Muestra los ataques disponibles"""
    print("\nAtaques disponibles:")
    for i, ataque in enumerate(ataques_disponibles, 1):
        print(f"{i}. {ataque}")

def seleccionar_ataque_jugador(ataques_disponibles):
    """Permite al jugador seleccionar un ataque"""
    while True:
        mostrar_ataques(ataques_disponibles)
        try:
            seleccion = int(input("\nElige un ataque (número): ")) - 1
            if 0 <= seleccion < len(ataques_disponibles):
                return ataques_disponibles[seleccion]
        except ValueError:
            pass
        print("Selección inválida. Intenta de nuevo.")

def seleccionar_ataque_computadora(ataques_disponibles):
    """Selecciona un ataque aleatorio para la computadora"""
    return random.choice(ataques_disponibles)

def aplicar_ataque(atacante_nombre, defensor_nombre, ataque_nombre, atacante_stats, defensor_stats):
    """Aplica el ataque y retorna las nuevas tuplas de stats"""
    # Obtener la función del ataque y ejecutarla
    funcion_ataque = ataques[ataque_nombre]
    cambios = funcion_ataque()
    
    # Extraer componentes de las tuplas
    salud_atacante, defensa_atacante = atacante_stats
    salud_defensor, defensa_defensor = defensor_stats
    
    # Aplicar cambios
    nueva_defensa_atacante = defensa_atacante + cambios[0]
    nueva_salud_defensor = salud_defensor + cambios[1]
    
    print(f"\n{atacante_nombre} usa {ataque_nombre}!")
    if cambios[0] > 0:
        print(f"{atacante_nombre} aumenta su defensa!")
    elif cambios[0] < 0:
        print(f"{atacante_nombre} reduce su defensa!")
    
    # Retornar nuevas tuplas de stats
    return (salud_atacante, nueva_defensa_atacante), (nueva_salud_defensor, defensa_defensor)

def batalla():
    """Función principal del juego"""
    print("¡Comienza la batalla Pokémon!")
    print(f"\n{pokemon_data['jugador']['nombre']} vs {pokemon_data['computadora']['nombre']}")
    
    jugador_stats = pokemon_data["jugador"]["stats"]
    computadora_stats = pokemon_data["computadora"]["stats"]
    
    while True:
        mostrar_estado(jugador_stats, computadora_stats)
        
        # Turno del jugador
        ataque_jugador = seleccionar_ataque_jugador(pokemon_data["jugador"]["ataques"])
        jugador_stats, computadora_stats = aplicar_ataque(
            pokemon_data["jugador"]["nombre"],
            pokemon_data["computadora"]["nombre"],
            ataque_jugador,
            jugador_stats,
            computadora_stats
        )
        
        if computadora_stats[0] <= 0:
            print(f"\n¡{pokemon_data['computadora']['nombre']} se debilitó!")
            print(f"\n¡{pokemon_data['jugador']['nombre']} es el ganador!")
            break
            
        # Turno de la computadora
        ataque_computadora = seleccionar_ataque_computadora(pokemon_data["computadora"]["ataques"])
        computadora_stats, jugador_stats = aplicar_ataque(
            pokemon_data["computadora"]["nombre"],
            pokemon_data["jugador"]["nombre"],
            ataque_computadora,
            computadora_stats,
            jugador_stats
        )
        
        if jugador_stats[0] <= 0:
            print(f"\n¡{pokemon_data['jugador']['nombre']} se debilitó!")
            print(f"\n¡{pokemon_data['computadora']['nombre']} es el ganador!")
            break

if __name__ == "__main__":
    batalla()
