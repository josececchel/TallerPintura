class Marca:
    def __init__(self,codigo,marca):
        self.codigo = codigo
        self.marca = marca

    def __str__(self):
        return f"MARCA: {self.marca}"

    def __repr__(self):
        return f"MARCA: {self.marca}"

    def cantidadMarcaiguales(marca,listamarca):
        cont = 0
        for i in listamarca:
            if i.marca == marca:
                cont +=1
                print(f"LA CANTIDAD DE VEHICULOS DE LA MARCA INGRESADA ES : {cont}")