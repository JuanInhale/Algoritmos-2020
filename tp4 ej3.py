from tda_lista import Lista, insertar, eliminar, busqueda, barrido, lista_vacia
from random import randint

lista_uno = Lista()
lista_dos = Lista()

for i in range(10):
    insertar(lista_uno, randint(0, 50))

for i in range(43):
    insertar(lista_dos, randint(0, 50))

aux = lista_uno.inicio
barrido(lista_uno)

while(aux is not None):
    pos = busqueda(lista_dos, aux.info)
    if(pos is not None):
        print(aux.info)
    aux = aux.sig



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

aux = lista_uno.inicio
while (aux is not None):
    if(aux.info % 2 == 0):
        insertar(lista_par, aux.info)
    else:
        insertar(lista_impar, aux.info)
    aux= aux.sig

print('par')
barrido(lista_par)
print('impar')
barrido(lista_impar)