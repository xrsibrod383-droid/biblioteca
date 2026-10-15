from modelos.libro import Libro
from modelos.prestamo import Prestamo
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro_nuevo):
        if self.buscar_libro(libro_nuevo.isbn):
            print("El libro ya esta en la lista")
            return
        self.libros.append(libro_nuevo)
        print("Libro registrado correctamente")

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_por_titulo(self, titulo):
        encontrados = []
        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower():
                encontrados.append(libro)
        return encontrados

    def buscar_por_autor(self, autor):
        encontrados = []
        for libro in self.libros:
            if autor.lower() in libro.autor.lower():
                encontrados.append(libro)
        return encontrados

    def listar_disponibles(self):
        disponibles = []
        for libro in self.libros:
            if libro.disponible:
                disponibles.append(libro)
        return disponibles

    def listar_prestados(self):
        prestados = []
        for libro in self.libros:
            if not libro.disponible:
                prestados.append(libro)
        return prestados

    def registrar_usuario(self, usuario_nuevo):
        if self.buscar_usuario(usuario_nuevo.id):
            print("El usuario ya esta en la lista")
            return
        self.usuarios.append(usuario_nuevo)
        print("Usuario registrado correctamente")

    def buscar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario
        return None

    def realizar_prestamo(self, id_usuario, isbn):
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            print(f"ERROR: No existe ningún usuario con el id {id_usuario}")
            return
        libro = self.buscar_libro(isbn)
        if not libro:
            print(f"ERROR: No existe ningún libro con el ISBN {isbn}")
            return
        if not libro.disponible:
            print(f"ERROR: El libro {isbn} ya se encuentra prestado")
            return
        prestamo = Prestamo(usuario, libro)
        self.prestamos.append(prestamo)
        libro.disponible = False
        print("Préstamo realizado correctamente")
