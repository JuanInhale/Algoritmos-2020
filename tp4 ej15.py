from tda_lista_lista import Lista, insertar, eliminar, busqueda, barrido, barrido_con_sublista, tamanio, lista_vacia
from random import randint
def inicializar(lista):
    entrenador1 = Entrenador("Ash",199,2,190)
    insertar(entrenadores,entrenador1,"nombre")
    entrenador1 = Entrenador("Gary",1400,10,100)
    insertar(entrenadores,entrenador1,"nombre")
    entrenador1 = Entrenador("Brook",11,100,2)
    insertar(entrenadores,entrenador1,"nombre")
    entrenador1 = Entrenador("Misty",1,2,2)
    insertar(entrenadores,entrenador1,"nombre")
        
    pokemon1 = Pokemon("Pikachu",10,"electrico","")
    pos = busqueda(entrenadores,"Ash","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    pokemon1 = Pokemon("Charizard",100,"Fuego","")
    pos = busqueda(entrenadores,"Ash","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    pokemon1 = Pokemon("Terrakion",1,"Agua","")
    pos = busqueda(entrenadores,"Ash","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    pokemon1 = Pokemon("Ivisoaur",4,"Planta","")
    pos = busqueda(entrenadores,"Ash","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    pokemon1 = Pokemon("Ivisoaur",4,"Planta","")
    pos = busqueda(entrenadores,"Ash","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    
    pokemon1 = Pokemon("Dragonite",10,"Dragon","Volador")
    pos = busqueda(entrenadores,"Gary","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    pokemon1 = Pokemon("Pidgeot",100,"Volador","Normal")
    pos = busqueda(entrenadores,"Gary","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    pokemon1 = Pokemon("Ivisoaur",1,"Planta","")
    pos = busqueda(entrenadores,"Gary","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    pokemon1 = Pokemon("Ivisoaur",1,"Planta","")
    pos = busqueda(entrenadores,"Gary","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    
    pokemon1 = Pokemon("Geodude",1,"Tierra","Roca")
    pos = busqueda(entrenadores,"Brook","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    pokemon1 = Pokemon("Misigno",12,"unkown","uknow")
    pos = busqueda(entrenadores,"Brook","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    pokemon1 = Pokemon("Onix",15,"rock","")
    pos = busqueda(entrenadores,"Brook","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    pokemon1 = Pokemon("Wingull",15,"rock","Dragon")
    pos = busqueda(entrenadores,"Brook","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    
    pokemon1 = Pokemon("Starmi",99,"Agua","Psic")
    pos = busqueda(entrenadores,"Misty","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    pokemon1 = Pokemon("Tyrantrum",1,"Agua","Hada")
    pos = busqueda(entrenadores,"Misty","nombre")
    insertar(pos.sublista,pokemon1,"nombre")
    pokemon1 = Pokemon("Gyarados",5,"Agua","Volador")
    pos = busqueda(entrenadores,"Misty","nombre")
    insertar(pos.sublista,pokemon1,"nombre")

def CargaDatos(lista):
    nombre = str(input("Ingrese nombre : "))
    while (nombre != ""):
        torneosganados = int(input("Torneos ganados : "))
        batallasperdidas = int(input("Batallas perdidas : "))
        batallasganadas = int(input("Batallas ganadas : "))
        entrenador1 = Entrenador(nombre.capitalize(),torneosganados,batallasperdidas,batallasganadas)
        insertar(entrenadores,entrenador1,"nombre")
        nombre = str(input("Ingrese nombre : "))
        
def porcentaje(perdidas,ganadas):
    resultado = (ganadas * 100) // (perdidas + ganadas)
    return resultado

    barrido(entrenadores)    
    
    nombre = input("Entrenador : ")
    while (nombre != ""):
        pos = busqueda(entrenadores,nombre,"nombre")
        if (pos is not None):
            nombre = input("Pokemon : ")
            nivel = input("Nivel : ")
            tipo = input("Tipo : ")
            subtipo = input("Sub-Tipo : ")
            pokemon1 = Pokemon(nombre.capitalize(),nivel,tipo.capitalize(),subtipo.capitalize)
            insertar(pos.sublista,pokemon1,"nombre")
        nombre = input("Entrenador : ")
    
    barrido_con_sublista(entrenadores)    

class Entrenador(object):
    
    def __init__(self,nombre,torneosganados,batallasperdidas,batallasganadas):
        self.nombre = nombre
        self.torneosganados = torneosganados
        self.batallasganadas = batallasganadas
        self.batallasperdidas = batallasperdidas
        
    def __str__(self):
        return "Entrenador: " + self.nombre + ": Torneos ganados: " + str(self.torneosganados) + ". Batallas ganadas: " + str(self.batallasganadas) + ". Batallas perdidas: " + str(self.batallasperdidas)

        
        
class Pokemon(object):
    
    def __init__(self,nombre,nivel,tipo,subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo
    def __str__(self):
        return  "Nombre: " + self.nombre + ". Nivel: " + str(self.nivel)  + ". Tipo: " + str(self.tipo) + ". SubTipo: " + str(self.subtipo)  
        
entrenadores = Lista()
inicializar(entrenadores)
#print("A - Inicializar  B - cargar datos manual?: ")
barrido_con_sublista(entrenadores)

print(" ")
maestro = input("Ingrese nombre del entrenador para mostrar datos: ")
maestro_cantidad = input("Ingrese nombre para mostrar cantidad de pokemons: ")
maestro_promedio_nivel = input("Ingrese entrendor para saber el promedio de nivel de sus pokemon: ")
print(" ")
pokemonRepite = input("Ingrese un pokemon para saber cuantos entrenadores lo tienen: ")
print("Ingrese un maestro pokemon y su pokemon para buscarlo: ")
maestro1 = input("Ingrese Entrenador: ")
pokemon1 = input("Ingrese pokemon: ")
aux = entrenadores.inicio
ganadoresTorneo = []
mayorTorneo = entrenadores.inicio
#mayorNivel = aux.sublista
#print("MARCA",aux.sublista.inicio.info)
contadorpokemon = 0
contRepetidos = 0
control1 = False
while(aux is not None):
    control1 = False
    contRepetidos = 0
    sub = aux.sublista.inicio
    sub6 = aux.sublista.inicio
    sub5 = aux.sublista.inicio
    sub2 = mayorTorneo.sublista.inicio
    mayorNivelPokemon = mayorTorneo.sublista.inicio
    sub3 = aux.sublista.inicio
    sub4 = aux.sublista.inicio
    cont = 0
    porcentajeganadas = porcentaje(aux.info.batallasperdidas,aux.info.batallasganadas)
    
    if (porcentajeganadas > 79):
        print(aux.info.nombre,"tiene un porcentaje de ",porcentajeganadas,"% batallas ganadas.")
        print(" ")
    if (aux.info.nombre == maestro):
        print("Datos del entrenador ",maestro,".")
        print(aux.info)
        barrido(aux.sublista)
        print(" ")
    if (aux.info.torneosganados > 3):
        ganadoresTorneo.append(aux.info.nombre)
    #Punto c
    if (aux.info.torneosganados > mayorTorneo.info.torneosganados):
        mayorTorneo = aux
        mayorNivelPokemon = mayorTorneo.sublista.inicio        
    while (sub2 is not None):
        if (sub2.info.nivel > mayorNivelPokemon.info.nivel):
            mayorNivelPokemon = sub2
        sub2 = sub2.sig
    print(" ")
    # cantidad de pokemones de cada entrenador
    if (aux.info.nombre == maestro_cantidad):
        while (sub3 is not None):
            cont += 1
            sub3 = sub3.sig
        print(aux.info.nombre,"Cantidad de pokemones: ",cont)
    #Punto f
    while (sub is not None):
        cont += 1
        if (sub.info.tipo == "Fuego" and sub.info.subtipo == "") or (sub.info.tipo == "Planta" and sub.info.subtipo == "") or (sub.info.tipo == "Agua" and sub.info.subtipo == "Volador"):
            print("Tiene un pokemon tipo fuego o planta o un tipo agua/volador. ",aux.info.nombre)
        #Punto h
        if (sub.info.nombre == pokemonRepite):
            contadorpokemon += 1
            break
        # Punto i
        while (sub5 is not None):
            if (sub.info.nombre == sub5.info.nombre):
                contRepetidos += 1
            sub5 = sub5.sig 
        # Punto j
        if (sub.info.nombre == "Tyrantrum" or sub.info.nombre == "Terrakion" or sub.info.nombre == "Wingull"):
            control1 = True
            print(sub.info.nombre)
            break
        sub = sub.sig
    if (control1 == True):
        print("Tiene al pokemon Tyrantrum, Terrakion o Wingull: ",aux.info.nombre)
    if (contRepetidos > 1):
        print("Entrenador con pokemon repetidos :", aux.info.nombre)
    #Punto g
    if (aux.info.nombre == maestro_promedio_nivel):
        cont3 = 0
        acum = 0
        while (sub4 is not None):
            cont3 += 1
            acum += int(sub4.info.nivel)
            sub4 = sub4.sig
        promedioNivel = acum // cont3
        print("El promedio de niveles de ",aux.info.nombre," es ",promedioNivel)
    # Punto k
    if (aux.info.nombre == maestro1):
        while (sub6 is not None):
            if (sub6.info.nombre == pokemon1):
                print("MARCA Encontrado ",aux.info)
                print("MARCA Su Pokemon ",sub6.info)
            sub6 = sub6.sig
    aux = aux.sig


print(" ")    
print("Gandores de mas de 3 Torneos. ",ganadoresTorneo)
print(" ")
print("Entrenador con mas trofeos ganados:",mayorTorneo.info.nombre)
print("Pokemon con mayor nivel del entrenador con mas trofeos",mayorNivelPokemon.info)
print(pokemonRepite," lo tienen ",contadorpokemon,"Entrenadores")