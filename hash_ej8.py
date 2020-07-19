from tda_tabla_hash import crear_tabla, agregar_ta, hash_diccionario2, hash_mensaje
from tda_lista import barrido

class Mensaje(object):
    
    def __init__(self,mensaje,posicion):
        self.mensaje = mensaje
        self.posicion = posicion

    def __str__(self):
        return self.mensaje
        
def codificar(caracter):
    a = ord(caracter)
    e = str(a)
    final = ""
    for b in e:
        if (b == "1"):
            final += "abd"
        elif (b == "2"):
            final += "def"
        elif (b == "3"):
            final += "ghi"
        elif (b == "4"):
            final += "jkl"
        elif (b == "5"):
            final += "mnñ"
        elif (b == "6"):
            final += "opq"
        elif (b == "7"):
            final += "rst"
        elif (b == "8"):
            final += "uvw"
        elif (b == "9"):
            final += "xyz"
        elif (b == "0"):
            final += "#?&"
    final +="%"
    return final
    


def decodificar(cadena):
    a = 0
    b = 0
    final = ""
    while a < len(cadena)-3:
        b = a +3    
        caracter = cadena[a:b]
        a += 3
        if caracter == "abd":
            final += "1"
        elif caracter == "def":
            final += "2"
        elif caracter == "ghi":
            final += "3"
        elif caracter == "jkl":
            final += "4"
        elif caracter == "mnñ":
            final += "5"
        elif caracter == "opq":
            final += "6"
        elif caracter == "rst":
            final += "7"
        elif caracter == "uvw":
            final += "8"
        elif caracter == "xyz":
            final += "9"
        elif caracter == "#?&":
            final += "0"
    return final

def guardar_mensaje(msje,tabla,tabla2):
    for e in mensaje:
        f = codificar(e)
        agregar_ta(tabla2,hash_diccionario2,f)
        agregar_ta(tabla,hash_diccionario2,e)
        
def guardar_mensaje_clase(msje,tabla):
    cont = 0
    for e in mensaje:
        f = codificar(e)
        print(f)
        mensaje1 = Mensaje(f,cont)
        agregar_ta(tabla,hash_mensaje,mensaje1) 
        cont += 1

def mostrar_tabla(tabla):
    res = ""       
    for f in tabla:
        if f:
            aux = f.inicio
            while aux:
                print(aux.info)
                print(decodificar(aux.info))
                asci = int(decodificar(aux.info))
                print(chr(asci))
                res += chr(asci)
                aux = aux.sig
    print( res)

def mostrar_tabla_clase(tabla):
    res = ""       
    for f in tabla:
        if f:
            aux = f.inicio
            while aux:
                print(aux.info.mensaje)
                print(decodificar(aux.info.mensaje))
                asci = int(decodificar(aux.info.mensaje))
                print(chr(asci))
                res += chr(asci)
                aux = aux.sig
    print( res)

mensaje = "Salvad al droid, porfavor."
code = crear_tabla(len(mensaje))
encode = crear_tabla(len(mensaje) * 6)         
encode2 = crear_tabla(len(mensaje) * 6)


#guardar_mensaje(mensaje,code,encode)
guardar_mensaje_clase(mensaje,encode2)

#mostrar_tabla(encode)
mostrar_tabla_clase(encode2)


#print(code)
#print(" ")
#print(decode)

#for e in code:
#    if e :
#        barrido(e)
#        print(" ")

        
