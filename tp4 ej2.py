from tda_lista import Lista, insertar, eliminar, busqueda, barrido, lista_vacia
from random import randint


lista = Lista()

for i in range(100):
    insertar(lista, chr(randint(65, 90)))


barrido(lista)

dato = eliminar(lista, 'A')
while(dato is not None):
    dato = eliminar(lista, 'A')

dato = eliminar(lista, 'E')
while(dato is not None):
    dato = eliminar(lista, 'E')

dato = eliminar(lista, 'I')
while(dato is not None):
    dato = eliminar(lista, 'I')

dato = eliminar(lista, 'O')
while(dato is not None):
    dato = eliminar(lista, 'O')

dato = eliminar(lista, 'U')
while(dato is not None):
    dato = eliminar(lista, 'U')
print()
barrido(lista)