from tda_tabla_hash import crear_tabla

def complemento(caracter):
    if caracter <= 78:
        return 79 + caracter -32
    elif caracter > 78:
        return 32 + caracter - 79

def codificar(caracter):
    a = ord(caracter)
    comp = complemento(a)
    four = str(a * 37)
    res = ""
    r = 0 
    for e in four:
        r = int (e) ** 2 + comp
        res += chr(r)
    res += chr(comp)
    return res

def decodificar_caracteres(caracter):
    # complemento en la posicion del final
    a = ord(caracter[4])
    print(a)
    # for e in caracter:
     
def separar_caracteres(listaencriptada):
    contador = 0
    contador2 = 0 
    vec = []
    car = ""
    while contador < len(listaencriptada):    
        
        for e in lista:
            if contador > 5:
                break
            contador += 1
            contador()
 

print(codificar("R"))

lista = "1ion!#$qw#$123qwe!#!e"