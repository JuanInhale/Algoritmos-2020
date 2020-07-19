from tda_tabla_hash import crear_tabla, agregar_tc, hash_diccionario,buscar_tc, agregar_ta, buscar_ta
from tda_lista import barrido

class Palabra(object):
    
    def __init__(self,palabra,significado):
        self.palabra = palabra
        self.significado = significado
        
    def __str__(self):
        
        return self.palabra.capitalize() + ". Significado : " + self.significado.capitalize()

# a b c d e f g h i j   k  l m   n  o  p q   r  s  t  u  v  w  x  y  z 
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

palabra1 = Palabra("a","letra")
palabra2 = Palabra("b","letra")
palabra3 = Palabra("aa","letra")
palabra4 = Palabra("aaa","letra")

diccionario = crear_tabla(26)
diccionario2 = crear_tabla(26)
'''
a = hash_diccionario(palabra1,diccionario)
b = hash_diccionario(palabra2,diccionario)
c = hash_diccionario(palabra3,diccionario)
d = hash_diccionario(palabra4,diccionario)

print(a)
print(b)
print(c)
print(d)
'''
agregar_ta(diccionario2,hash_diccionario,palabra1,"palabra")
agregar_ta(diccionario2,hash_diccionario,palabra2,"palabra")
agregar_ta(diccionario2,hash_diccionario,palabra3,"palabra")
agregar_ta(diccionario2,hash_diccionario,palabra4,"palabra")


cont = 0 
for e in diccionario2:
    print(cont)
    if e:
        aux = e.inicio
        while aux:
            print(aux.info)
            aux = aux.sig
    cont += 1
    
buscado = buscar_ta(diccionario2,hash_diccionario,palabra1,"palabra")
print(buscado.info)



