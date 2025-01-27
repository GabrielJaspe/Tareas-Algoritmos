import random

# Definición de ataques compartidos y específicos
ataques_compartidos = {
    "Tacleada": {"daño": 10, "defensa": 5},
    "Ataque Rápido": {"daño": 25, "defensa": -5}
}

# Definición de los Pokémon y sus ataques
pokemon_data = {
    "jugador": {
        "nombre": "Pikachu",
        "salud": 100,
        "ataques": {
            "Impactrueno": {"daño": 20, "defensa": 0},
            "Onda Trueno": {"daño": 15, "defensa": 10},
            **ataques_compartidos  # Agrega los ataques compartidos
        }
    },
    "computadora": {
        "nombre": "Charmander",
        "salud": 100,
        "ataques": {
            "Lanzallamas": {"daño": 25, "defensa": -5},
            "Ascuas": {"daño": 20, "defensa": 0},
            **ataques_compartidos  # Agrega los ataques compartidos
        }
    }
}

def mostrar_estado(pokemon_data):
    """Muestra el estado actual de los Pokémon"""
    print(f"\n{pokemon_data['jugador']['nombre']}: {pokemon_data['jugador']['salud']} HP")
    print(f"{pokemon_data['computadora']['nombre']}: {pokemon_data['computadora']['salud']} HP")

def mostrar_ataques(ataques):
    """Muestra los ataques disponibles"""
    print("\nAtaques disponibles:")
    for i, ataque in enumerate(ataques.keys(), 1):
        print(f"{i}. {ataque}")

def seleccionar_ataque_jugador(ataques):
    """Permite al jugador seleccionar un ataque"""
    while True:
        mostrar_ataques(ataques)
        try:
            seleccion = int(input("\nElige un ataque (número): ")) - 1
            if 0 <= seleccion < len(ataques):
                return list(ataques.keys())[seleccion]
        except ValueError:
            pass
        print("Selección inválida. Intenta de nuevo.")

def seleccionar_ataque_computadora(ataques):
    """Selecciona un ataque aleatorio para la computadora"""
    return random.choice(list(ataques.keys()))

def aplicar_ataque(atacante, defensor, ataque_nombre, ataque_info):
    """Aplica el daño y los efectos de defensa del ataque"""
    defensor["salud"] -= ataque_info["daño"]
    if ataque_info["defensa"] != 0:
        atacante["salud"] += ataque_info["defensa"]
    print(f"\n{atacante['nombre']} usa {ataque_nombre}!")
    if ataque_info["defensa"] > 0:
        print(f"{atacante['nombre']} aumenta su defensa!")
    elif ataque_info["defensa"] < 0:
        print(f"{atacante['nombre']} reduce su defensa!")

def batalla():
    """Función principal del juego"""
    print("¡Comienza la batalla Pokémon!")
    print(f"\n{pokemon_data['jugador']['nombre']} vs {pokemon_data['computadora']['nombre']}")
    
    while True:
        mostrar_estado(pokemon_data)
        
        # Turno del jugador
        ataque_jugador = seleccionar_ataque_jugador(pokemon_data["jugador"]["ataques"])
        aplicar_ataque(
            pokemon_data["jugador"],
            pokemon_data["computadora"],
            ataque_jugador,
            pokemon_data["jugador"]["ataques"][ataque_jugador]
        )
        
        if pokemon_data["computadora"]["salud"] <= 0:
            print(f"\n¡{pokemon_data['computadora']['nombre']} se debilitó!")
            print(f"\n¡{pokemon_data['jugador']['nombre']} es el ganador!")
            break
            
        # Turno de la computadora
        ataque_computadora = seleccionar_ataque_computadora(pokemon_data["computadora"]["ataques"])
        aplicar_ataque(
            pokemon_data["computadora"],
            pokemon_data["jugador"],
            ataque_computadora,
            pokemon_data["computadora"]["ataques"][ataque_computadora]
        )
        
        if pokemon_data["jugador"]["salud"] <= 0:
            print(f"\n¡{pokemon_data['jugador']['nombre']} se debilitó!")
            print(f"\n¡{pokemon_data['computadora']['nombre']} es el ganador!")
            break

if __name__ == "__main__":
    batalla()
