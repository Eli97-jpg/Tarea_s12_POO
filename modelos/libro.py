class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # título y autor en tupla
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
