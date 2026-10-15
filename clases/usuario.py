class Usuario:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.prestamos = []

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def __str__(self):
        return f"Usuario: {self.nombre} | DNI: {self.dni}"

