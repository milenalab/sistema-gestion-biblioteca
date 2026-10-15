from datetime import date


class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha = date.today()
        self.activo = True

    def finalizar(self):
        self.activo = False

    def __str__(self):
        return f"Préstamo del libro '{self.libro.titulo}' a {self.usuario} el {self.fecha} - {'Activo' if self.activo else 'Finalizado'}"
    