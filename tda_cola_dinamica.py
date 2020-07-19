class nodoCola(object):
    """crea una variable nodo cola"""
    def __init__(self):
        self.info, self.sig = None, None

class Cola(object):
    """TDA cola """

    def __init__(self):
        self.frente, self.final, self.tamanio = None, None, 0


def arribo(cola, dato):
    nodo = nodoCola()
    nodo.info = dato
    if(cola.final is None):
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1

def atencion(cola):
    aux = cola.frente.info
    cola.frente = cola.frente.sig
    if(cola.frente is None):
        cola.final = None
    cola.tamanio -= 1
    return aux


def cola_vacia(cola):
    return cola.tamanio == 0

def mostrar_cola(cola):   
    colaaux = Cola()
    while (not cola_vacia(cola)):
        a = atencion(cola)        
        print(a)
        arribo(colaaux,a)
    while not cola_vacia(colaaux):
        b = atencion(colaaux)
        arribo(cola,b)

def tamanio(cola):
    return cola.tamanio

# Devuelve el dato pero no lo quita de la cola
def en_frente(cola):
    return cola.frente.info

def mover_final(cola):
    x = atencion(cola)
    arribo(cola, x)
    return x