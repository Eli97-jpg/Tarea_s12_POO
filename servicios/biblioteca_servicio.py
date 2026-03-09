from modelos.libro import Libro
from modelos.usuarios import Usuario

class BibliotecaServicio:
    def __init__(self):
        self.libros = {}       # diccionario {isbn: libro}
        self.usuarios = {}     # diccionario {id: usuario}
        self.ids_usuarios = set()  # conjunto de IDs únicos

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.libros_prestados.append(libro)
            del self.libros[isbn]

    def devolver_libro(self, id_usuario, isbn):
        usuario = self.usuarios.get(id_usuario)
        if usuario:
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    break

    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros.values() if libro.titulo_autor[0] == titulo]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros.values() if libro.titulo_autor[1] == autor]

    def buscar_por_categoria(self, categoria):
        return [libro for libro in self.libros.values() if libro.categoria == categoria]

    def listar_libros_prestados(self, id_usuario):
        usuario = self.usuarios.get(id_usuario)
        if usuario:
            return usuario.libros_prestados
        return []
