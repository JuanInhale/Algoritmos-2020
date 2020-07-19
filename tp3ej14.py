from tda_cola_dinamica import Cola, mostrar_cola, cola_vacia, arribo, atencion, tamanio, en_frente, mover_final
from random import choice, randint

# Formato de los datos en la cola #@@@
# # == A,B,C,D,E,F 
# @@@ == 000 al 999

cola1 = Cola()

letras = ["A","B","C","D","E","F"]

for e in range(50):
    a = " "
    a = choice(letras) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
    print(a)
    arribo(cola1,a)



cont_A = 0
cont_B = 0
cont_C = 0
cont_D = 0
cont_E = 0
cont_F = 0

cola2 = Cola()
cola3 = Cola()    
while not cola_vacia(cola1):
    b = atencion(cola1)
    if b[0] == "A" or b[0] == "C" or b[0] == "F":
        arribo(cola2,b)
    if b[0] == "B" or b[0] == "D" or b[0] == "E":
        arribo(cola3,b)
    if b[0] == "A":
        cont_A += 1
    if b[0] == "B":
        cont_B += 1
    if b[0] == "C":
        cont_C += 1
    if b[0] == "D":
        cont_D += 1
    if b[0] == "E":
        cont_E += 1
    if b[0] == "F":
        cont_F += 1

print("Cantidad de A's",cont_A)
print("Cantidad de C's",cont_C)
print("Cantidad de F's",cont_F)
print(" ")
print("Cantidad de B's",cont_B)
print("Cantidad de D's",cont_D)
print("Cantidad de E's",cont_E)

tamanios = [cont_A,cont_C,cont_F]
tamanios2 = [cont_B,cont_D,cont_E]

def devolver_ACoD(mayor):
    if mayor == 0:
        print("A tiene mas turnos.")
    if mayor == 1:
        print("C tiene mas turnos.")
    if mayor == 2:
        print("F tiene mas turnos.")

def devolver_BEoF(mayor):
    if mayor == 0:
        print("B tiene mas turnos.")
    if mayor == 1:
        print("D tiene mas turnos.")
    if mayor == 2:
        print("E tiene mas turnos.")
      
def mayor(lista):
    mayor = [0,lista[0]]
    cont = 0
    for e in lista:
        if e > mayor[1]:
            mayor = [cont,e]
        cont += 1
    return mayor
    
print("Cola de A,C y F")
mostrar_cola(cola2)
print("Cola de B,D y E")
mostrar_cola(cola3)
print(" ")
if tamanio(cola2) > tamanio(cola3):
    print("Cola con A,C,F tiene mas turnos. ")
    print(" Cantidad de turnos: ",tamanio(cola2))
    devolver_ACoD(mayor(tamanios)[0])
    print("Con una cantidad de, ",mayor(tamanios)[1])
else:
    print("Cola con B,D,E tiene mas turnos. ")
    print(" Cantidad de turnos: ",tamanio(cola3))
    devolver_BEoF(mayor(tamanios2)[0])
    print("Con una cantidad de, ",mayor(tamanios2)[1])

print(" ")
if tamanio(cola2) < tamanio(cola3):
    print("Cola con A,C y F. Es la menor.")
    print("lista de turnos mayores a 506.")
    while not cola_vacia(cola2):
        a = atencion(cola2)
        n = int(a[1] + a[2] + a[3])
        if n > 506:
            print(a)
else:
    print("Cola con B,D y E. Es la menor.")
    print("lista de turnos mayores a 506.")
    while not cola_vacia(cola3):
        a = atencion(cola3)
        n = int(a[1] + a[2] + a[3])
        if n > 506:
            print(a)
    