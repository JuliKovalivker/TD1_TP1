{% comment %} def bin_misma_len(n:int, m:int) -> list[str]:
    '''
    Requiere: n y m > 0
    Devuelve: una lista con la representación binaria de n y m con la 
    misma longitud, completada con 0s. La primera posicion de la lista corresponde
    a n y la segunda a m
    '''
    n_bin:str = bin(n).replace('0b', '')
    m_bin:str = bin(m).replace('0b', '')
    if len(n_bin) != len(m_bin):
        if len(n_bin) > len(m_bin):
            m_bin = '0'*(len(n_bin)-len(m_bin)) + m_bin
        else:
            n_bin = '0'*(len(m_bin)-len(n_bin)) + n_bin
    res:list[str] = [n_bin, m_bin]
    return res


def aledaños_en_intervalo(n:int, a:int, b:int) -> list[int]:
    '''
    Requiere: n > 0, a > 0, a < b
    Devuelve: los numeros en el intervalo [a, b] que
    son vecinos aledaños a n
    '''
    i:int = a
    res:list[int] = []
    while i <= b:
        if son_aledaños(n, i):
            res.append(i)
        i += 1
    return res


def distancia_binaria(n:int, m:int) -> int:
    '''
    Requiere: n y m > 0
    Devuelve: la distancia binaria entre n y m
    '''
    res:int = 0
    i:int = 0
    lista_bin:list[str] = bin_misma_len(n, m)
    n_bin:str = lista_bin[0]
    m_bin:str = lista_bin[1]   
    while i < len(n_bin):
        if n_bin[i] != m_bin[i]:
            res += 1
        i += 1
    return res


def son_aledaños(n:int, m:int) -> bool:
    '''
    Requiere: n y m > 0
    Devuelve: True si son vecinos aledaños, False si no lo son
    '''
    res:bool = False
    if distancia_binaria(n, m) == 1:
        res = True
    return res


def aledaños_menores(n:int) -> list[int]:
    '''
    Requiere: n > 0
    Devuelve: los vecinos aledaños menores a n
    '''
    res:list[int] = aledaños_en_intervalo(n, 1, n-1)
    return res


def cant_aledaños(n:int, a:int, b:int) -> int:
    '''
    Requiere: n > 0, a > 0, a < b
    Devuelve: la cantidad de números en el intervalo [a, b] que
    son vecinos aledaños a n
    '''
    res:int = len(aledaños_en_intervalo(n, a, b))
    return res


def densidad_intervalo(n:int, a:int, b:int) -> float:
    '''
    Requiere: n > 0, a > 0, a < b
    Devuelve: la densidad binaria de n en [a, b], con un error
    menor a 10^-5
    '''
    res:float = cant_aledaños(n, a, b) / (b - a + 1)
    res = round(res, 5)
    return res

def formatear_lista_numeros(lista:list[int]) -> str:
    '''
    Requiere: nada
    Devuelve: Un string representando los valores de la lista sin
    y el último valor separado por 'y'. [1,2,3] -> "1, 2 y 3"
    '''
    res:str = ''
    i:int = 0
    while i < len(lista)-1:
        res = res + str(lista[i])
        if(i != len(lista)-2): # Si estamos en el último valor, no agregar ', '
            res += ', '
        i+=1
        
    if len(lista) > 1 : # Si hay más de un valor, agregar ' y '
        res += ' y ' + str(lista[-1])
    else:               # Si hay solo un valor
        res = str(lista[0])

    return res {% endcomment %}

def bin_misma_len(n:int, m:int) -> list[str]:
    '''
    Requiere: n y m > 0
    Devuelve: Una lista con la representación binaria de n y m con la misma longitud, completada con ceros.
    La primera posicion de la lista corresponde a n y la segunda a m.
    '''
    res:list[str] = [] # Valor de retorno.
    n_bin:str = bin(n).replace('0b', '') # A n_bin asignale como valor n (en su representación binaria).
    m_bin:str = bin(m).replace('0b', '') # A m_bin asignale como valor m (en su representación binaria).
    if len(n_bin) != len(m_bin): # Si la longitud de n_bin difiere de la de m_bin...
        if len(n_bin) > len(m_bin): # Si la longitud de n_bin es mayor a la de m_bin...
            m_bin = '0'*(len(n_bin)-len(m_bin)) + m_bin # A m_bin concatenale (por la izquierda) tantos ceros como sea la diferencia entre la longitud de n_bin y m_bin.
        else: # De lo contrario...
            n_bin = '0'*(len(m_bin)-len(n_bin)) + n_bin # A n_bin concatenale (por la izquierda) tantos ceros como sea la diferencia entre la longitud de n_bin y m_bin.
    res:list[str] = [n_bin, m_bin] # A res asignale como valor una lista conformada por n_bin y m_bin (en dicho orden).
    return res # Retorna res.

