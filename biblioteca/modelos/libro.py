class Libro:
    def __init__(self,isbn, titulo, autor, genero, anio = None , disponible = True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.disponible = disponible

    def __str__(self) -> str:   
        estado = "Disponible" if self.disponible else "Prestado" 
        return f"ISBN: {self.isbn} - Título: {self.titulo} - Autor: {self.autor} - Año: {self.anio} - Género: {self.genero} - Disponible: {self.disponible}"
    
    def __repr__(self):
        return(
            f"ISBN: {self.isbn!r}, " 
            f"Título: {self.titulo!r}, "
            f"Autor: {self.autor!r}, "
            f"Año: {self.anio!r}, "
            f"Género: {self.genero!r}, "
            f"Disponible: {self-self.disponible!r}"
        )

    def __eq__ (self, libro):
        return self.isbn == libro.isbn