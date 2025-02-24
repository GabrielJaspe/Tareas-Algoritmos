import requests  # Importamos la librería para hacer solicitudes HTTP a la API de Pokémon

def obtener_datos_pokemon(nombre):
    """
    Obtiene información detallada de un Pokémon desde la API PokeAPI.

    Parámetro:
        nombre (str): Nombre del Pokémon ingresado por el usuario.

    Retorna:
        dict: Diccionario con la información del Pokémon (nombre, género, descripción, tipos, fortalezas y debilidades).
        None: Si el Pokémon no se encuentra en la API.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"  # Construimos la URL con el nombre del Pokémon en minúsculas
    response = requests.get(url)  # Realizamos la solicitud HTTP a la API

    if response.status_code == 200:  # Verificamos si la solicitud fue exitosa
        data = response.json()  # Convertimos la respuesta en un diccionario JSON
       
        # Extraemos el nombre del Pokémon y sus tipos
        nombre_pokemon = data["name"].capitalize()
        tipos = [t["type"]["name"].capitalize() for t in data["types"]]
       
        # Obtenemos la URL de la especie para extraer más información
        especie_url = data["species"]["url"]
        especie_response = requests.get(especie_url).json()

        # Determinamos el género según la tasa de género en la API
        genero = "desconocido"
        if especie_response["gender_rate"] == 1:
            genero = "femenino"
        elif especie_response["gender_rate"] == 0:
            genero = "masculino"
        else:
            genero = "ambos"

        # Extraemos la descripción en español del Pokémon
        descripcion = next(
            (entry["flavor_text"] for entry in especie_response["flavor_text_entries"]
             if entry["language"]["name"] == "es"), "Descripción no disponible."
        ).replace("\n", " ").replace("\f", " ")  # Eliminamos saltos de línea innecesarios
       
        # Listas para almacenar fortalezas y debilidades del Pokémon
        fortalezas = []
        debilidades = []

        # Obtenemos los tipos y sus relaciones de daño
        for tipo in data["types"]:
            tipo_url = tipo["type"]["url"]
            tipo_data = requests.get(tipo_url).json()
           
            # Extraemos fortalezas y debilidades en base a la relación de daño
            dobles_fortalezas = [d["name"].capitalize() for d in tipo_data["damage_relations"]["double_damage_to"]]
            dobles_debilidades = [d["name"].capitalize() for d in tipo_data["damage_relations"]["double_damage_from"]]
           
            # Agregamos los datos a las listas
            fortalezas.extend(dobles_fortalezas)
            debilidades.extend(dobles_debilidades)

        # Retornamos un diccionario con la información del Pokémon
        return {
            "nombre": nombre_pokemon,
            "genero": genero,
            "descripcion": descripcion,
            "tipos": tipos,
            "fuerte": list(set(fortalezas)),  # Eliminamos duplicados en fortalezas
            "debil": list(set(debilidades))   # Eliminamos duplicados en debilidades
        }
    else:
        print("Error: Pokémon no encontrado.")  # Mensaje de error si la API no encuentra el Pokémon
        return None

def guardar_en_archivo(datos):
    """
    Guarda la información del Pokémon en un archivo de texto 'pokedex.txt'.

    Parámetro:
        datos (dict): Diccionario con la información del Pokémon.

    Retorna:
        None
    """
    with open("pokedex.txt", "a", encoding="utf-8") as archivo:  # Abrimos el archivo en modo 'append' para no sobrescribir datos anteriores
        archivo.write(f"{datos['nombre']} el Pokémon {datos['genero']}.\n")  # Guardamos el nombre y género
        archivo.write(f"{datos['descripcion']}\n")  # Guardamos la descripción del Pokémon
        archivo.write(f"{datos['nombre']} es de tipo {', '.join(datos['tipos'])}, "
                      f"por lo que es fuerte contra {', '.join(datos['fuerte'])} "
                      f"y débil contra {', '.join(datos['debil'])}.\n")  # Guardamos los tipos, fortalezas y debilidades
        archivo.write("="*40 + "\n")  # Separador visual en el archivo

def main():
    """
    Función principal que solicita al usuario el nombre de un Pokémon,
    obtiene su información y la guarda en un archivo.

    Retorna:
        None
    """
    while True:  # Bucle infinito hasta que se obtenga un Pokémon válido
        nombre_pokemon = input("Introduce el nombre del Pokémon: ").strip()  # Pedimos al usuario que ingrese el nombre del Pokémon
        datos = obtener_datos_pokemon(nombre_pokemon)  # Obtenemos los datos del Pokémon

        if datos:  # Si el Pokémon se encontró en la API
            guardar_en_archivo(datos)  # Guardamos la información en 'pokedex.txt'
            print("Información guardada en 'pokedex.txt'.")
            break  # Salimos del bucle
        else:
            print("Inténtalo de nuevo.\n")  # Mensaje si el Pokémon no se encuentra en la API

# Verificamos que el script se ejecute directamente y no como módulo
if __name__ == "__main__":
    main()

