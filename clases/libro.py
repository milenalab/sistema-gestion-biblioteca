class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if not self.disponible:
            return False
        self.disponible = False
        return True

    def devolver(self):
        if self.disponible:
            return False
        self.disponible = True
        return True

    def __str__(self):
        return f"El título es '{self.titulo}' por {self.autor} (ISBN: {self.isbn}) - {'Disponible' if self.disponible else 'No disponible'}"


    