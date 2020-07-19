from tda_tabla_hash import crear_tabla, agregar_tc,hash_diccionario2,cantidad_elementos_tc

def porcentaje(tot,n):
    result = (n * 100) / tot
    return int(result)
    

personajes =  crear_tabla(26)



starwars = ["achewy","bR2d2","cLuke","dleia","eObiwan","fchewy","gR2d2","hLuke","ileia","jObiwan","kchewy","lR2d2","mLuke","nleia","oObiwan","pchewy","qR2d2","rLuke","sleia","tObiwan"]

for e in starwars:
    agregar_tc(personajes,hash_diccionario2,e)
    porc = porcentaje(len(personajes),cantidad_elementos_tc(personajes))
    if (porc > 75):
        aux = personajes
        a = int (len(personajes) + (len(personajes) / 2))
        personajes = crear_tabla(a)
        for a in aux:
            if a:
                agregar_tc(personajes,hash_diccionario2,a)

print(porc)
    
print(len(personajes))
print(personajes)


#print(len(personajes))
#print(len(starwars))
#a = porcentaje(len(personajes),len(starwars))
#print(a)
#for e in starwars:
#    
#    agregar_tc(personajes,hash_diccionario,e)
#    if (porcentaje(len(personajes),cantidad_elementos_tc(personajes)) > 75):
#        extra = len(personajes) / 2        
#        crear_tabla(len(personajes) + extra)