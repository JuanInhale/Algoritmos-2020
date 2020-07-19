from tda_cola_dinamica import Cola, mostrar_cola, cola_vacia, arribo, atencion, tamanio, en_frente, mover_final
from random import randint
# Generar una cola de 5000 caracteres y digitos.

cola1 = Cola()

# Cola de digitos
cola2 = Cola()
#Cola de caracteres
cola3 = Cola()

for e in range(50000):
    arribo(cola1,chr(randint(0,255)))

print(tamanio(cola1))
cont_caract = 0
resto = 0
while not cola_vacia(cola1):
    a = ord(atencion(cola1))
    if a > 47 and a < 58:
        b = chr(a)
        arribo(cola2,b)
        resto += 1
    else:
        if a == 35 or a == 63:
            print("existe el caracter",chr(a)) 
        if a > 64 and a < 91:
            cont_caract += 1
        elif a > 96 and a < 123:
            cont_caract += 1
        else:
            resto += 1
        c = chr(a)
        arribo(cola3,c)

print("Cantidad de caracteres en la cola ",cont_caract)
print(resto)

#print("cola de digitos")
#mostrar_cola(cola2)
#
#print("cola de caracteres")
#mostrar_cola(cola2)

