from tda_cola_dinamica import Cola, mostrar_cola, cola_vacia, arribo, atencion, tamanio, en_frente, mover_final
from random import choice, randint

coches = ["automóvil","camioneta","camione","colectivo"]
tarifa = [47,59,71,64]

cola1 = Cola()
cola2 = Cola()
cola3 = Cola()

for e in range(30):
    a = randint(1,3)
    if a == 1:
        a = choice(coches)
        arribo(cola1,a)
    if a == 2:
        a = choice(coches)
        arribo(cola2,a)
    if a == 3:
        a = choice(coches)
        arribo(cola3,a)
        
def atender_coches(cola):
    cant_autos = 0
    cant_camionetas = 0
    cant_camiones = 0
    cant_colectivos = 0 
    recaudo = 0
    while not cola_vacia(cola):
        a = atencion(cola)
        if a == "automóvil":
            recaudo += 47
            cant_autos += 1
        if a == "camioneta":
            recaudo += 59
            cant_camionetas += 1
        if a == "camion":
            recaudo += 71
            cant_camiones += 1
        if a == "colectivo":
            recaudo += 64
            cant_colectivos += 1
    print("Cantidad de automoviles atendidos",cant_autos)
    print("Cantidad de camionetas atendidos",cant_camionetas)
    print("Cantidad de camiones atendidos",cant_camiones)
    print("Cantidad de colectivos atendidos",cant_colectivos)
    print("Cantidad recaudado",recaudo)

print("Cola1")
atender_coches(cola1)
print(" ")
print("Cola2")
atender_coches(cola2)
print(" ")
print("Cola3")
atender_coches(cola3)
print(" ")

