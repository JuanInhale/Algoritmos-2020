from tda_lista import Lista, insertar, eliminar, busqueda, barrido, lista_vacia
from random import randint

lista1 = Lista()
for e in range(10):
    insertar(lista1,randint(1,100))

#barrido(lista1)

aux = lista1.inicio

while(aux is not None):
    pos = busqueda(lista1, aux.info)
    if(pos is not None):
        print(aux.info)
    aux = aux.sig

# Separar en dos listas los pares y los impares

lista_uno = Lista()
lista_par = Lista()
lista_impar = Lista()

for i in range(30):
    insertar(lista_uno, randint(0, 50))

#barrido(lista)

while(not lista_vacia(lista_uno)):
    dato = eliminar(lista_uno, lista_uno.inicio.info)
    if(dato % 2 == 0):
        insertar(lista_par, dato)
    else:
        insertar(lista_impar, dato)   
    
print("Par " )
barrido(lista_par)
print("Impar " )
barrido(lista_impar)

# Otra forma de separar en pares e impares.

lista2 = Lista()
lista_par2 = Lista()
lista_impar2 = Lista()

for i in range(30):
    insertar(lista2, randint(0, 50))
    
print("Barrido lista 2")    
barrido(lista2)

aux = lista2.inicio

while (aux is not None):
    if (aux.info % 2 == 0):
        insertar(lista_par2,aux.info)
    else:
        insertar(lista_impar2,aux.info)
    aux = aux.sig

print("Par " )
barrido(lista_par2)
print("Impar " )
barrido(lista_impar2)

# Eliminar las vocales de una lista de caracteres.

def cargarLetras(lista):
    for e in range(10):
        insertar(caract,chr(randint(97,123)))

def eliminarVocales(lista):
    aux = eliminar(lista,"a")
    while (aux is not None):
        aux = eliminar(lista,"a")
        
    aux = eliminar(lista,"e")
    while (aux is not None):
        aux = eliminar(lista,"e")
        
    aux = eliminar(lista,"i")
    while (aux is not None):
        aux = eliminar(lista,"i")
        
    aux = eliminar(lista,"o")
    while (aux is not None):
        aux = eliminar(lista,"o")
        
    aux = eliminar(lista,"u")
    while (aux is not None):
        aux = eliminar(lista,"u")
        

caract = Lista()
cargarLetras(caract)
barrido(caract)
eliminarVocales(caract)
print("after. ")
barrido(caract)

# elminar los numeros primos.
def cargarNumerosRand(lista):
    for e in range(10):
        insertar(lista,randint(1,10))

def NumerosPrimos(lista):
    aux = lista.inicio
    while (aux is not None):
        control = False
        for e in range(2,aux.info):
            if (aux.info % e == 0):
                control = True
        if control == True:
            eliminar(lista,aux.info)
        control = False
        aux = aux.sig

numeros = Lista()
cargarNumerosRand(numeros)
barrido(numeros)
NumerosPrimos(numeros)
print("Son primos")
barrido(numeros)

