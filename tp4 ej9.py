from tda_lista_lista import Lista, insertar, busqueda, barrido, tamanio

class Alumno(object):

    def __init__(self, apellido, nombre, legajo):
        self.apellido = apellido
        self.nombre = nombre
        self.legajo = legajo

    def __str__(self):
        return self.apellido + " " + self.nombre

class Parcial(object):

    def __init__(self, materia, nota, fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

    def __str__(self):
        return self.materia + " " + self.nota


lista = Lista()

for i in range(3):
    apellido = input('ingrese apellido ')
    nombre = input('ingrese nombre ')
    legajo = input('ingrese legajo ')

    alumno = Alumno(apellido, nombre, legajo)
    insertar(lista, alumno, 'apellido')


legajo = input('ingrese legajo ')
while(legajo != ''):
    pos = busqueda(lista, legajo, 'legajo')
    if(pos is not None):
        materia = input('ingrese materia ')
        nota = int(input('ingrese nota'))
        fecha = ''#input('ingrese fecha')
        parcial = Parcial(materia, nota, fecha)
        insertar(pos.sublista, parcial, 'materia')

    legajo = input('ingrese legajo ')


# * punto A
barrido(lista)

# * punto B, C, D, E
aux = lista.inicio
while(aux is not None):
    promedio = 0
    parciales = aux.sublista.inicio
    control = True
    while(parciales is not None):
        if(parciales.info.nota < 6):
            control = False
        promedio += parciales.info.nota
        parciales = parciales.sig
        
    
    if(control and tamanio(aux.sublista) > 0):
        print('aprobo todos los examenes', aux.info)

    if(tamanio(aux.sublista) > 0 ):
        promedio = promedio / tamanio(aux.sublista) 
    print(promedio, aux.info)
    if(promedio>8.89):
        print('promedio mayor a ..', aux.info, promedio)

    if(aux.info.apellido[0].upper() == 'L'):
        print('comienza con..', aux.info)


    aux = aux.sig