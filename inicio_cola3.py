from tda_cola_dinamica import Cola, mostrar_cola, cola_vacia, arribo, atencion, tamanio, en_frente, mover_final

# Dos colas ordenadas agregarlas a una

def ingresar_enteros(cola):
    while (tamanio(cola) < 2):
        num = input("numero ")
        arribo(cola,num)

cola1 = Cola()
cola2 = Cola()
cola3 = Cola()

print("numeros de cola1")
ingresar_enteros(cola1)
print("numeros de cola2")
ingresar_enteros(cola2)

# Funciona si estan ordenador de menor a mayor


while(not cola_vacia(cola1) or not cola_vacia(cola2)):
    if (not(cola_vacia(cola1))):   
        a = en_frente(cola1)
    else:
        a = 0
    if (not(cola_vacia(cola2))):
        b = en_frente(cola2)
    else:
        b = 0
    if int(a) >= int(b):
        arribo(cola3,atencion(cola1))
    else:
        arribo(cola3,atencion(cola2))
        
#    a = 0
#    b = 0
#    if not cola_vacia(cola1):
#        a = int(en_frente(cola1))
#    if not cola_vacia(cola1):
#        b = int(en_frente(cola2))
#    if a > b:
#        arribo(cola3,atencion(cola1))
#    elif( a == b):
#        arribo(cola3,atencion(cola2))
#        arribo(cola3,atencion(cola1))
#    else:
#        arribo(cola3,cola1)
    
mostrar_cola(cola3)

