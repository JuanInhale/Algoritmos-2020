
def suma(n):
	if n == 0:
		return 0
	elif n > 0:
		r = n + suma(n-1)
	return r

def fibonacci(n):
	if (n == 0):
		return 0
	elif (n == 1) or (n == 2):
		return 1
	else:
		return (fibonacci(n-2)+fibonacci(n-1))

def producto(num1,num2):
	if num2 == 1:
		return num1
	else:
		res = num1 + producto(num1, num2-1)
	return res
	
def potencia(base, exp):
	if (exp == 0):
		return 1
	else:
		return (base*potencia(base,exp-1))	

def secuenciainvert(palabra,longitud):
	inv = ""
	if longitud == 0:
		#secuenciainvert(palabra,longitud)		
		#inv = inv + palabra[0]	
		return inv
	else:
		inv  = palabra[longitud-1] + secuenciainvert(palabra,longitud-1) 
	return inv 

def serie(n):
	s = 0
	if n == 1:
		return (s + 1)
	else:
		s = (1/n) + serie(n-1)
	return s

def binario(numero):
    if(numero <= 1):
        return str(numero)
    else:
        return binario(numero//2) + str(numero % 2) 

def caractent(num):
	cont = 0
	if (num < 10):
		return 1  
	elif (num > 9):
		cont += 1 + caractent(num/10)
		return cont

def invent(num):
	if (num < 10):
		return num
	else:
		return (num % 10) * 10 + invent(num // 2)

def sumadig(num):
	if (num == 0):
		return 0 
	else:
		resto = (num % 10)
		suma = resto + sumadig(num // 10)
		return suma

def raiz(num):
    x=0
    if (x * x) > num:
        return x
    else:
        x += 0.1 + raiz(num)
        return x
		
def bbin(vector, buscado, primero, ultimo):
    if(primero <= ultimo):
        med = (primero + ultimo) // 2
        if(vector[med] == buscado):
            return med
        elif(vector[med] > buscado):
            return bbin(vector, buscado, primero, med-1)
        else:
            return bbin(vector, buscado, med+1, ultimo)
    else:
        return -1
								
def mcd(m, n):
    """Cálculo del máximo comun divisor."""
    if(m % n == 0):
        return n
    else:
        return mcd(n, m % n)

def mcm(m, n):
    """Cálculo del mínimo comun multiplo."""
    if(n % m == 0):
        return n
    else:
        return mcm(n, m * n)

def logaritmo(base, numero):
    if(base == numero):
        return 1
    else:
        return 1 + logaritmo(base, numero/base)

def recorrervector(vector):
    tam = len(vector)
    if tam == 1:
        return print(vector[0])
    else:
        print(vector[tam-1])
        recorrervector(vector)
        
def barrido(vec):
    if(len(vec) == 1):
        print(vec[0])
    else:
        print(vec[-1])
        barrido(vec[0:-1])

def bussecuencial(vector,buscado):
    tam = len(vector)
    result = False	
    if (tam == 1):
        if vector[0] == buscado:
            result = True
            return result
        elif  (buscado == vector[tam-1]):
            result = True
            bussecuencial(vector,buscado)

def contar_naves(vec):
    if(len(vec)==0):
        return 0
    else:
        if(vec[-1][2]):
            return 1 + contar_naves(vec[0:-1])
        else:
            return 0 + contar_naves(vec[0:-1])

def barrido_matriz(mat, i, j):
    if(i<len(mat) and j<len(mat[i])):
        print(mat[i][j])
        if(j == len(mat[i])-1):
            i += 1
            j = -1
        barrido_matriz(mat, i, j+1)

                
def salida_laberinto(matriz, x, y , caminos=[]):
        if (x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
            if(matriz[x][y] == 2):
                caminos.append([x,y])
                print("Saliste del laboratorio. ")
                print(caminos)
                caminos.pop()
            elif(matriz[x][y] == 1):
                matriz[x][y] = 3
                caminos.append([x,y])
                salida_laberinto(matriz,x,y+1,caminos)
                salida_laberinto(matriz,x,y-1,caminos)
                salida_laberinto(matriz,x-1,y,caminos)
                salida_laberinto(matriz,x+1,y,caminos)
                caminos.pop()
                matriz[x][y] = 1

def quicksort(vector, primero, ultimo):
    if(primero<ultimo):
        pivot = ultimo
        izq = primero
        der = ultimo-1
        while(izq < der):
            while(vector[izq] < vector[pivot]):
                izq += 1

            while(vector[der] > vector[pivot]):
                der -= 1

            if(izq < der):
                vector[izq], vector[der] = vector[der], vector[izq]

        if(vector[izq]>vector[pivot]):
            vector[izq], vector[pivot] = vector[pivot], vector[izq]

        quicksort(vector, primero, izq-1)
        quicksort(vector, izq+1, ultimo)

def raiz_cuadrada(entero):
    # x*x = res
    x = 0
    while x * x <= 0:
        x += 0.1
    return x
    
def raiz_cuadrada2(n,x):
    if x * x > n:
        return x
    else:
        x += 0.1
        raiz_cuadrada2(n,x)

def cuenta_regresiva(numero):
    if numero == 0:
        print("Boom!")
    else:
        print(numero)
        cuenta_regresiva(numero-1)

cuenta_regresiva(6)

def recorrer_vector(vector):
    pos = len(vector)
    if pos == 1:
        print(vector[0])
    else:
        print(vector[pos-1])
        recorrer_vector(vector[0:-1])
        
vector = [1,2,3,4,5,6]
recorrer_vector(vector)

# cada termino se obtiene a partir del aterior multiplicando *r
def sucesion_geometrica(n,r):
    s=0
    for i in range(n):
        s+=r**i
        print(i+1,r**i,s)
    print("En notación científica es %e,\n y el total es: %E granos de trigo." % (2**i,s))

sucesion_geometrica(20,2)

def sucesion_geo_recursiva(a,n,r):    
    # primero tengo que hacer una sucesion del a al n, recursiva
    if a == n:
        print(a*r)
    else:
        print(a*r)
        sucesion_geo_recursiva(a+1,n,r)
        
sucesion_geo_recursiva(2,10,-2)

def rec1(a,n):
    if a == n:
        print(2)
    else:
        print(n + (1/rec1(a,n-1)))
        rec1(a+1,n)

        
def storm_trooper(vector,contador):
    pos = len(vector)
    if pos == 1:
        if vector[0][2] == "derribado":
            contador += 1
        print(contador)
    else:
        if vector[pos-1][2] == "derribado":
            storm_trooper(vector[0:-1],contador+1)
        else:
            storm_trooper(vector[0:-1],contador)
    
    
atat = [["50,100","canion","derribado"],["05,10","laser","derribado"],["2,65","granada","no derribado"]]
print("Naves derribadas")
storm_trooper(atat,0)                

def torre_hanoi(discos,torre1,torre2,torre3):
    if discos == 1:
        print("mueve el disco ",discos," desde la torre ",torre1,"hasta",torre2)
    else:
        torre_hanoi(discos-1,torre1,torre2,torre3)
        print("mueve el disco ",discos," desde la torre ",torre1,"hasta",torre2)
        torre_hanoi(discos-1,torre3,torre2,torre1)

torre_hanoi(4,1,2,3)

def suc_geo2(a,n,razon):
    if n == a:
        print(a*4)
    else:
        print(n/4)
        suc_geo2(a,n/4  ,razon)
                    
suc_geo2(5.25,1376256,4)    

def suc_rec2(numero):
    if numero == 1:
        print(3)
    else:
        print(numero-1 + 2*numero)
        suc_rec2(numero-1)
        
print("")
print(suc_rec2(5))

