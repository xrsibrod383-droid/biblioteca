# Biblioteca

## Descripción

Aplicación de consola en Python para gestionar una biblioteca. Permite registrar libros y usuarios, hacer préstamos y devoluciones, consultar los libros y los préstamos, y guardar toda la información en un fichero JSON para que no se pierda al cerrar el programa.

## Instalación

1. Tener instalado Python 3.
2. Clonar el repositorio:

```bash
git clone https://github.com/xrsibrod383-droid/biblioteca.git
```

No hace falta instalar nada más, solo se usan módulos que vienen con Python (`json`, `os` y `datetime`), por eso no hay `requirements.txt`.

## Ejecución

```bash
cd biblioteca
python main.py
```

## Estructura

```text
biblioteca/
├── main.py              → menú y comunicación con el usuario
├── modelos/
│   ├── libro.py         → clase Libro
│   ├── usuario.py       → clase Usuario
│   └── prestamo.py      → clase Prestamo
├── servicios/
│   └── biblioteca.py    → clase Biblioteca, con toda la lógica
└── datos/
    └── biblioteca.json  → se crea al guardar los datos
```

He usado un solo fichero JSON para guardar libros, usuarios y préstamos juntos, porque los préstamos guardan el id del usuario y el ISBN del libro y así al cargar se pueden enlazar con sus objetos.

## Diseño

- **Libro**: guarda el ISBN, título, autor, año, género y si está disponible o no.
- **Usuario**: guarda el id, nombre, apellidos y email.
- **Prestamo**: relaciona un usuario con un libro y guarda la fecha del préstamo y la de devolución. La propiedad `activo` indica si el libro todavía no se ha devuelto.
- **Biblioteca**: tiene las listas de libros, usuarios y préstamos y se encarga de todas las operaciones: registrar, buscar, prestar, devolver, consultar y guardar/cargar el JSON. Es la que comprueba las reglas (que no haya duplicados, que el libro esté disponible, etc.).

`main.py` solo muestra el menú, pide los datos y llama a los métodos de `Biblioteca`. También tiene las funciones `pedir_texto` y `pedir_numero` para validar lo que se escribe.

## Funcionalidades

1. Registrar libro (no deja ISBN repetidos y comprueba que el año sea un número válido).
2. Registrar usuario (no deja ids repetidos y comprueba el email).
3. Buscar libro por ISBN, por título o por autor.
4. Listar todos los libros, solo los disponibles o solo los prestados.
5. Realizar préstamo (el usuario y el libro tienen que existir y el libro tiene que estar disponible).
6. Registrar devolución (solo si el libro tiene un préstamo activo).
7. Mostrar los préstamos activos.
8. Mostrar los préstamos de un usuario.
9. Guardar datos en el JSON.
0. Salir (también guarda los datos).

Al arrancar se cargan los datos guardados. Si el fichero no existe se empieza con la biblioteca vacía y si está mal se avisa del error. Si se escribe una letra donde va un número o se deja un campo vacío, el programa avisa y lo vuelve a pedir.
