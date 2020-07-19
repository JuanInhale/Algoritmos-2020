from tda_tabla_hash import crear_tabla, agregar_tc, hash_contactos, buscar_tc

class contacto(object):
    
    def __init__(self, nombreyapellido, email):
        self.nombreyapellido = nombreyapellido
        self.email = email
        
    def __str__(self):
        return self.nombreyapellido + " " + self.email

contactos = crear_tabla(10)

contacto1 = contacto("Jeremy Rock","JeremyKingOfGods@gmail.com")

agregar_tc(contactos,hash_contactos,contacto1)

posicion = buscar_tc(contactos,hash_contactos,contacto1)

print(contactos)

if contactos[posicion]:
    print(contactos[posicion])