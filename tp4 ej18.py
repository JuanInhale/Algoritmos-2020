from tda_lista_lista import Lista, insertar, eliminar, busqueda, barrido, barrido_con_sublista, tamanio, lista_vacia
from random import randint
from datetime import datetime

class Usuario(object):
    
    def __init__(self,nombre):
        self.nombre = nombre
    
    def __str__(self):
        return "Usuario de git: "+ self.nombre
        
class Commit(object):
    
    def __init__(self,timestamp,commit,archivoModificado,cantLineas):
        self.timestamp = timestamp
        self.commit = commit
        self.archivoModificado = archivoModificado
        self.cantLineas = cantLineas
    
    def __str__(self):
        fecha1 = self.timestamp.strftime("%m/%d/%Y, %I:%M")
        return "Nombre del archivo: "+self.archivoModificado + '\n' +"Comenarios: "+  self.commit + '\n' + "Cantidad de lineas cambiadas: "+ str(self.cantLineas) +'\n'+"Fecha de modificacion: "+ fecha1

def inicializar(lista):
# Ingresar datos de un usuario
    usuariogit1 = Usuario("Rafael")
    insertar(lista,usuariogit1,"nombre")
    
    #commists = Lista()
    aux1 = busqueda(lista,"Rafael","nombre")
    
    fecha1 = datetime(2019,12,3,22,25)
    commit1 = Commit(fecha1,"Agrego una tabla hash","test.py",30)
    insertar(aux1.sublista,commit1,"archivoModificado")
    fecha1 = datetime(2020,1,13,15,0)
    commit1 = Commit(fecha1,"Implementacion de una lista","Animales.py",100)
    insertar(aux1.sublista,commit1,"archivoModificado")
    
# Ingresar datos de un usuario   
    usuariogit1 = Usuario("Marcela")
    insertar(lista,usuariogit1,"nombre")
    
    #commists = Lista()
    aux1 = busqueda(lista,"Marcela","nombre")  
    
    fecha1 = datetime(2019,9,3,20,30)
    commit1 = Commit(fecha1,"Borrados los archivos viejos","Personas",-30)
    insertar(aux1.sublista,commit1,"archivoModificado")
    fecha1 = datetime(2020,2,18,18,15)
    commit1 = Commit(fecha1,"Implementacion busqueda por razas","Animales",100)
    insertar(aux1.sublista,commit1,"archivoModificado")
    fecha1 = datetime(2020,1,1,20,10)
    commit1 = Commit(fecha1,"shuffle los animales","Animales",1)
    insertar(aux1.sublista,commit1,"archivoModificado")
    barrido_con_sublista(lista)

def mayorCommits(lista): # Usuario que tenga mas commits
    aux = lista.inicio
    valormaximo = 0
    while (aux is not None):
        if (tamanio(aux.sublista) > valormaximo):
            valormaximo = tamanio(aux.sublista)
        aux = aux.sig
    aux2 = lista.inicio
    while (aux2 is not None):
        if (tamanio(aux2.sublista) == valormaximo):
            print(aux2.info, " mayor cantidad de commits: ",str(valormaximo))
        aux2 = aux2.sig
    
   
# esta en git   
def cantidadLineas(lista): # mayor y menor cantidad de lineas 
    aux = lista.inicio
    while (aux is not None):
        sub = aux.sublista.inicio        
        contadorLineas = 0
        while (sub is not None):
            contadorLineas += sub.info.cantLineas
            sub = sub.sig
        print(contadorLineas, aux.info.nombre)
        aux = aux.sig

def testpy(lista):
    aux = lista.inicio
    while (aux is not None):
        sub = aux.sublista.inicio
        while(sub is not None):
            if (sub.info.archivoModificado == "test.py"):
                print(aux.info)
                print(sub.info)
            sub = sub.sig
        aux = aux.sig

def testpy2(lista):
    aux = lista.inicio
    while (aux is not None):
        pos = busqueda(aux.sublista,"test","archivo")
        if(pos is not None):
            print(aux.info)
        aux = aux.sig

    

usuarios = Lista()
inicializar(usuarios)
mayorCommits(usuarios)
cantidadLineas(usuarios)
testpy(usuarios)