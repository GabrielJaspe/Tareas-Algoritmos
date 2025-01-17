def crear_perfil():
    # Pedir nombre y validar mayuscula 
    nombre = input("Ingrese su nombre: ")
    if not nombre or not nombre [0].isupper():
        print("El nombre no puede estar vacío y debe empezar con mayúscula")
        return
    
    # Pedir sexo
    sexo = input("Ingrese su sexo (M/F): ").upper()
    if sexo not in ["M", "F"]:
        print("El sexo debe ser M o F")
        return
    
    # Pedir region 
    print("\nPaises disponibles: ")
    print("1. España")
    print("2. México")
    print("3. Argentina")

    pais = input("Ingrese su pais o region (1-3): ") 
    if pais not in ["1", "2", "3"]:
        print("Error: Pais no valido")
        return
    
    # Definir opciones segun pais
    opciones = {
        "1": ["Paella", "Jamón ibérico", "Tortilla de patatas"],
        "2": ["Tacos", "Tequila", "Enchiladas"],
        "3": ["Asado", "Mate", "Empanadas"],
    }

    # Mostrar cosas favoritas de la region o pais 
    print(f"\nCosas favoritas del pais: ")
    for i, cosa in enumerate(opciones[pais], 1):
        print(f"{i}. {cosa}")

        favorito = input("Elija su opcion favorita (1-3): ")
        if favorito not in ["1", "2", "3"]:
            print("Error: Opcion no valida")
            return
        
        # Mostrar perfil
        paises = {
            "1": "España",
            "2": "México",
            "3": "Argentina",
        }
    
        articulo = "el" if sexo == "M" else "la"
        print(f"\nHola {nombre}!")
        print(f"Eres {articulo} usuari{'a' if sexo == 'F' else 'o'} de {paises[pais]}")  
        print(f"Tu cosa favorita es {opciones[pais][int(favorito) - 1]}")
        
    if __name__ == "__main__":
        crear_perfil()