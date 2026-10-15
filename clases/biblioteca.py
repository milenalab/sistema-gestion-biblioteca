from clases.libro import Libro
from clases.prestamo import Prestamo
from clases.usuario import Usuario


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = {}
        self.usuarios = {}
        self.prestamos = []

    def registrar_libro(self, titulo, autor, isbn):
        if isbn in self.libros:
            return False, "El libro ya está registrado."
        self.libros[isbn] = Libro(titulo, autor, isbn)
        return True, "Libro registrado exitosamente."

    def registrar_usuario(self, nombre, dni):
        if dni in self.usuarios:
            return False, "El usuario ya está registrado."
        self.usuarios[dni] = Usuario(nombre, dni)
        return True, "Usuario registrado exitosamente."

    def prestar_libro(self, isbn, dni):
        if isbn not in self.libros:
            return False, "El libro no está registrado."
        if dni not in self.usuarios:
            return False, "El usuario no está registrado."

        libro = self.libros[isbn]
        usuario = self.usuarios[dni]

        if not libro.prestar():
            return False, "El libro no está disponible para préstamo."

        prestamo = Prestamo(libro, usuario)
        self.prestamos.append(prestamo)
        usuario.agregar_prestamo(prestamo)
        return True, f"Préstamo realizado: {prestamo}"

    def devolver_libro(self, isbn, dni):
        if isbn not in self.libros:
            return False, "El libro no está registrado."
        if dni not in self.usuarios:
            return False, "El usuario no está registrado."

        libro = self.libros[isbn]
        usuario = self.usuarios[dni]

        for prestamo in usuario.prestamos:
            if prestamo.libro == libro and prestamo.activo:
                prestamo.finalizar()
                libro.devolver()
                return True, f"Devolución realizada: {prestamo}"

        return False, "No se encontró un préstamo activo para este libro y usuario."

    def listar_libros(self):
        return [str(libro) for libro in self.libros.values()]

    def listar_usuarios(self):
        return [str(usuario) for usuario in self.usuarios.values()]

    def listar_prestamos_activos(self):
        return [str(prestamo) for prestamo in self.prestamos if prestamo.activo]

    def __str__(self):
        return f"Biblioteca: {self.nombre} | Libros: {len(self.libros)} | Usuarios: {len(self.usuarios)} | Préstamos activos: {len(self.listar_prestamos_activos())}"