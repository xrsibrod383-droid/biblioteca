import json
import os
from datetime import date
from modelos.libro import Libro
from modelos.prestamo import Prestamo
from modelos.usuario import Usuario

FICHERO_DATOS = "datos/biblioteca.json"

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

    def buscar_prestamo_activo(self, isbn):
        for prestamo in self.prestamos:
            if prestamo.libro.isbn == isbn and prestamo.activo:
                return prestamo
        return None

    def registrar_devolucion(self, isbn):
        libro = self.buscar_libro(isbn)
        if not libro:
            print(f"ERROR: No existe ningún libro con el ISBN {isbn}")
            return
        prestamo = self.buscar_prestamo_activo(isbn)
        if not prestamo:
            print(f"ERROR: El libro {isbn} no tiene ningún préstamo activo")
            return
        prestamo.fecha_devolucion = date.today()
        libro.disponible = True
        print("Libro devuelto correctamente")

    def listar_prestamos_activos(self):
        activos = []
        for prestamo in self.prestamos:
            if prestamo.activo:
                activos.append(prestamo)
        return activos

    def prestamos_de_usuario(self, id_usuario):
        encontrados = []
        for prestamo in self.prestamos:
            if prestamo.usuario.id == id_usuario:
                encontrados.append(prestamo)
        return encontrados

    def guardar_datos(self):
        datos = {"libros": [], "usuarios": [], "prestamos": []}
        for libro in self.libros:
            datos["libros"].append({
                "isbn": libro.isbn,
                "titulo": libro.titulo,
                "autor": libro.autor,
                "anio": libro.anio,
                "genero": libro.genero,
                "disponible": libro.disponible
            })
        for usuario in self.usuarios:
            datos["usuarios"].append({
                "id": usuario.id,
                "nombre": usuario.nombre,
                "apellidos": usuario.apellidos,
                "email": usuario.email
            })
        for prestamo in self.prestamos:
            fecha_devolucion = None
            if prestamo.fecha_devolucion:
                fecha_devolucion = str(prestamo.fecha_devolucion)
            datos["prestamos"].append({
                "usuario": prestamo.usuario.id,
                "libro": prestamo.libro.isbn,
                "fecha_prestamo": str(prestamo.fecha_prestamo),
                "fecha_devolucion": fecha_devolucion
            })
        try:
            os.makedirs("datos", exist_ok=True)
            with open(FICHERO_DATOS, "w", encoding="utf-8") as fichero:
                json.dump(datos, fichero, indent=4, ensure_ascii=False)
            print("Datos guardados correctamente")
        except OSError as e:
            print(f"ERROR: No se han podido guardar los datos -> {e}")

    def cargar_datos(self):
        if not os.path.exists(FICHERO_DATOS):
            print("No hay datos guardados, la biblioteca empieza vacía")
            return
        try:
            with open(FICHERO_DATOS, "r", encoding="utf-8") as fichero:
                datos = json.load(fichero)
            for libro in datos["libros"]:
                self.libros.append(Libro(libro["isbn"], libro["titulo"], libro["autor"], libro["genero"], libro["anio"], libro["disponible"]))
            for usuario in datos["usuarios"]:
                self.usuarios.append(Usuario(usuario["id"], usuario["nombre"], usuario["apellidos"], usuario["email"]))
            for prestamo in datos["prestamos"]:
                usuario = self.buscar_usuario(prestamo["usuario"])
                libro = self.buscar_libro(prestamo["libro"])
                if usuario and libro:
                    self.prestamos.append(Prestamo(usuario, libro, prestamo["fecha_prestamo"], prestamo["fecha_devolucion"]))
            print("Datos cargados correctamente")
        except (json.JSONDecodeError, KeyError) as e:
            print(f"ERROR: El fichero de datos no es válido -> {e}")
            self.libros = []
            self.usuarios = []
            self.prestamos = []
