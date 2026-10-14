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

    libro = Libro(isbn, titulo, autor, anio, genero)
    biblioteca.registrar_libro(libro)

def main():
    miBiblioteca = Biblioteca()

    while True:
        mostrarMenu()
        opcion = int(input("Introduce la opción que quieres: "))
        if opcion == 1:
            registrar_libro(miBiblioteca)
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
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