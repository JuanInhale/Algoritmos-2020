from tda_tabla_hash import crear_tabla, agregar_tc, buscar_tc_catedra, bernstein_catedra, buscar_tc_catedra
from tda_lista import Lista, insertar, barrido


class Catedra(object):

    def __init__(self, nombre, modalidad, horas, codigo):
        self.nombre = nombre
        self.modalidad = modalidad
        self.horas = horas
        self.docentes = []
        self.codigo = codigo
        
    def __str__(self):
        return self.codigo + " " + self.nombre + " " + self.modalidad + " " + str(self.horas)

class Docentes(object):
    
    def __init__(self, nombre,catedra):
        self.nombre = nombre
        self.catedra = catedra
        
    def __str__(self):
        return self.nombre + " " + self.catedra
        

# nombre, modalidad, horas, codigo

tabla_catedra = crear_tabla(50)

catedra = Catedra("Algoritmos y estructura de datos", "Anual", 10, "ADC_12345")
agregar_tc(tabla_catedra,bernstein_catedra,catedra)

cont = 0
for e in tabla_catedra:
    print(cont," ",e)
    cont += 1

profesores = Lista()
insertar(profesores,"Walter")
insertar(profesores,"Ricardo")


posicion = buscar_tc_catedra(tabla_catedra,bernstein_catedra,Catedra("","",0,"ADC_12345"))
if posicion:
    print("Carga de docente realizada.")
    tabla_catedra[posicion].docentes = profesores

cont = 0
for e in tabla_catedra:
    if e:
        print("Docentes : ")
        barrido(e.docentes)
        print(e)

