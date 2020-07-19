from tda_lista_lista import Lista, insertar, eliminar, busqueda, barrido, barrido_con_sublista, tamanio, lista_vacia
from random import randint
from datetime import datetime

class Vuelo(object):
    
    def __init__(self,empresa,numero,cantidadAsientos,fechaSalida,destino,kmVuelo):
        self.empresa = empresa
        self.numero = numero
        self.cantidadAsientos = cantidadAsientos
        self.fechaSalida = fechaSalida
        self.destino = destino
        self.kmVuelo = kmVuelo
    
    def __str__(self):
        fecha1 = self.fechaSalida.strftime("%m/%d/%Y")
        return "Empresa: " + self.empresa + ". Destino : " + self.destino +". Numero de Vuelo : "+ str(self.numero) + '\n' + "Cantidad de asientos: " + str(self.cantidadAsientos) + ". Fecha de Salida :  " + fecha1
        
class clasesAsientos(object):
    
    def __init__(self,TotalesTurista,TotalesPrimeraClase,OcupadosTurista,OcupadosPrimeraClase):
        
        self.TotalesTurista = TotalesTurista
        self.TotalesPrimeraClase = TotalesPrimeraClase
        self.OcupadosTurista = OcupadosTurista
        self.OcupadosPrimeraClase = OcupadosPrimeraClase
        
    def __str__(self):
        return " Asientos turistas Totales : " + str(self.TotalesTurista) + '\n' + " Asientos Primera Clase Totales : " + str(self.TotalesPrimeraClase) + '\n' + " Asientos turistas ocupados : " + str(self.OcupadosTurista) + '\n' + " Asientos Primera clase ocupados : " + str(self.OcupadosPrimeraClase)
        
def inicializar(lista):
    
    fecha = datetime(2020,2,10)
    vuelo1 = Vuelo("jet2",1,600,fecha,"Tailandia",3500)
    insertar(aeropuerto,vuelo1,"numero")

    clase1 = clasesAsientos(500,100,451,20)
    auxi = busqueda(aeropuerto,"jet2","empresa")
    insertar(auxi.sublista,clase1)


    fecha = datetime(2020,2,10)
    vuelo1 = Vuelo("Aeroflot",2,300,fecha,"Rodas",1000)
    insertar(lista,vuelo1,"numero")
    
    clase1 = clasesAsientos(200,100,51,2)
    auxi = busqueda(aeropuerto,"Aeroflot","empresa")
    insertar(auxi.sublista,clase1)
    
    
    fecha = datetime(2020,2,10)
    vuelo1 = Vuelo("Primera Air",3,350,fecha,"Miconos",2000)
    insertar(lista,vuelo1,"numero")
    
    clase1 = clasesAsientos(250,100,250,1)
    auxi = busqueda(aeropuerto,"Primera Air","empresa")
    insertar(auxi.sublista,clase1)
    
    
    fecha = datetime(2020,4,10)
    vuelo1 = Vuelo("SAS",4,600,fecha,"Atenas",1500)
    insertar(lista,vuelo1,"numero")

    clase1 = clasesAsientos(500,100,500,20)
    auxi = busqueda(aeropuerto,"SAS","empresa")
    insertar(auxi.sublista,clase1)         

def mostrarViajes(lista):
    print("    Viajes a Atenas, Miconos, Rodas.")
    aux = lista.inicio
    while (aux is not None):
        if (aux.info.destino == "Atenas" or aux.info.destino == "Miconos" or aux.info.destino == "Rodas"):
            print(aux.info)
        aux = aux.sig
         
def turistasDisponibles(lista):
    print(" ")
    print("Vuelos con asientos turista disponibles: ",'\n')
    aux = lista.inicio
    sub = aux.sublista.inicio
    while (aux is not None):
        sub = aux.sublista.inicio
        while (sub is not None):
            if (sub.info.OcupadosTurista < sub.info.TotalesTurista):
                print("TURISTA DISPONIBLE: ",aux.info)
            sub = sub.sig
        aux = aux.sig
    


