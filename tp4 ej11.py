from tda_lista_lista import Lista, insertar, eliminar, busqueda, barrido, barrido_con_sublista, tamanio, lista_vacia
from random import randint

def eliminar_anteultimo(lista,clave):
    cont = 0
    aux = lista.inicio
    c1 = str(clave)
    tam = tamanio(lista)-1
    while (aux is not None):
        n = str(aux.info.nombre)
        if (cont == tam-1):
            eliminar(lista,n,c1)
        cont += 1
        aux = aux.sig
    

class Personaje(object):
    
    def __init__(self,nombre,altura,edad,genero,especie,planetaNatal,episodioAparece):
        self.altura = altura
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.especie = especie
        self.planetaNatal = planetaNatal
        self.episodioAparece = episodioAparece
        
    def __str__(self):
        ret = ""
        for e in self.episodioAparece:
            ret += e
        return self.nombre +" "+ self.altura +" "+ self.edad +" "+ self.genero +" "+ self.especie +" "+ self.planetaNatal+" "+ret

starWars = Lista()
personaje1 = Personaje("Artud","60","801","masculino","Droide","Industria Autonoma",["1","2","3","4","5","6","7"])
insertar(starWars,personaje1,"nombre")
personaje1 = Personaje("Darth Vader","180","845","masculino","humano","Tatooine",["4","5","6"])
insertar(starWars,personaje1,"nombre")
personaje1 = Personaje("Han Solo","160","800","masculino","humano","Corelia",["2"])
insertar(starWars,personaje1,"nombre")
personaje1 = Personaje("Leia","150","815","femenino","humano","Alderaan",["1"])
insertar(starWars,personaje1,"nombre")
barrido(starWars)
'''
nombre = input("Nombre del personaje: ")
while (nombre != ""):
    altura = input("Ingrese altura: ")
    edad = input("Ingrese edad: ")
    genero = input("Ingrese genero (femenino, masculino, robot: ")
    especie = input("Ingrese Especie: ")
    planetaNatal = input("Ingrese planeta natal: ")
    #episodios = int(input("En cuantos episodios aparece: "))
    #for e in range(episodios):
     #   episodio = input("Numero del episodio: ")
      #  episodioAparece += episodio
    episodioAparece = []
    episodio = input("Episodio donde aparece: ")
    while (episodio != ""):
        episodioAparece += episodio
        episodio = input("Ingrese otro episodio donde aparece: ")
    personaje = Personaje(nombre,altura,edad,genero,especie,planetaNatal,episodioAparece)
    insertar(starWars,personaje,"nombre")
    nombre = input("Ingrese un personaje: ")
barrido(starWars)  
'''
print("")

aux = starWars.inicio
mayor = aux
while (aux is not None):
    if (aux.info.genero == "femenino"):
        print("Personaje feminino")        
        print(aux.info.nombre)
    control = False
    if (aux.info.especie == "Droide"):
        for e in aux.info.episodioAparece:
            if (int(e) < 7):
                control = True
    if (control == True):
        print("Droide encontrado en los primeros 6 episodios: ")
        print(aux.info)
    if (aux.info.nombre == "Darth Vader"):
        print("Vader esta en la lista : ")
        print(aux.info)
    if (aux.info.nombre == "Han Solo"):
        print("Informacion de Han Solo: ")
        print(aux.info)
    control2 = False
    for e in aux.info.episodioAparece:
        if (int(e)<=7):
            control2 = True
    if (control2 == True):
        print("Peronsaje que aprece en alguno de los primeros 7 episodios: ")
        print(aux.info)
    if (int(aux.info.edad) > 800):
        print("Personaje con mas de 800 anios.",aux.info.nombre)
    if (int(aux.info.edad) > 800 and int(aux.info.edad) > int(mayor.info.edad)):
        mayor = aux
    if (aux.info.especie == "humano" and aux.info.planetaNatal == "Alderaan"):
        print("Humano nacido en Alderan ",aux.info.nombre)
    if (int(aux.info.altura) < 70):
        print(aux.info.nombre, " su altura es menor de 70.")
#    for e in aux.info.episodioAparece:
#        if (int(e) == 7 or int(e) == 5 or int(e) == 4):
#            nom = aux.info.nombre
#            eliminar(starWars,nom,"nombre")
    aux = aux.sig
    
print(" ")            
barrido(starWars)
print("MARCA",mayor.info)
print(" ")
chu = []
ep = input("Chew aparece en el episodio: ")
while (ep != ""):
    chu += ep
    ep = str(input("Chewy aparece en el episodio: "))

personaje1 = Personaje("Chewbacca","230","101","masculino","Wookiee","Kashyyyk",chu)
insertar(starWars,personaje1,"nombre")
barrido(starWars)
print("Datos de chewbacca : ",busqueda(starWars,"Chewbacca","nombre").info)

eliminar_anteultimo(starWars,"nombre")
print(" ")
barrido((starWars))