from tda_tabla_hash import crear_tabla, buscar_ta, agregar_ta, hash_cifrado, bernstein_palabra
from tda_lista import barrido

class Palabra(object):
    
    def __init__(self,palabra,significado):
        self.palabra = palabra
        self.significado = significado
        
    def __str__(self):
        return self.palabra + " " + self.significado
        
tabla1 = crear_tabla(10)

tabla2 = crear_tabla(10)

# Desifrar usando un diccionario
def desifrar(dato):
    diccionario = {"#?&" : "0","abc": "1","def": "2","ghi": "3","jkl": "4","mnñ": "5","opq": "6","rst": "7","uvw": "8","xyz": "9"}    
    cadena = ''
    for i in range(0,len(dato),3):
        cadena += diccionario[dato[i:i+3]]
        #print(dato[i:i+3])
    # print (chr(int(cadena)))
    return chr(int(cadena))
    
def cifrar(dato):
    valor = str(ord(dato))
    # 65 6 
    valor_cifrado = ["#?&","abc","def","ghi","jkl","mnñ","opq","rst","uvw","xyz"]
    
    cadena = ""
    for num in valor:
        numInt = int(num)
        cadena += valor_cifrado[numInt]
    cadena += "%"
    return cadena
    
a = "Nueva cadena"
a_cifrado = ""

# Obtengo una lista cifrada en el orden y en la tabla se guardan los 
# caracteres con su respectivo cifrado.

for letra in a:
    valor = buscar_ta(tabla1,hash_cifrado,Palabra(letra,""),"palabra")
    cifrado = ""
    if (valor is None):
        cifrado = cifrar(letra)
        dato = Palabra(letra,cifrado)
        agregar_ta(tabla1,hash_cifrado,dato,"palabra")
    else:
        cifrado = valor.info.significado
    a_cifrado += cifrado

# Mostrar tabla1
print("tabla1")
for e in tabla1:
    if e:
        barrido(e)
print(" ")

'''
for e in tabla1:
    if e is not None:
        aux = e.inicio
        while aux:
            print(aux.info)
            aux = aux.sig
'''
# Mensaje cifrado
print("Mensaje cifrado")
print(a_cifrado)

#Se limpia la lista de los % y el espacio del final
lista = a_cifrado.split("%")
print(lista)
lista.pop()
print(lista)

cadena2 = ""
for e in lista:
    valor  = buscar_ta(tabla2,bernstein_palabra,Palabra(e,""),"palabra")
    desifrado = ""
    if (valor is None):
        desifrado = desifrar(e)
        palabra1 = Palabra(e,desifrado)
        agregar_ta(tabla2,bernstein_palabra,palabra1,"palabra")
    else:
        desifrado = valor.info.significado
    cadena2 += desifrado

print(cadena2)

for e in tabla2:
    if e:
        barrido(e)
        
