def bin_misma_len(n:int, m:int) -> list[str]:
    '''
    Requiere: n y m > 0
    Devuelve: Una lista con la representación binaria de n y m con la 
    misma longitud, completada con ceros. La primera posicion de la lista corresponde
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

def distancia_binaria(n:int, m:int) -> int:
    '''
    Requiere: n y m > 0
    Devuelve: La distancia binaria entre n y m
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

def aledaños_en_intervalo(n:int, a:int, b:int) -> list[int]:
    '''
    Requiere: n > 0, a > 0, a < b
    Devuelve: Los numeros en el intervalo [a, b] que son vecinos aledaños a n.
    '''
    res:list[int] = []
    i:int = a    
    while i <= b:
        if son_aledaños(n, i):
            res.append(i)
        i += 1
    return res

def aledaños_menores(n:int) -> list[int]:
    '''
    Requiere: n > 0
    Devuelve: Los vecinos aledaños menores a n
    '''
    res:list[int] = aledaños_en_intervalo(n, 1, n-1)
    return res


def cant_aledaños(n:int, a:int, b:int) -> int:
    '''
    Requiere: n > 0, a > 0, a < b
    Devuelve: La cantidad de números en el intervalo [a, b] que son vecinos aledaños a n
    '''
    res:int = len(aledaños_en_intervalo(n, a, b))
    return res


def densidad_intervalo(n:int, a:int, b:int) -> float:
    '''
    Requiere: n > 0, a > 0, a < b
    Devuelve: La densidad binaria de n en [a, b], con un error menor a 10^-5
    '''
    res:float = cant_aledaños(n, a, b) / (b - a + 1) # (cantidad de vecinos aledaños en [a, b]) / len(intervalo)
    res = round(res, 5)
    return res


def formatear_lista_numeros(lista:list[int]) -> str:
    '''
    Requiere: Nada
    Devuelve: Los valores de lista enumerados bajo las reglas del lenguaje natural (español).
    Ello implica lo siguiente: [1,2,3,4] -> '1, 2, 3 y 4' o [1,2] -> '1 y 2'.
    '''
    res:str = ''
    i:int = 0 
    if len(lista) == 1:
        res = str(lista[0])
    elif len(lista) != 0:
        while i < len(lista)-2:
            res = res + str(lista[i]) + ', '
            i = i + 1
        res = res + str(lista[-2]) + ' y ' + str(lista[-1])
    return res