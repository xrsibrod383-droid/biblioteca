from datetime import date
from modelos.libro import Libro
from modelos.prestamo import Prestamo
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca

def mostrarMenu():
    print("=========BIBLIOTECA=========")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Buscar libro")
    print("4. Listar libros")
    print("5. Realizar préstamo")
    print("6. Registrar devolución")
    print("7. Mostrar préstamos activos")
    print("8. Mostrar préstamos de un usuario")
    print("9. Guardar datos")
    print("0. Salir")
    print("=============================")


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Este campo no puede estar vacío")

def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes introducir un número")

def registrar_libro(biblioteca):
    isbn = pedir_texto("ISBN: ")
    titulo = pedir_texto("Título: ")
    autor = pedir_texto("Autor: ")
    anio = pedir_numero("Año: ")
    while anio < 0 or anio > date.today().year:
        print("El año no es válido")
        anio = pedir_numero("Año: ")
    genero = pedir_texto("Género: ")

    libro = Libro(isbn, titulo, autor, genero, anio)
    biblioteca.registrar_libro(libro)

def registrar_usuario(biblioteca):
    id = pedir_texto("Id: ")
    nombre = pedir_texto("Nombre: ")
    apellidos = pedir_texto("Apellidos: ")
    email = pedir_texto("Email: ")
    while "@" not in email:
        print("El email no es válido")
        email = pedir_texto("Email: ")

    usuario = Usuario(id, nombre, apellidos, email)
    biblioteca.registrar_usuario(usuario)

def mostrar_libros(libros):
    if not libros:
        print("No se ha encontrado ningún libro")
        return
    for libro in libros:
        print(libro)

def buscar_libro(biblioteca):
    print("1. Buscar por ISBN")
    print("2. Buscar por título")
    print("3. Buscar por autor")
    tipo = pedir_numero("¿Cómo quieres buscar?: ")
    if tipo == 1:
        isbn = pedir_texto("ISBN: ")
        libro = biblioteca.buscar_libro(isbn)
        if libro:
            print(libro)
        else:
            print("No existe ningún libro con ese ISBN")
    elif tipo == 2:
        titulo = pedir_texto("Título: ")
        mostrar_libros(biblioteca.buscar_por_titulo(titulo))
    elif tipo == 3:
        autor = pedir_texto("Autor: ")
        mostrar_libros(biblioteca.buscar_por_autor(autor))
    else:
        print("Opcion incorrecta")

def listar_libros(biblioteca):
    print("1. Todos los libros")
    print("2. Libros disponibles")
    print("3. Libros prestados")
    tipo = pedir_numero("¿Qué libros quieres ver?: ")
    if tipo == 1:
        mostrar_libros(biblioteca.libros)
    elif tipo == 2:
        mostrar_libros(biblioteca.listar_disponibles())
    elif tipo == 3:
        mostrar_libros(biblioteca.listar_prestados())
    else:
        print("Opcion incorrecta")

def realizar_prestamo(biblioteca):
    id_usuario = pedir_texto("Id del usuario: ")
    isbn = pedir_texto("ISBN del libro: ")
    biblioteca.realizar_prestamo(id_usuario, isbn)

def registrar_devolucion(biblioteca):
    isbn = pedir_texto("ISBN del libro: ")
    biblioteca.registrar_devolucion(isbn)

def mostrar_prestamos_activos(biblioteca):
    activos = biblioteca.listar_prestamos_activos()
    if not activos:
        print("No hay ningún préstamo activo")
        return
    for prestamo in activos:
        print(f"{prestamo.libro.isbn} - {prestamo.libro.titulo} - Usuario: {prestamo.usuario.id} - Fecha: {prestamo.fecha_prestamo}")

def mostrar_prestamos_usuario(biblioteca):
    id_usuario = pedir_texto("Id del usuario: ")
    usuario = biblioteca.buscar_usuario(id_usuario)
    if not usuario:
        print(f"ERROR: No existe ningún usuario con el id {id_usuario}")
        return
    prestamos = biblioteca.prestamos_de_usuario(id_usuario)
    print(f"PRÉSTAMOS DE {usuario.nombre.upper()} {usuario.apellidos.upper()}")
    if not prestamos:
        print("Este usuario no tiene ningún préstamo")
        return
    for prestamo in prestamos:
        estado = "Activo" if prestamo.activo else "Devuelto"
        print(f"{prestamo.libro.isbn} - {prestamo.libro.titulo} - {estado}")

def main():
    miBiblioteca = Biblioteca()
    miBiblioteca.cargar_datos()

    while True:
        mostrarMenu()
        opcion = pedir_numero("Introduce la opción que quieres: ")
        if opcion == 1:
            registrar_libro(miBiblioteca)
        elif opcion == 2:
            registrar_usuario(miBiblioteca)
        elif opcion == 3:
            buscar_libro(miBiblioteca)
        elif opcion == 4:
            listar_libros(miBiblioteca)
        elif opcion == 5:
            realizar_prestamo(miBiblioteca)
        elif opcion == 6:
            registrar_devolucion(miBiblioteca)
        elif opcion == 7:
            mostrar_prestamos_activos(miBiblioteca)
        elif opcion == 8:
            mostrar_prestamos_usuario(miBiblioteca)
        elif opcion == 9:
            miBiblioteca.guardar_datos()
        elif opcion == 0:
            miBiblioteca.guardar_datos()
            print("Has salido del programa")
            break 
        else:
            print("Opcion incorrecta")   


if __name__ == "__main__":
    main()