from servicios.biblioteca_servicio import BibliotecaServicio
from modelos.libro import Libro
from modelos.usuarios import Usuario

def main():
    servicio = BibliotecaServicio()

    while True:
        print("\n--- Menú Biblioteca ---")
        print("1. Añadir libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar libro por título")
        print("6. Listar libros prestados")
        print("0. Salir")

        opcion = input("Elija opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            servicio.agregar_libro(libro)
            print("Libro añadido.")

        elif opcion == "2":
            nombre = input("Nombre usuario: ")
            id_usuario = input("ID usuario: ")
            usuario = Usuario(nombre, id_usuario)
            servicio.registrar_usuario(usuario)
            print("Usuario registrado.")

        elif opcion == "3":
            id_usuario = input("ID usuario: ")
            isbn = input("ISBN libro: ")
            servicio.prestar_libro(id_usuario, isbn)
            print("Libro prestado.")

        elif opcion == "4":
            id_usuario = input("ID usuario: ")
            isbn = input("ISBN libro: ")
            servicio.devolver_libro(id_usuario, isbn)
            print("Libro devuelto.")

        elif opcion == "5":
            titulo = input("Título a buscar: ")
            resultados = servicio.buscar_por_titulo(titulo)
            for libro in resultados:
                print(f"{libro.titulo_autor[0]} - {libro.titulo_autor[1]}")

        elif opcion == "6":
            id_usuario = input("ID usuario: ")
            libros = servicio.listar_libros_prestados(id_usuario)
            for libro in libros:
                print(f"{libro.titulo_autor[0]} - {libro.titulo_autor[1]}")

        elif opcion == "0":
            break

if __name__ == "__main__":
    main()  #fin
