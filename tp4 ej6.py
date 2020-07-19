from tda_lista_2 import Lista, insertar, eliminar, busqueda, barrido, lista_vacia
from random import randint

# Super heros
class Heroe(object):

    def __init__(self,nombre,casa,anio,biografia):
        self.nombre = nombre
        self.casa = casa
        self.anio = anio
        self.biografia = biografia
        
    def __str__(self):
        return self.nombre+" "+self.casa+" "+str(self.anio)+" "+self.biografia

listaHeroes = Lista()

heroe = Heroe("Linterna Verde","Marvel",1963,"Usa un traje verde. ")
insertar(listaHeroes,heroe,"anio")
heroe = Heroe("Wolvering","Marvel",1999,"Es un x-men con garras de acero. ")
insertar(listaHeroes,heroe,"anio")
heroe = Heroe("Dr. Strange","DC",1998,"Tiene super super poderes. ")
insertar(listaHeroes,heroe,"anio")
heroe = Heroe("Iron Man","DC",1970,"Usa una armadura poderosa. ")
insertar(listaHeroes,heroe,"anio")
heroe = Heroe("Capitan Marvel","Marvel",1960,"Es el capitan de los marvel. ")
insertar(listaHeroes,heroe,"anio")
heroe = Heroe("Mujer Maravilla","DC",1963,"Es una mujer con un latigo poderoso. ")
insertar(listaHeroes,heroe,"anio")
heroe = Heroe("Flash","Marvel",2001,"Es muy rapido. ")
insertar(listaHeroes,heroe,"anio")
heroe = Heroe("Star Lord","Marvel",1965,"Es poderoso. ")
insertar(listaHeroes,heroe,"anio")
heroe = Heroe("SpiderMan","Marvel",1963,"Tiene poderes y traje de arania. ")
insertar(listaHeroes,heroe,"anio")
heroe = Heroe("Batman","Marvel",1963,"Tiene poderes y traje de murcielago. ")
insertar(listaHeroes,heroe,"anio")
barrido(listaHeroes)

eliminar(listaHeroes,"Linterna Verde","nombre")
barrido(listaHeroes)

aux = listaHeroes.inicio
while (aux is not None):
    if (aux.info.nombre == "Wolvering"):
        print(aux.info.anio)
    aux = aux.sig

data = eliminar(listaHeroes,"Dr. Strange","nombre")
data.casa = "Marvel"
print(data.casa)
insertar(listaHeroes,data,"anio")
barrido(listaHeroes)

aux = listaHeroes.inicio
while (aux is not None):
    a = -1
    b = -1    
    cadena = aux.info.biografia
    #print(cadena)
    tam = len(cadena)
    a = cadena.find("traje")
    if (a > -1):
        print(aux.info.nombre+" Usa traje")
    b = cadena.find("armadura")
    if (b > -1):
        print(aux.info.nombre+" Usa armadura")
    aux = aux.sig

print("Estrenos en 1963. ")
aux = listaHeroes.inicio
while (aux is not None):
    if (aux.info.anio == 1963):
        print(aux.info.nombre)
    aux = aux.sig
    
aux1 = busqueda(listaHeroes,"Mujer Maravilla","nombre")
print(aux1.info.casa)
aux1 = busqueda(listaHeroes,"Capitan Marvel","nombre")
print(aux1.info.casa)

aux1 = busqueda(listaHeroes,"Flash","nombre")
print(aux1.info)

aux1 = busqueda(listaHeroes,"Star Lord","nombre")
print(aux1.info)

aux = listaHeroes.inicio
cont = 0
cont2 = 0
while (aux is not None):
    if (aux.info.casa == "DC"):
        cont +=1
    else:
        cont2 +=1
    aux = aux.sig
print("La casa DC tiene ", cont)
print("La casa Marvel tiene ", cont2)

aux = listaHeroes.inicio
while (aux is not None):
    if (aux.info.nombre[0] == "S" or aux.info.nombre[0] == "B" or aux.info.nombre[0] == "M"):
        print("Su nombre empieza con S, M or B",aux.info.nombre)   
    aux = aux.sig

