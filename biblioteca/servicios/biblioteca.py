from modelos.libro import Libro
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
