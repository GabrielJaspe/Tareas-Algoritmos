class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __repr__(self):
        return f"{self.model} ({self.year})"

def bubble_sort(vehicles):
    n = len(vehicles)
    for i in range(n):
        for j in range(0, n-i-1):
            if vehicles[j].year > vehicles[j+1].year:
                vehicles[j], vehicles[j+1] = vehicles[j+1], vehicles[j]

def insertion_sort(vehicles):
    for i in range(1, len(vehicles)):
        key = vehicles[i]
        j = i-1
        while j >= 0 and key.year < vehicles[j].year:
            vehicles[j + 1] = vehicles[j]
            j -= 1
        vehicles[j + 1] = key

def selection_sort(vehicles):
    n = len(vehicles)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if vehicles[j].year < vehicles[min_idx].year:
                min_idx = j
        vehicles[i], vehicles[min_idx] = vehicles[min_idx], vehicles[i]

def binary_search(vehicles, year):
    left, right = 0, len(vehicles) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if vehicles[mid].year == year:
            return mid
        elif vehicles[mid].year < year:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    # Crear una lista de vehículos
    vehicles = [
        Vehicle("Car A", 2015),
        Vehicle("Car B", 2018),
        Vehicle("Car C", 2012),
        Vehicle("Car D", 2020),
        Vehicle("Car E", 2017)
    ]

    # Ordenar la lista de vehículos usando uno de los algoritmos
    print("Lista de vehículos antes de ordenar:")
    print(vehicles)
    
    bubble_sort(vehicles)
    print("\nLista de vehículos después de ordenar con Bubble Sort:")
    print(vehicles)
    
    insertion_sort(vehicles)
    print("\nLista de vehículos después de ordenar con Insertion Sort:")
    print(vehicles)
    
    selection_sort(vehicles)
    print("\nLista de vehículos después de ordenar con Selection Sort:")
    print(vehicles)

    # Solicitar al usuario el año del vehículo que desea buscar
    year_to_search = int(input("\nIntroduce el año del vehículo que deseas buscar: "))
    index = binary_search(vehicles, year_to_search)

    if index != -1:
        print(f"Vehículo encontrado: {vehicles[index]}")
    else:
        print("Vehículo no encontrado.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
