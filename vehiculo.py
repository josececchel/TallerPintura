class Vehiculo:
    def __init__(self,tipovehiculo="",codigo=int,patente=str,marca=None,modelo=None,propietario=None):
        self.tipovehiculo = tipovehiculo
        self.codigo = codigo
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.propietario = propietario

    def __str__(self):
        return f"VEHICULO: {self.tipovehiculo},{self.patente}, {self.marca}, {self.modelo}, {self.propietario}"

    def __repr__(self):
        return f"VEHICULO: {self.tipovehiculo},{self.patente}, {self.marca}, {self.modelo}, {self.propietario}"

    def cantidadVehiculoTipo(listavehiculo):
        tipo={}
        for i in listavehiculo:
            if i.tipovehiculo in tipo:
                tipo[i.tipovehiculo] += 1
            else:
                tipo[i.tipovehiculo] = 1
        for tipos, cantidad in tipo.items():

            print(f"CANTIDAD DE VEHICULOS : {tipos}, {cantidad}")