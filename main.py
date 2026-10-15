from clases.biblioteca import Biblioteca


def menu():
    print("=== Menú de la Biblioteca ===")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Listar libros")
    print("6. Listar libros disponibles")
    print("7. Listar usuarios")
    print("8. Listar préstamos activos")
    print("9. Salir")

def main():
    biblioteca = Biblioteca("Biblioteca Milena")

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            exito, mensaje = biblioteca.registrar_libro(titulo, autor, isbn)
            print(mensaje)

        elif opcion == "2":
            nombre = input("Ingrese el nombre del usuario: ")
            dni = input("Ingrese el DNI del usuario: ")
            exito, mensaje = biblioteca.registrar_usuario(nombre, dni)
            print(mensaje)

        elif opcion == "3":
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            dni = input("Ingrese el DNI del usuario que solicita el préstamo: ")
            exito, mensaje = biblioteca.prestar_libro(isbn, dni)
            print(mensaje)

        elif opcion == "4":
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            dni = input("Ingrese el DNI del usuario que devuelve el libro: ")
            exito, mensaje = biblioteca.devolver_libro(isbn, dni)
            print(mensaje)

        elif opcion == "5":
            libros = biblioteca.listar_libros()
            print("\n=== Lista de Libros ===")
            for libro in libros:
                print(libro)

        elif opcion == "6":
            libros_disponibles = [libro for libro in biblioteca.listar_libros() if 'Disponible' in libro]
            print("\n=== Lista de Libros Disponibles ===")
            for libro in libros_disponibles:
                print(libro)

        elif opcion == "7":
            usuarios = biblioteca.listar_usuarios()
            print("\n=== Lista de Usuarios ===")
            for usuario in usuarios:
                print(usuario)

        elif opcion == "8":
            prestamos_activos = biblioteca.listar_prestamos_activos()
            print("\n=== Lista de Préstamos Activos ===")
            for prestamo in prestamos_activos:
                print(prestamo)

        elif opcion == "9":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
    