def recaudo(lista):
    print(" ")
    print("Recaudos por vuelo : ")
    aux = lista.inicio    
    sub = aux.sublista.inicio
    while (aux is not None):
        RTurista = 75 * aux.info.kmVuelo
        RPrimeraClase = 203 * aux.info.kmVuelo
        while (sub is not None):
            RTurista = RTurista * sub.info.OcupadosTurista
            RPrimeraClase = RPrimeraClase * sub.info.OcupadosPrimeraClase
            sub = sub.sig
        print("Vuelo :",aux.info.numero)
        print("Recaudacion clase Turista $ ", RTurista)
        print("Recaudacion Primera clase $ ", RPrimeraClase)
        aux = aux.sig
        
def vuelosPorFecha(lista):
    print("Mostrar Vuelos programados para la fecha.")
    a = int(input("Dia: "))
    b = int(input("Mes: "))
    c = int(input("Anio: "))
    fecha = datetime(a,b,c)
    aux = lista.inicio
    while (aux is not None):
        if (aux.info.fechaSalida == fecha):
            print(aux.info)
        aux = aux.sig    
    
def venderPasajeTurista(lista):
    print(" ")
    print("Vender pasaje.")
    n = int(input("Numero de vuelo: "))
    aux = busqueda(aeropuerto,n,"numero")
    #turOPrime = int(input(" (1) - Turista. (2) - Primera clase: "))
    print(aux.info)
    print(" ")
    sub = aux.sublista
    print(" ")
    print(sub.inicio.info.TotalesTurista)
    print(sub.inicio.info.TotalesPrimeraClase)
    print(sub.inicio.info.OcupadosTurista)
    print(sub.inicio.info.OcupadosPrimeraClase)
    print(" ")
    
    a = sub.inicio.info.TotalesTurista
    b = sub.inicio.info.TotalesPrimeraClase
    c = int(sub.inicio.info.OcupadosTurista) + 1
    print("MARCA",c)
    d = sub.inicio.info.OcupadosPrimeraClase
    clave1 = sub.inicio.info.TotalesTurista
    eliminar(aux.sublista,clave1,"TotalesTurista")
    asientos1 = clasesAsientos(a,b,c,d)
    insertar(aux.sublista,asientos1)
    barrido_con_sublista(lista)

def venderPasajePrimera(lista):
    print(" ")
    print("Vender pasaje.")
    n = int(input("Numero de vuelo: "))
    aux = busqueda(aeropuerto,n,"numero")
    sub = aux.sublista
    a = sub.inicio.info.TotalesTurista
    b = sub.inicio.info.TotalesPrimeraClase
    c = sub.inicio.info.OcupadosTurista
    d = int(sub.inicio.info.OcupadosPrimeraClase)  + 1
    clave1 = sub.inicio.info.TotalesTurista
    eliminar(aux.sublista,clave1,"TotalesTurista")
    asientos1 = clasesAsientos(a,b,c,d)
    insertar(aux.sublista,asientos1)
    #barrido_con_sublista(lista)
    
def cancelarVuelo(lista):
    print(" ")
    print("Cancelar Vuelo.")
    n = int(input("Numero de vuelo: "))
    aux = busqueda(aeropuerto,n,"numero")
    sub = aux.sublista
    kms1= aux.info.kmVuelo
    devolver1 = int(sub.inicio.info.OcupadosTurista) * 75
    devolver2 = int(sub.inicio.info.OcupadosPrimeraClase) * 203 
    clave1 = aux.info.numero
    eliminar(lista,clave1,"numero")
    print("Dinero a devolver: ",(devolver1 + devolver2) * kms1)
    barrido(lista)

def destinoTailandia(lista):
    aux = lista.inicio
    while (aux is not None):
        if (aux.info.destino == "Tailandia"):
            print(aux.info.empresa)
            print(aux.info.kmVuelo)
        aux =  aux.sig

aeropuerto = Lista()
inicializar(aeropuerto)
barrido_con_sublista(aeropuerto)
mostrarViajes(aeropuerto)
turistasDisponibles(aeropuerto)
recaudo(aeropuerto)
#vuelosPorFecha(aeropuerto)
#venderPasajeTurista(aeropuerto)
#venderPasajePrimera(aeropuerto)
#cancelarVuelo(aeropuerto)
destinoTailandia(aeropuerto)