class Modelo:
    def __init__(self,modelovehiculo=str,codigo=int):
        self.modelovehiculo = modelovehiculo
        self.codigo = codigo

    def __str__(self):
        return f"MODELO: {self.modelovehiculo}"

    def __repr__(self):
        return f"MODELO: {self.modelovehiculo}"