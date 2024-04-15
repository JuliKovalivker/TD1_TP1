def bin_misma_len(n:int, m:int) -> list[str]:
    '''
    Requiere: n y m > 0
    Devuelve: una lista con la representación binaria de n y m con la 
    misma len compleada con 0s. La primera posicion de la lista corresponde
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
    Requiere: a > 0, a < b, n > 0
    Devuelve: los numeros en el intervalo [a, b] que
    son vecinos aledaños a n
    '''
    i:int = a
    res:list[int] = []
    #AROTU HACE EL PREDICADO PERO LLAMANOS POR DS CUANDO LO HAGAS
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
    #HACER PREDICADOOOOOOOOO (AROTU) 
    while i < len(n_bin):
        if n_bin[i] != m_bin[i]:
            res += 1
        i += 1
    return res


def son_aledaños(n:int, m:int) -> bool:
    '''
    Requiere: n y m > 0
    Devuelve: True si son vecinos aledaño, False si no lo son
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
    res:list[int] = aledaños_en_intervalo(n, 0, n-1)
    return res
#COMPROBAR


def cant_aledaños(n:int, a:int, b:int) -> int:
    '''
    Requiere: a > 0, a < b, n > 0
    Devuelve: la cantidad de numeros en el intervalo [a, b] que
    son vecinos aledaños a n
    '''
    res:int = len(aledaños_en_intervalo(n, a, b))
    return res


def densidad_intervalo(n:int, a:int, b:int) -> float:
    '''
    Requiere: a > 0, a < b, n > 0
    Devuelve: la densidad binaria de n en [a, b], con un error
    menor a 10^-5
    '''
    res:float = cant_aledaños(n, a, b) / (b - a)
    res = round(res, 5)
    return res