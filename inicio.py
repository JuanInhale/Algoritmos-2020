from tda_cola import Cola, arribo, atencion,cola_vacia,cola_llena, tamanio,barrer,barrer_pos ,en_frente, mover_final;
from pila import Pila, apilar, desapilar, pila_vacia, pila_llena,tamanio;
#from tda_cola_dinamica import Cola, cola_vacia, arribo, atencion, tamanio, en_frente, mover_final
# Eliminar vocales.
from random import randint

def noVocales(cola):
    colaaux = Cola()
    colaaux2 = Cola()
    while (not cola_vacia(cola)):
        a = atencion(cola)
        if ((a == "a") or (a == "i") or (a == "e") or (a == "o")or (a == "u")):
            arribo(colaaux,a)
        else:
            arribo(colaaux2,a)
    print(colaaux2.datos)   

def noVocales2(cola):
    colaaux = Cola()
    colaaux2 = Cola()
    while (not cola_vacia(cola)):
        a = ord(atencion(cola))
        print(a)
        if ((a == 97) or (a == 101) or (a == 105) or (a == 111)or (a == 117)):
            arribo(colaaux,chr(a))
        else:
            arribo(colaaux2,chr(a))
    print(colaaux2.datos)

def caracteresAleatorios(cola):
    while (not cola_llena(cola)):
        a = randint(97,122)
        arribo(cola,chr(a))
    
#caracteres = Cola()  
#caracteresAleatorios(caracteres)
#print(caracteres.datos)
#noVocales(caracteres)
#noVocales2(caracteres)

# Invertir una cola con pilas y colas.

def invertir(cola):
    pila1 = Pila()
    pilaInvertida = Pila()
    while not(cola_vacia(cola)):
        a = atencion(cola)
        apilar(pila1,a)
    while not(pila_vacia(pila1)):
        a = desapilar(pila1)
        apilar(pilaInvertida,a)
    return pilaInvertida
    #Devuelve una pila
'''
cola1 = Cola()
caracteresAleatorios(cola1)
print(cola1.datos)
print(invertir(cola1).datos)
'''
# Palindromo

def cargarCaracteres(cola):
    while (not cola_llena(cola)):
        a = input("Ingrese un caracter: ")
        arribo(cola,a)

def compararpilas(pila,pila2):
    igualdad = True
    if (tamanio(pila) == tamanio(pila2)):
        while (not pila_vacia(pila) and (igualdad == True)):
            a = desapilar(pila)
            b = desapilar(pila2)
            if (a == b):
                igualdad = True
                return igualdad
            else:
                igualdad = False
                return igualdad
    return igualdad
 
def invertirPila(pila):
    pilaux = Pila()    
    while(not pila_vacia(pila)):
        aux = desapilar(pila)
        apilar(pilaux,aux)
    return pilaux
 
