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


def registrar_libro(biblioteca):
    isbn = input("ISBN: ").strip()
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    anio = input("Año: ").strip()
    genero = input("Género: ").strip()

    libro = Libro(isbn, titulo, autor, genero, anio)
    biblioteca.registrar_libro(libro)

def registrar_usuario(biblioteca):
    id = input("Id: ").strip()
    nombre = input("Nombre: ").strip()
    apellidos = input("Apellidos: ").strip()
    email = input("Email: ").strip()

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
    tipo = int(input("¿Cómo quieres buscar?: "))
    if tipo == 1:
        isbn = input("ISBN: ").strip()
        libro = biblioteca.buscar_libro(isbn)
        if libro:
            print(libro)
        else:
            print("No existe ningún libro con ese ISBN")
    elif tipo == 2:
        titulo = input("Título: ").strip()
        mostrar_libros(biblioteca.buscar_por_titulo(titulo))
    elif tipo == 3:
        autor = input("Autor: ").strip()
        mostrar_libros(biblioteca.buscar_por_autor(autor))
    else:
        print("Opcion incorrecta")

def listar_libros(biblioteca):
    print("1. Todos los libros")
    print("2. Libros disponibles")
    print("3. Libros prestados")
    tipo = int(input("¿Qué libros quieres ver?: "))
    if tipo == 1:
        mostrar_libros(biblioteca.libros)
    elif tipo == 2:
        mostrar_libros(biblioteca.listar_disponibles())
    elif tipo == 3:
        mostrar_libros(biblioteca.listar_prestados())
    else:
        print("Opcion incorrecta")

def main():
    miBiblioteca = Biblioteca()

    while True:
        mostrarMenu()
        opcion = int(input("Introduce la opción que quieres: "))
        if opcion == 1:
            registrar_libro(miBiblioteca)
        elif opcion == 2:
            registrar_usuario(miBiblioteca)
        elif opcion == 3:
            buscar_libro(miBiblioteca)
        elif opcion == 4:
            listar_libros(miBiblioteca)
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
             pass
        elif opcion == 9:
            pass
        elif opcion == 0:
            print("Has salido del programa")
            break 
        else:
            print("Opcion incorrecta")   


if __name__ == "__main__":
    main()