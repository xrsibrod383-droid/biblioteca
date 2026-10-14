class Usuario:
    def __init__(self,id, nombre, apellidos, email):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __str__(self) -> str:    
        return f"Nombre: {self.nombre} - Apellidos: {self.apellidos} - Id: {self.id} - Email: {self.email}"

    def __repr__(self):
        return(
            f"Nombre: {self.nombre!r}, " 
            f"Apellidos: {self.apellidos!r}, "
            f"Id: {self.id!r}, "
            f"Email: {self.email!r}"
        )

