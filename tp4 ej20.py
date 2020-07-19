from tda_lista_lista import Lista, insertar, eliminar, busqueda, barrido, barrido_con_sublista, tamanio
from datetime import datetime

class Estacion(object):
    
    def __init__(self,pais,latitud,longitud,altitud):
        self.pais = pais
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud
    
    def __str__(self):
        return self.pais + " " + str(self.latitud) + " " + str(self.longitud) + " " + str(self.altitud)
        
class Medicion(object):
    
    def __init__(self,temperatura,presion,humedad,estado,fecha):
        self.temperatura = temperatura
        self.presion = presion
        self.humedad = humedad
        self.estado = estado
        self.fecha = fecha
    
    def __str__(self):
        return str(self.fecha) + " " + self.estado + " " + str(self.humedad) + " " + str(self.presion) + " " + str(self.temperatura)
        
estaciones_meteorilogicas = Lista()

estacion1 = Estacion("Argentina",20,30,2117)
insertar(estaciones_meteorilogicas,estacion1,"pais")

estacion1 = Estacion("Uruguay",45,50,512)
insertar(estaciones_meteorilogicas,estacion1,"pais")

estacion1 = Estacion("Bolivia",30,35,2500)
insertar(estaciones_meteorilogicas,estacion1,"pais")

estacion1 = Estacion("Paraguay",10,30,3117)
insertar(estaciones_meteorilogicas,estacion1,"pais")

estacion1 = Estacion("Chile",20,30,2.900)
insertar(estaciones_meteorilogicas,estacion1,"pais")

barrido(estaciones_meteorilogicas)

aux = estaciones_meteorilogicas.inicio
while aux:
    if aux.info.pais == "Argentina":
        medicion1 = Medicion(2,15,50,"lluvioso",datetime(2020,1,3,17,30))
        insertar(aux.sublista,medicion1,"fecha")
        medicion1 = Medicion(5,30,70,"solado",datetime(2020,2,3,16,40))
        insertar(aux.sublista,medicion1,"fecha")
        medicion1 = Medicion(3,20,50,"lluvioso",datetime(2020,3,3,00,30))
        insertar(aux.sublista,medicion1,"fecha")
    if aux.info.pais == "Uruguay":
        medicion1 = Medicion(2,15,50,"lluvioso",datetime(2020,1,3,17,30))
        insertar(aux.sublista,medicion1,"fecha")
        medicion1 = Medicion(5,30,70,"solado",datetime(2020,2,3,16,40))
        insertar(aux.sublista,medicion1,"fecha")
        medicion1 = Medicion(3,20,50,"lluvioso",datetime(2020,3,3,00,30))
        insertar(aux.sublista,medicion1,"fecha")
    
    if aux.info.pais == "Chile":
        medicion1 = Medicion(2,15,50,"lluvioso",datetime(2020,1,3,17,30))
        insertar(aux.sublista,medicion1,"fecha")
        medicion1 = Medicion(5,30,70,"solado",datetime(2020,2,3,16,40))
        insertar(aux.sublista,medicion1,"fecha")
        medicion1 = Medicion(3,20,50,"lluvioso",datetime(2020,3,3,00,30))
        insertar(aux.sublista,medicion1,"fecha")
    
    if aux.info.pais == "Bolivia":
        medicion1 = Medicion(2,15,50,"nevando",datetime(2020,1,3,17,30))
        insertar(aux.sublista,medicion1,"fecha")
        medicion1 = Medicion(5,30,70,"solado",datetime(2020,2,3,16,40))
        insertar(aux.sublista,medicion1,"fecha")
        medicion1 = Medicion(3,20,50,"lluvioso",datetime(2020,3,3,00,30))
        insertar(aux.sublista,medicion1,"fecha")
    
    if aux.info.pais == "Paraguay":
        medicion1 = Medicion(2,15,50,"lluvioso",datetime(2020,1,3,17,30))
        insertar(aux.sublista,medicion1,"fecha")
        medicion1 = Medicion(5,30,70,"solado",datetime(2020,2,3,16,40))
        insertar(aux.sublista,medicion1,"fecha")
        medicion1 = Medicion(3,20,50,"lluvioso",datetime(2020,3,3,00,30))
        insertar(aux.sublista,medicion1,"fecha")
    aux = aux.sig

#a = busqueda(estaciones_meteorilogicas,"Argentina","pais")
#barrido(a.sublista)
#
#a = busqueda(estaciones_meteorilogicas,"Uruguay","pais")
#barrido(a.sublista)
#
#a = busqueda(estaciones_meteorilogicas,"Bolivia","pais")
#barrido(a.sublista)
#
#a = busqueda(estaciones_meteorilogicas,"Paraguay","pais")
#barrido(a.sublista)
#
#a = busqueda(estaciones_meteorilogicas,"Chile","pais")
#barrido(a.sublista)

acum = 0
cont = 0
aux = estaciones_meteorilogicas.inicio
while aux:
    bandera = False
    bandera2 = False
    print(aux.info.pais)
    sub = aux.sublista.inicio
    while sub:
        print("XXXXXX",sub.info)
        print(sub.info.fecha.month)
        if sub.info.estado == "lluvioso" or sub.info.estado == "nevado":
            bandera = True
        if sub.info.estado == "tormenta electrica" or sub.info.estado == "huracanes":
            bandera2 = True
        if sub.info.fecha.month == 2:
            acum += sub.info.temperatura
            cont += 1
        sub = sub.sig
    if bandera == True:
        print("Esta lloviendo o nevando en ", aux.info.pais)
    if bandera == True:
        print("Hay tormentas electricas o huracanes en ", aux.info.pais)
    aux = aux.sig

print("promedio de temperaturas",int(acum / cont))
