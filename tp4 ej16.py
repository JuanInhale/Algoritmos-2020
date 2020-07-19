from tda_lista_lista import Lista, insertar, eliminar, busqueda, barrido, barrido_con_sublista, tamanio, lista_vacia
from random import randint
import time
from datetime import datetime, date

class Actividad(object):

    def __init__(self,costo,tiempoEjecucion,fechaInicio,fechaFinEstimada,fechaFinEfectiva,personaAcargo):
        self.costo = costo
        self.tiempoEjecucion = tiempoEjecucion
        self.fechaInicio = fechaInicio
        self.fechaFinEstimada = fechaFinEstimada
        self.fechaFinEfectiva = fechaFinEfectiva
        self.personaAcargo = personaAcargo
    
    def __str__(self):
        print("Persona a cargo: ",self.personaAcargo)
        print("Fecha inicio: ",self.fechaInicio)
        print("Fecha estimada: ",self.fechaFinEstimada)
        print("Fecha efectiva: ",self.fechaFinEfectiva)
        return "$" + str(self.costo) + ". Tiempo ejecucion " + str(self.tiempoEjecucion) + " meses." 
    
def inicializarActividades(lista):
    
    actividad1 = Actividad(1500,5,date(2020,5,26),date(2020,10,20),date(2020,11,20),"Silvia")
    insertar(actividades,actividad1,"personaAcargo")
    actividad1 = Actividad(800,2,date(2020,5,26),date(2020,8,28),date(2020,7,28),"Pedro")
    insertar(actividades,actividad1,"personaAcargo")
#    actividad1 = Actividad(250,2,time.strftime("1/7/2020"),time.strftime("1/9/2020"),time.strftime("10/10/2020"),"Jose")
#    insertar(actividades,actividad1,"personaAcargo")
#    actividad1 = Actividad(2000,3,time.strftime("30/9/2020"),time.strftime("30/11/2020"),time.strftime("30/12/2020"),"Fede")
#    insertar(actividades,actividad1,"personaAcargo")
#    actividad1 = Actividad(180,7,time.strftime("1/6/2020"),time.strftime("1/1/2021"),time.strftime("1/2/2021"),"Juan")
#    insertar(actividades,actividad1,"personaAcargo")
'''
def basico(lista):
    aux = actividades.inicio
    while (aux is not None):

        aux = aux.sig

    return 
'''
def promedio(lista):
    aux = actividades.inicio
    promedio = 0
    cont = 0
    while (aux is not None):
        promedio += aux.info.tiempoEjecucion
        cont += 1
        aux = aux.sig
    promedio = promedio // cont
    return promedio

def costoTotal(lista):
    aux = actividades.inicio
    tot = 0
    while (aux is not None):
        tot += aux.info.costo
        aux = aux.sig
    return tot

def buscarPersona(lista):
    aux = actividades.inicio
    personal = input("Ingrese un empleado para mostrar sus datos: ")
    while (aux is not None):
        if (aux.info.personaAcargo == personal):
            emp = busqueda(lista,personal,"personaAcargo")
            print(emp.info)
        aux = aux.sig 

def entreDosFechas(lista):
    print("Mostrar las tareas que se realizan entre dos fechas.")
    print("Ingrese datos primera fecha. ")
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    anio = int(input("Anio: "))
    fecha1 = date(anio,mes,dia)
#    print("Fecha ingresada",fecha1)
    print("Ingrese datos segunda fecha. ")
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    anio = int(input("Anio: "))
    fecha2 = date(anio,mes,dia)
#    print("Fecha ingresada", fecha2)
#    if (fecha1 > fecha2):
#        print(fecha1," es mayor que ",fecha2)
#    else:
#        print(fecha2," es mayor ",fecha1)
    aux = lista.inicio
    while (aux is not None):
        if (aux.info.fechaInicio > fecha1 and aux.info.fechaInicio < fecha2):
            print(aux.info)
        aux = aux.sig
        
def tareasEnTiempo(lista):
    aux = lista.inicio
    while (aux is not None):
        if (aux.info.fechaFinEstimada > aux.info.fechaFinEfectiva):
            print("Fue entregada en tiempo.")
            print(aux.info)
            print(" ")
        else:
            print("No fue entregada a tiempo.")
            print(aux.info)
            print(" ")
        aux = aux.sig
        
actividades = Lista()
inicializarActividades(actividades)
barrido(actividades)
print("Tiempo promedio de tareas: ", promedio(actividades)," Horas")
print("Costo total del proyecto: $",costoTotal(actividades))
print(buscarPersona(actividades))
#entreDosFechas(actividades)
tareasEnTiempo(actividades)