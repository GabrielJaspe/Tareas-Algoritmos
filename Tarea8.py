class Carro:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}"


class Barco:
    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad 

    def mostrar_info(self):
        return f"Marca: {self.nombre}, Modelo: {self.tipo}, Año: {self.capacidad}"
    

class Avion:
    def __init__(self, aerolinea, modelo, alcance):
            self.aerolinea = aerolinea
            self.modelo = modelo
            self.alcance = alcance
    
    def mostrar_info(self):
        return f"Marca: {self.aerolinea}, Modelo: {self.modelo}, Año: {self.alcance}" 
    
carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Ford", "Explorer", 2019)
carro3 = Carro("Chevrolet", "Camaro", 2018)

barco1 = Barco("Titanic", "Crucero", 2200)
barco2 = Barco("Mar azul", "Pesquero", 100)

avion1 = Avion("conviasa", "Boeing 747", 10000)
avion2 = Avion("Aeropostal", "Airbus A380", 15000)

vehiculos = [carro1, carro2, carro3, barco1, barco2, avion1, avion2]

for vehiculo in vehiculos:
    print(vehiculo.mostrar_info())