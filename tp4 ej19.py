from tda_lista_lista import Lista, insertar, eliminar, busqueda, barrido, barrido_con_sublista, tamanio

class Venta(object):
    
    def __init__(self,codigo,producto,precio,reciclado,comprador):
        self.codigo = codigo
        self.producto = producto
        self.precio = precio
        self.reciclado = reciclado
        self.comprador = comprador
    
    def __str__(self):
        if self.reciclado == True:
            print("Producto con partes recicladas.")
        else:
            print("Producto sin partes recicladas")
        pre = str(self.precio)
        return self.codigo + " " + self.comprador  + " $ " + pre  + " " + self.producto

def agregar_sinrepetir(lista,nombre):
    if not lista:
        lista.append(nombre)
    else:
        control = False
        for e in lista:
            if nombre == e:
                control = True
        if control == False:
            lista.append(nombre)
            
        
lista1 = Lista()
lista2 = Lista()
lista3 = Lista()
lista4 = Lista()

archivo = open("ventas.txt")
a = "Desconocido"
linea = archivo.readline()

#01;TIE;5000;True;Jar Jar Bins 
#codigo; NombreProducto; integer precio; buleano Reciclado; Nombre compador

while linea:
    print("EEEEE",linea)
    linea = linea.split(";")
    linea[0] = linea[0].title() # title sirve para poner el primer caracter de un string en mayuscula y el resto en minuscula.
    linea[1] = linea[1]
    linea[2] = int(linea[2])
    if linea[3].title() == "True":
        linea[3] = True
    elif linea[3].title() == "False":
        linea[3] = False
    else:
        break
    linea[4] = linea[4].title().strip()
    venta1 = Venta(linea[0],linea[1],linea[2],linea[3],linea[4])
    if linea[4].strip() == "Desconocido":
        insertar(lista1,venta1,"codigo")
    else:
        insertar(lista2,venta1,"codigo")
    linea = archivo.readline()
    
print("Lista con compradores desconocidos")
barrido(lista1)
print(" ")
print("Lista con compradores conocidos")
barrido(lista2)           

compradores = []
total = 0
unidades_vendidas = 0
ganancia_AT = 0

aux = lista1.inicio
while(aux is not None):
    total += aux.info.precio
    unidades_vendidas += 1
    a = aux.info.producto.find("AT")
    if a != -1:
        ganancia_AT += aux.info.precio
    aux = aux.sig
    
    
aux = lista2.inicio   
while(aux is not None):
    total += aux.info.precio
    unidades_vendidas += 1
    agregar_sinrepetir(compradores,aux.info.comprador)
    if aux.info.comprador == "Darth Vader":
        insertar(lista3,aux.info,"producto")
    if aux.info.reciclado == True:
        insertar(lista4,aux.info,"producto")
    print("XXXXX",aux.info.producto)
    a = aux.info.producto.find("AT")
    if a != -1:
        ganancia_AT += aux.info.precio
    aux = aux.sig



print("Compras de darth")
barrido(lista3)
print("")
print("Total recaudado",total)
print("Unidades vendidas",unidades_vendidas)
print(compradores)
print(" ")
print("Lista de rebajas por reciclaje")
barrido(lista4)
#mostrar clientes y monto a devolver de cada uno.
def rebaja(monto):
    return (monto / 100) * 15
aux = lista4.inicio
while aux:
    print(" ")
    print(aux.info.comprador)
    print("Rebaja del 15%")
    print("monto a devolver",rebaja(aux.info.precio))
    aux = aux.sig
print("Ganancia de los productos serie AT",ganancia_AT)