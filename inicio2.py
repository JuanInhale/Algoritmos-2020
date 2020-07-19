from tda_cola_dinamica import Cola, cola_vacia, arribo, atencion, tamanio, en_frente, mover_final
from piladinamica import desapilar

#Personajes star wars
class Personaje(object):
    
    def __init__(self,nombre,planeta):
        self.nombre = nombre
        self.planeta = planeta
        
    def __str__(self):
        return self.nombre +" "+ self.planeta
        
star = Cola()
staraux = Cola()

personaje1 = Personaje("Luke Skywalker","Tatooine") 
arribo(star,personaje1)

personaje1 = Personaje("Darth","Tatooine") 
arribo(star,personaje1)

personaje1 = Personaje("Leia","Alderaan") 
arribo(star,personaje1)

personaje1 = Personaje("Jar Jar Binks","Naboo") 
arribo(star,personaje1)

personaje1 = Personaje("Duloks","Endor") 
arribo(star,personaje1)

personaje1 = Personaje("Yoda","Uknown") 
arribo(star,personaje1)



#for i in range(tamanio(star)):
#    atencion(star)

'''
while (not cola_vacia(star)):
    dato1 = atencion(star) 
    if (dato1.nombre == "Yoda"):
        nombre = input("Nombre ")
        planeta = input("Planeta ")
        personaje1 = Personaje(nombre.capitalize(),planeta.capitalize())
        arribo(staraux,personaje1)
    arribo(staraux,dato1)

print("Cola aux")
for i in range(tamanio(staraux)):
    per = atencion(staraux)
    print(per)
    arribo(star,per)
'''
#print("Cola star")
#for i in range(tamanio(star)):
#    print(atencion(star))
borra = 0 
cont = 0
while (not cola_vacia(star)):    
    dato = atencion(star)
    if (dato.nombre == "Jar Jar Binks"):
        borra = cont
    if (dato.planeta.capitalize() == "Alderan") or (dato.planeta.capitalize() == "Endor") or (dato.planeta.capitalize() == "Tatooine"):
        print("Alderan, Endor, Tatuine :",dato.nombre)
    if (dato.nombre == "Luke Skywalker"):
        print("Planera natal de Luke",dato.planeta)
    if (dato.nombre.capitalize() == "Darth"):
        print("Planeta natal de Darth: ",dato.planeta)
    if (dato.nombre == "Yoda"):
        nombre = input("Nombre ")
        planeta = input("Planeta ")
        personaje1 = Personaje(nombre.capitalize(),planeta.capitalize())
        arribo(staraux,personaje1)
    arribo(staraux,dato)    
    cont += 1    
    
print(borra," ",cont )

print("Cola aux")
for i in range(tamanio(staraux)-1):
    print(i)
    if i == borra+1:
        atencion(staraux)
    per = atencion(staraux)
    print(per)  
    arribo(star,per)
    

