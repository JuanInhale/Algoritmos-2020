class Cola():
    """TDA cola """

    def __init__(self):
        self.datos, self.frente, self.final, self.tamanio = [0] * 5, 0, -1, 0


def arribo(cola, dato):
    cola.final += 1 
    cola.datos[cola.final] = dato
    if(cola.final == len(cola.datos)-1):
        cola.final = -1
    cola.tamanio += 1

def atencion(cola):
    aux = cola.datos[cola.frente]
    cola.frente += 1
    if(cola.frente==len(cola.datos)):
        cola.frente = 0
    cola.tamanio -= 1
    return aux

def barrer(cola):
    aux = Cola()
    while (not cola_vacia(cola)):
        dato = atencion(cola)
        print(dato)
        arribo(aux,dato)
    while (not cola_vacia(aux)):
        datoaux = atencion(aux)
        arribo(cola,datoaux)

def barrer_pos(cola):
    aux = Cola()
    contador = 0
    while (not cola_vacia(cola)):
        contador += 1 
        dato = atencion(cola)
        print("Posicion: ",contador,", dato: ",dato)
        arribo(aux,dato)
    while (not cola_vacia(aux)):
        datoaux = atencion(aux)
        arribo(cola,datoaux)        
        
def cola_vacia(cola):
    return cola.tamanio == 0

def cola_llena(cola):
    return cola.tamanio == len(cola.datos)

def tamanio(cola):
    return cola.tamanio

def en_frente(cola):
    return cola.datos[cola.frente]

def mover_final(cola):
    x = atencion(cola)
    arribo(cola, x)
    return x