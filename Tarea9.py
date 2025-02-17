from datetime import datetime

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.trabajando = False

    def marcar_jornada(self):
        if self.trabajando:
            self.trabajando = False
            print(f"{self.nombre} ha terminado su jornada laboral.")
        else:
            self.trabajando = True
            self.iniciar_jornada()

    def iniciar_jornada(self):
        pass

class Profesor(Empleado):
    def iniciar_jornada(self):
        print(f"{self.nombre} ha comenzado su jornada: Preparando clases.")

class Administrativo(Empleado):
    def iniciar_jornada(self):
        print(f"{self.nombre} ha comenzado su jornada: Revisando documentos.")

class Mantenimiento(Empleado):
    def iniciar_jornada(self):
        print(f"{self.nombre} ha comenzado su jornada: Inspeccionando equipos.")

# Ejemplo de uso
empleados = [
    Profesor("Carlos"),
    Administrativo("Ana"),
    Mantenimiento("Luis")
]

for empleado in empleados:
    empleado.marcar_jornada()

print("--- Fin de jornada ---")

for empleado in empleados:
    empleado.marcar_jornada()