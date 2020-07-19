from tda_tabla_hash import crear_tabla, agregar_ta, bernstein, cantidad_elementos_ta, hash_division

def decodificar(binario):
    t = len(binario) + 1
    a = binario[2:t]
    b = int(a,2)
    return b
    
        
mensaje = "!@#%^&*"
print("tamanio del mensaje, ",len(mensaje))
mensajes = crear_tabla(10)

mensajes_decodificados = crear_tabla(10)

for e in mensaje:
    print (e)
    a = ord(e)
    print(a)
    b = bin(a)
    print(b)
    agregar_ta(mensajes,bernstein,b)


print(mensajes)

for e in mensajes:
    if e:
        aux = e.inicio
        while aux:
            print(aux.info)
            f = decodificar(aux.info)
            print(f)
            agregar_ta(mensajes_decodificados,hash_division,f)
            aux = aux.sig
        print(" ")
        
print(mensajes_decodificados)
print(" ")

for r in mensajes_decodificados:
    if r:
        aux = r.inicio
        while aux:
            print(aux.info)
            aux = aux.sig
        print(" ")
        