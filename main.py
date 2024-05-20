from propietario import Propietario
from marca import Marca
from modelo import Modelo
from vehiculo import Vehiculo

listavehiculo=[]
listamodelo=[]
listamarca=[]
listapropietario=[]

def lecturadebasededatos():
    try:
        with open("basededatos.txt","r") as file:
            archivo = file.readlines()
            for linea in archivo:
                lineas = linea.strip().split(",")
                dni,nombre,telefono,tipovehiculo,codigov,patente,modelovehiculo,codigomod,codigomarca,marca = lineas
                propietario = (Propietario(dni,nombre,telefono))
                listapropietario.append(propietario)
                modelo = (Modelo(modelovehiculo,codigomod))
                listamodelo.append(modelo)
                marca = (Marca(codigomarca,marca))
                listamarca.append(marca)
                vehiculo = (Vehiculo(tipovehiculo,codigov,patente,propietario,modelo,marca))
                listavehiculo.append(vehiculo)
    except FileNotFoundError:
        print("ARCHIVO NO ENCONTRADO")

def listarvehiculos():
    try:
        print("LISTA DE VEHICULOS Y PROPIETARIOS EN TALLER DE PINTURA".center(120))
        for vehiculo in listavehiculo:
            print(f"TIPO DE VEHICULO : {vehiculo.tipovehiculo}, {vehiculo.propietario}, {vehiculo.modelo}, {vehiculo.marca}")
    except Exception as e:
        print(f"ERROR A LISTAR LOS VEHICULOS {e}")
def marcaIguales():
    try:
        marca = str(input("LISTAR NUMERO DE VEHICULOS DE LA MARCA : "))
        marca = marca.capitalize()
        Marca.cantidadMarcaiguales(marca,listamarca)
    except ValueError:
        print("INGRESO INCORRECTO")
def cantidadvehiculos():
    Vehiculo.cantidadVehiculoTipo(listavehiculo)

def main():
    try:
        lecturadebasededatos()
        while True:
            print("INGRESE LA OPCIÓN DESEADA".center(120))

            print("INGRESE 0 PARA SALIR".center(120))
            ingreso = int(input("LISTAR VEHICULOS EXISTENTES EN TALLER - 1 / CONSULTAR SOBRE CANTIDAD VEHICULO SEGÚN SU MARCA - 2 / CONSULTAR TIPO DE VEHICULOS Y CANTIDAD EXISTENTES - 3 :  "))
            if ingreso == 1:
                listarvehiculos()
            if ingreso == 2:
                marcaIguales()
            if ingreso == 3:
                cantidadvehiculos()
            if ingreso == 0:
                print(" NOS VEMOS LUEGO ")
                break
            else:
                if ingreso != 1 and ingreso !=2 and ingreso !=3 and ingreso != 0:


                    print("INGRESO INCORRECTO")
    except Exception as e:
        print(f"ERROR {e}")


if __name__=="__main__":
    main()