from tda_cola_dinamica import Cola, mostrar_cola, cola_vacia, arribo, atencion, tamanio, en_frente, mover_final

class personaje_marvel(object):
    
    def __init__(self,nombre,nombrepersonaje,genero):
        self.nombre = nombre
        self.nombrepersonaje = nombrepersonaje
        self.genero = genero
    
    def __str__(self):
        return self.nombre + " " + self.nombrepersonaje + " " + self.genero
        
cola1 = Cola()

personaje1 = personaje_marvel("Scott Lang","Ant Man","M")
arribo(cola1,personaje1)

personaje1 = personaje_marvel("Brie Larson","Capitan Marvel","M")
arribo(cola1,personaje1)

personaje1 = personaje_marvel("Tony Stark","Iron Man","M")
arribo(cola1,personaje1)

personaje1 = personaje_marvel("Steve Rogers","Capitan America","M")
arribo(cola1,personaje1)

personaje1 = personaje_marvel("Natasha Romanoff","Black Widow","F")
arribo(cola1,personaje1)

personaje1 = personaje_marvel("Wanda Maximoff","Scarlet Witch","F")
arribo(cola1,personaje1)

personaje1 = personaje_marvel("Ororo Monroe","Storm","F")
arribo(cola1,personaje1)

while not cola_vacia(cola1):
    a = atencion(cola1)
    aux = False
    if a.nombrepersonaje == "Capitan Marvel":
        print("Capitan marvel su nombre es",a.nombre)
    if a.genero == "F":
        print("Personaje femenino",a)
    if a.genero == "M":
        print("Personaje masculino",a)
    if a.nombre == "Scott Lang":
        print("El personaje de Scott Lang es ", a.nombrepersonaje)
    if a.nombrepersonaje[0] == "S":
        print("Personaje que su nombre empieza con S :",a.nombrepersonaje)
    if a.nombre == "Carol Danvers":
        print("Carol Danvers se encuentra en la lista y su personaje es ", a.nombrepersonaje)
    else:
        aux = True
if aux == True:
    print("Carol Danvers no se encuentra en la lista.")