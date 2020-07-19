from tda_tabla_hash import crear_tabla, agregar_ta, hash_guia
from tda_lista import barrido

class Telefono(object):
    
    def __init__(self,telefono,apellido,nombre,direccion):
        self.telefono = telefono
        self.apellido = apellido
        self.nombre = nombre
        self.direccion = direccion
        
    def __str__(self):
        return self.apellido + " " + self.nombre + ". Direccion: " + self.direccion + ". Telefono: " + str(self.telefono)
      
guia = crear_tabla(10)

telefono1 = Telefono(562385,"Fort","Ricardo","Maiameee")
telefono2 = Telefono(572385,"Saitama","Sensei","One Punch")

print(hash_guia(telefono1,guia))

agregar_ta(guia,hash_guia,telefono1,"telefono")
agregar_ta(guia,hash_guia,telefono2,"telefono")

posicion = hash_guia(telefono1,guia)

if guia[posicion]:
    barrido(guia[posicion])



