from tda_tabla_hash import agregar_ta, agregar_ta_pokemon, agregar_tc, buscar_tc, crear_tabla, bernstein_pokemon, bernstein

class Pokemon(object):
    
    def __init__(self,nombre,nivel,tipo1,tipo2,numero):
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.numero = numero
        self.nombre = nombre
        self.nivel = nivel
        
    def __str__(self):
        return self.tipo1 + " " + self.tipo2 + " " + str(self.numero)

tipos = crear_tabla(15)

pokemon1 = Pokemon("Charizard",100,"electrico","fuego",1)

print(bernstein("Fuego", tipos))

agregar_tc(tipos,bernstein_pokemon,pokemon1)

print(tipos)




