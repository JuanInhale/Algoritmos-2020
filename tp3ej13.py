from tda_cola_dinamica import Cola, mostrar_cola, cola_vacia, arribo, atencion, tamanio, en_frente, mover_final
import math

class base_rebelde(object):
    
    def __init__(self,nombre,numero_flota,latitud,longitud):
        self.nombre = nombre
        self.numero_flota = numero_flota
        self.latitud = latitud
        self.longitud = longitud
    
    def __str__(self):
        return " Nombre : " +self.nombre + " Numero flota: " + str(self.numero_flota) + ". Latitud: " + str(self.latitud) + " longitud: " + str(self.longitud)


def borrar_base(base,aborrar):
    colaaux = Cola()
    while not cola_vacia(base):
        at = atencion(base)
        if base.nombre != at.nombre:
            arribo(colaaux,at)
    while not cola_vacia(colaaux):
        aten = atencion(colaaux)
        arribo(base,aten)

# Formula Haversine
def distancia(flota,lat,long):
    r = 6371000
    # Latitud
    gama1 = math.radians(lat) # origen
    gama2 = math.radians(flota.latitud) # destino
    # longitud en radianes
    fi1 = math.radians(long) #origen
    fi2 = math.radians(flota.longitud) #destino
    res = 2 * r * math.acos(math.sqrt(math.sin(((gama2 - gama1) / 2) ** 2)) + (math.cos(gama1) * math.cos(gama2) * math.sin(((fi2 - fi1) ** 2)/2)))
    return res

def prueba(base1):
    print(base1.latitud)

bases = Cola()
tres_bases = Cola()

print("Ingresar posicion actual")
latitud = int(input("latitud"))
longitud = int(input("longitud"))

flota1 = base_rebelde("base1",100,50,90)
arribo(bases,flota1)

flota1 = base_rebelde("base2",200,15,30)
arribo(bases,flota1)

flota1 = base_rebelde("base3",300,20,30)
arribo(bases,flota1)

flota1 = base_rebelde("base4",1,90,10)
arribo(bases,flota1)

#mostrar_cola(bases)

mayor = en_frente(bases)
colaaux1 = Cola()
while (not cola_vacia(bases)):
    a = atencion(bases)
    if a.numero_flota > mayor.numero_flota:
        mayor = a
    arribo(colaaux1,a)
while not cola_vacia(colaaux1):
    b = atencion(colaaux1)
    arribo(bases,b)
    
print("La base con mayor flota: ",mayor)
print(" ")

for e in range(3):
    baseaux = Cola()
    # math.cos return the cos of x radians
    # Si ingreso grados, antes debo convertirlos en radiants.
    distmin = (distancia(en_frente(bases),latitud,longitud))
    minim = en_frente(bases)
    while not cola_vacia(bases):
        a = atencion(bases)
        distanc = int(distancia(a,latitud,longitud))
        print(distanc)        #imprimo las distnacias calculadas, para verificar las 3 bases mas cercanas
        if distanc < distmin:
            distmin = distanc
            minim = a
        arribo(baseaux,a)
    
    while not cola_vacia(baseaux):
        b = atencion(baseaux)
        if (b.nombre != minim.nombre):
            arribo(bases,b)
            
    print(e,"-Distancia minima : ",distmin)
    print(e,"-Base : ",minim)
    arribo(tres_bases,minim)

print("final")
while not cola_vacia(bases):
    b = atencion(bases) 
    print(b)

mayor_flota = en_frente(tres_bases)
print("3 bases a menor distancia")
while not cola_vacia(tres_bases):
    c = atencion(tres_bases)
    print(c)
    if c.numero_flota > mayor_flota.numero_flota:
        mayor_flota = c
print("Base con mayor cantidad de flotas, de las tres cercanas: ",mayor_flota)