def palindromo(cola):
    piladerecha = Pila()
    pilaizquierda = Pila()
    t = cola.tamanio
    cont = 0
    mitad = (t//2)
    while (not cola_vacia(cola)):
        a = atencion(cola)
        cont += 1
        if (t%2 == 0):
            if (cont <= mitad):
                apilar(piladerecha,a)
            elif (cont >= mitad+1):
                apilar(pilaizquierda,a)
        else:
            if (cont <= mitad):
                apilar(piladerecha,a)
            elif (cont >= mitad+2):
                apilar(pilaizquierda,a)
    print(piladerecha.datos)
    print(invertirPila(pilaizquierda).datos)
    if (compararpilas(pilaizquierda,piladerecha) == True):
        print("La palabra es palindroma.")
    else:
        print("La palabra no es palindroma.")
''''
cola1 = Cola()
cargarCaracteres(cola1)
print(cola1.datos)
palindromo(cola1)
'''
# Eliminar numeros primos

def cargarNumero(cola):
    while (not cola_llena(cola)):
        arribo(cola,randint(0,10))

def sinPrimos(cola):
    colaaux = Cola()
    while (not cola_vacia(cola)):
        control = False        
        a = atencion(cola)
        print(a)
        for e in range(2,a):
            print(a,"%",e)            
            resto = a % e
            print(resto)
        if (resto == 0):
            control = True
        if control == True:
            arribo(colaaux,a)
    print(colaaux.datos)

'''
colaNumeros = Cola()
cargarNumero(colaNumeros)
print(colaNumeros.datos)
sinPrimos(colaNumeros)
'''
#control = False
#a = 6
#for e in range(2,a):
#    print(a,"%",e)            
#    resto = a % e
#    print(resto)
#    if (resto == 0):
#        control = True              
#if control == True:
#    print("Es no primo.")
#else:
#    print("Es primo.")

# Ejercicio 6 - Contar ocurrencias sin auxiliar.
'''
cola1 = Cola()

for e in range(10):
    arribo(cola1,randint(0,10))

barrer(cola1)

buscado = int(input("Buscar ocurrencias de dato:"))
cont = 0
while (not cola_vacia(cola1)):
    dato = atencion(cola1)
    if dato == buscado:
        cont += 1

print(cont)
'''
#Eliminar en la posicion
'''
def eliminar_inesimo(cola,pos):
    aux = Cola()
    contador = 1
    while (not cola_vacia(cola)):
        if (contador != pos):
            dato = atencion(cola)
            print(dato)
            arribo(aux,dato)
        elif(contador == pos):
            dato2 = atencion(cola)
            print("Posicion :",contador,", borrando ",dato2)
        contador += 1
    while (not cola_vacia(aux)):
        datoaux = atencion(aux)
        arribo(cola,datoaux) 
        
cola1 = Cola()
for e in range(10):
    arribo(cola1,randint(0,10))

print(" 2 paso")
barrer_pos(cola1)
    
print(" 2 paso")
eliminar_inesimo(cola1,2)

print("3 paso")
barrer(cola1)
'''
# Ordenar los elementos que se van agregarndo a una cola.
# usar una cola aux
'''
cola1 = Cola()
cola2 = Cola()


for e in range(5):
    midato = int(input("dato"))
    if cola_vacia(cola1):
        arribo(cola1,midato)
    else:
        while(not cola_vacia(cola1)):
            dato = atencion(cola1)
            if (dato < midato):
                arribo(cola2,dato)
            elif(dato >= midato or cola_vacia(cola1)):
                print(dato)
                arribo(cola1,dato)
                break
        arribo(cola1,midato)
        while(not cola_vacia(cola2)):
            dato2 = atencion(cola2)
            arribo(cola1,dato2)
            
print("cola1")
barrer(cola1)
print("cola2")         
barrer(cola2)   
'''
#Rango
#Elementos negativos
'''
cola1 = Cola()
for e in range(10):
    arribo(cola1,randint(0,10))
'''
# Prueba de codigo walter
# Se usan las colas dinamicas
'''
cola1 = Cola()
cola2 = Cola()
print('cargar cola 1')
while tamanio(cola1)<5:
    dato = int(input("ingrese un número"))
    arribo(cola1, dato)
print('cargar cola 2')
while tamanio(cola2)<7:
    dato = int(input("ingrese un número"))
    arribo(cola2, dato)
#c1 0 1 3 4 5 34 60 67
#c2 99
# itereaciones 4-4
cant = tamanio(cola1)
for i in range (0, cant):
    if(en_frente(cola1)< en_frente(cola2)):
        mover_final(cola1)
    else:
        #dato1 = atencion(cola1)
        while(en_frente(cola1)>en_frente(cola2)):
            dato = atencion(cola2)
            arribo(cola1, dato)
        mover_final(cola1)
        
while(not cola_vacia(cola2)):
    dato = atencion(cola2)
    arribo(cola1, dato)
    
for i in range(0, tamanio(cola1)):
    print(mover_final(cola1))    
    '''
# Rango. Hallar mayor, menor y restarlos.
'''
cola1 = Cola()

for e in range (5):
    num = randint(-10,10)
    arribo(cola1,num)
    print(num)
    

a = atencion(cola1)
maxi = a
mini = a  
cont = 0
arribo(cola1,a)
while (not cola_vacia(cola1)):
    a = atencion(cola1)
    if a < 0:
        cont += 1
    if a > maxi:
        maxi = a
    if a < mini:
        mini = a
    print(a)

    
rango = maxi - mini

print("numeros negativos",cont)
print("rango",rango)
print("minimo",mini)
print("maximo",maxi)
'''