def distancia_binaria(n:int, m:int) -> int:
    '''
    Requiere: n y m > 0
    Devuelve: La distancia binaria entre n y m.
    '''
    res:int = 0 # Valor de retorno.
    i:int = 0 # Índice.
    lista_bin:list[str] = bin_misma_len(n, m) # A lista_bin asignale como valor una lista conformada por n y m (en formato binario).
    n_bin:str = lista_bin[0] # A n_bin asignale como valor el primer elemento de lista_bin, es decir, n (en formato binario).
    m_bin:str = lista_bin[1] # A m_bin asignale como valor el primer elemento de lista_bin, es decir, m (en formato binario).
    while i < len(n_bin): # Mientras i sea menor a la longitud de n_bin...
        if n_bin[i] != m_bin[i]: # Si el i-ésimo caracter (dígito) de n_bin difiere del i-ésimo caracter (dígito) de m_bin...
            res += 1 # A res sumale 1.
        i += 1 # A i sumale 1.
    return res # Retorna res.

def son_aledaños(n:int, m:int) -> bool:
    '''
    Requiere: n y m > 0
    Devuelve: True si son vecinos aledaños, False si no lo son.
    '''
    res:bool = False # Valor de retorno. A res asignale False.
    if distancia_binaria(n, m) == 1: # Si la distancia binaria entre n y m es equivalente a 1...
        res = True # A res asignale True.
    return res # Retorna res.

def aledaños_en_intervalo(n:int, a:int, b:int) -> list[int]:
    '''
    Requiere: n > 0, a > 0, a < b
    Devuelve: Los numeros en el intervalo [a, b] que son vecinos aledaños a n.
    '''
    res:list[int] = [] # Valor de retorno.
    i:int = a # Índice. A i asignale como valor a.
    while i <= b: # Mientras i sea menor o igual a b...
        if son_aledaños(n, i): # Si n e i son aledaños... 
            res.append(i) # Añadí i a res.
        i += 1 # A i sumale 1.
    return res # Retorna res.

def aledaños_menores(n:int) -> list[int]:
    '''
    Requiere: n > 0
    Devuelve: Los vecinos aledaños menores a n.
    '''
    res:list[int] = aledaños_en_intervalo(n, 1, n-1) # Valor de retorno. A res asignale como valor los vecinos aledaños desde 1 hasta n (sin incluir).
    return res # Retorna res.

def cant_aledaños(n:int, a:int, b:int) -> int:
    '''
    Requiere: n > 0, a > 0, a < b
    Devuelve: la cantidad de números en el intervalo [a, b] que son vecinos aledaños a n.
    '''
    res:int = len(aledaños_en_intervalo(n, a, b)) # Valor de retorno. A res asignale como valor la longitud de la lista de aledaños en intervalo.
    return res # Retorna res.

def densidad_intervalo(n:int, a:int, b:int) -> float:
    '''
    Requiere: n > 0, a > 0, a < b
    Devuelve: La densidad binaria de n en [a, b], con un error menor a 10^-5.
    '''
    res:float = cant_aledaños(n, a, b) / (b + 1 - a) # Valor de retorno. A res asignale como valor la división entre la cantidad de vecinos aledaños en un intervalo y la diferencia de dicho intervalo. 
    return round(res, 5) # Retornamos res redondeado (hasta 5 ceros después de la coma).

def formatear_lista_numeros(lista:list[int]) -> str:
    '''
    Requiere: len(lista) > 0.
    Devuelve: Los valores de lista enumerados bajo las reglas del lenguaje natural (español).
    Ello implica lo siguiente: [1,2,3,4] -> '1, 2, 3 y 4' o [1,2] -> '1 y 2'.
    '''
    res:str = '' # Valor de retorno
    i:int = 0 # Índice
    if len(lista) == 1: # Si la longitud de lista es de un elemento...
        res = str(lista[0]) # Asignale a res el valor del único elemento de lista (en formato string).
    else: # De lo contrario...
        while i < len(lista): # Mientras i sea menor a la longitud de lista...
            res = res + str(lista[i]) # A res concatenale el i-ésimo elemento de la lista (en formato string).
            if i < len(lista)-2:  # Si i es menor a la longitud de lista - 2...
                res = res + ', ' # A res concatenale ', '.
            elif i == len(lista)-2: # Si i es equivalente a la longitud de lista - 2...
                res = res + ' y ' # A res concatenale ' y '.
            i = i + 1 # A i sumale 1.
    return res # Retorna res 