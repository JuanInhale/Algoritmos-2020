from tda_lista_lista import Lista, insertar, eliminar, busqueda, barrido, barrido_con_sublista, tamanio, lista_vacia
from random import randint

def eliminar_anteultimo(lista,clave):
    cont = 0
    aux = lista.inicio
    c1 = str(clave)
    while (aux is not None):
        n = str(aux.info.nombre)
        if (cont == lista.info.tamanio-1):
            eliminar(lista,n,c1)
        cont += 1
        aux = aux.sig
    