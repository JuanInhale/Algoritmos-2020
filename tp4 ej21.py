from tda_lista_lista import Lista, insertar, eliminar, busqueda, barrido, barrido_con_sublista, tamanio

class Pelicula(object):
    
    def __init__(self,nombre,valoracion,anio_estreno,recaudacion):
        self.nombre = nombre
        self.valoracion = valoracion
        self.anio_estreno = anio_estreno
        self.recaudacion = recaudacion
    
    def __str__(self):
        return self.nombre + " " + str(self.anio_estreno) + " " + str(self.valoracion) + " " + str(self.recaudacion)

peliculas = Lista()

pelicula1 = Pelicula("señor de los anillos",9,2003,1000000000)
insertar(peliculas,pelicula1,"valoracion")

pelicula1 = Pelicula("señor de los anillos 2",8,2005,900000000)
insertar(peliculas,pelicula1,"valoracion")

pelicula1 = Pelicula("señor de los anillos 3",7,2007,700000000)
insertar(peliculas,pelicula1,"valoracion")

pelicula1 = Pelicula("señor de los anillos 4",9,2003,500000000)
insertar(peliculas,pelicula1,"valoracion")

pelicula1 = Pelicula("Harry potter",2,2005,109999999)
insertar(peliculas,pelicula1,"valoracion")

#barrido(peliculas)

anio_mostrar = int(input("Mostrar las peliculas del anio :"))
pelis_anio = Lista()

mayor_recaudo = peliculas.inicio.info
aux = peliculas.inicio
mayor_valoracion = peliculas.inicio.info.valoracion
while aux:
    if aux.info.anio_estreno == anio_mostrar:
        insertar(pelis_anio,aux.info,"nombre")
    if aux.info.recaudacion>mayor_recaudo.recaudacion:
        mayor_recaudo = aux.info
    if aux.info.valoracion > mayor_valoracion:
        mayor_valoracion =  aux.info.valoracion
    aux = aux.sig

print("Peliculas con mayor valoracion")
aux = peliculas.inicio
while aux:
    if aux.info.valoracion == mayor_valoracion:
        print(aux.info)
    aux = aux.sig

print(mayor_recaudo)
print("Lista de peliculas del año: ",anio_mostrar)
barrido(pelis_anio)

lista_aux = Lista()
crit = str(input("Ingrese el criterio por el cual se motrara el contenido de la lista: "))
aux = peliculas.inicio
while aux:
    insertar(lista_aux,aux.info,crit)
    aux = aux.sig        
    
barrido(lista_aux)