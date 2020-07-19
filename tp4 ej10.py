from tda_lista_lista import Lista, insertar, eliminar, busqueda, barrido, barrido_con_sublista, tamanio, lista_vacia
from random import randint

# Canciones Spotify

class Cancion(object):
    
    def __init__(self, nombre, artista, duracion, ultimoMes):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion
        self.ultimoMes = ultimoMes
        
    def __str__(self):
        return self.nombre + ", " + self.artista

def unicaPalabra(palabra):
    control = False
    for e in range(len(palabra)):
        a  = palabra[e]
        if (a == " "):
            control = True
            break
    return control
    
canciones = Lista()

archivo = open("songs.txt")

linea =  archivo.readline()

while linea:
    linea = linea.split(";")
    linea[0] = linea[0].title()
    linea[1] = linea[1].title()
    linea[2] = int(linea[2])
    linea[3] = int(linea[3])
    cancion1 = Cancion(linea[0],linea[1],linea[2],linea[3])
    insertar(canciones,cancion1,"nombre")
    linea = archivo.readline()

'''
a = int(input("Cuantas canciones vas a ingresar?"))

for e in range(a):
    print("Ingrese una cancion: ")
    cancion = input("Cancion: ")
    artista = input("Artista: ")
    duracion = int(input("Duracion: "))
    ultimoMes = int(input("Reproducciones del ultimo mes: "))
    
    cancion1 = Cancion(cancion,artista,duracion,ultimoMes)    
    insertar(canciones,cancion1,"duracion")
'''
print("Lista de canciones.")  
print(barrido(canciones))
'''
aux = canciones.inicio
duraMayor = canciones.inicio
cont = 0
tam = canciones.tamanio
while (aux is not None):
#    if (a.duracion > duraMayor.duracion):
#        duraMayor = a    
#    aux = aux.sig
    top = int(input("Ingrese el top que desea mostrar: "))
    r = tam-top
    while (cont < r):
        print(a)
'''
aux = canciones.inicio
mayor = canciones.inicio
contador = 0
tam = int(canciones.tamanio)
print("En la lista hay, ",tam," canciones. Elija un top menor o igual a la cantidad de canciones en la lista.")
top = int(input("Ingrese el top de canciones mas escuchadas : "))
puesto = top + 1
while (aux is not None):
    if (aux.info.artista == "Artic Monkeys"):
        print("Cancion de Artic Monkeys: " , aux.info.nombre)    
    if (aux.info.duracion > mayor.info.duracion):
        mayor = aux
    if (unicaPalabra(aux.info.artista) == False):
        print("Grupo con una sola palabra en su nombre: " , aux.info.artista)
    #Cambiar el parametro de orden por cantidad de veces reproducidas
    r = (tam - top)
    if (contador >= r):
        puesto -= 1
        print ("Puesto :",puesto,aux.info)
    aux = aux.sig
    contador += 1
print("Cancion de mayor duracion" , mayor.info)

        