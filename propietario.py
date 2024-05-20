class Propietario:
    def __init__(self,dni,nombre,telefono):
        self.dni = dni
        self.nombre = nombre
        self.telefono = telefono


    def __str__(self):
        return f"PROPIETARIO: {self.nombre}, DNI:  {self.dni}, TEL : {self.telefono}"

    def __repr__(self):
        return f"PROPIETARIO: {self.nombre}, DNI: {self.dni}, TEL: {self.telefono}"