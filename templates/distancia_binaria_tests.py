import unittest

# Se importa el código a testear.
from distancia_binaria import distancia_binaria, son_aledaños, aledaños_menores, cant_aledaños, densidad_intervalo, bin_misma_len, aledaños_en_intervalo

#####################################################################
class TestDistanciaBinaria(unittest.TestCase):
    # Testear cuando la distancia binaria es 0
    def test_distancia_cero(self):
        self.assertEqual(distancia_binaria(1,1), 0)
        self.assertEqual(distancia_binaria(120,120), 0)
        
    # Testear distancia binaria entre numeros con diferente cantidad de digitos
    def test_distintos_digitos(self):
        self.assertEqual(distancia_binaria(1, 128), 2)
        self.assertEqual(distancia_binaria(256, 3), 3)

# Tests para la función distancia_binaria()
class TestDistanciaBinaria(unittest.TestCase):

    # Probar números con distinta cantidad de digitos en binario
    def test_distintos_digitos(self):
        output:int = distancia_binaria(1,128)
        expected_output:int = 2
        self.assertEqual(output,expected_output)

    # Probar el mismo numero
    def test_mismo_numero(self):
        output:int = distancia_binaria(128,128)
        expected_output:int = 0
        self.assertEqual(output,expected_output)

    # Ningún digito coincide
    def test_distancia_completa(self):
        output:int = distancia_binaria(127,128)
        expected_output:int = 8
        self.assertEqual(output,expected_output)

# Tests para la función son_aledaños()
class TestSonAledanos(unittest.TestCase):

    # Probar 2 números aledaños
    def test_aledanos_verdadero(self):
        output:bool = son_aledaños(8,12)
        expected_output:bool = True
        self.assertEqual(output,expected_output)
    
    # Probar 2 números que no son aledaños
    def test_aledanos_falso(self):
        output:bool = son_aledaños(6,18)
        expected_output:bool = False
        self.assertEqual(output,expected_output)

# Tests para la función aledaños_menores()
class TestAledanosMenores(unittest.TestCase):

    # Probar un número sin aledaños menores
    def test_ningun_aledano(self):
        output:list[int] = aledaños_menores(16)
        expected_output:list[int] = []
        self.assertEqual(output,expected_output)

    # Probar un número con varios vecinos aledaños menores
    def test_varios(self):
        output:list[int] = aledaños_menores(11)
        expected_output:list[int] = [3,9,10]
        self.assertEqual(output,expected_output)

# Tests para la función cant_aledaños()
class TestCantidadAledanos(unittest.TestCase):

    # Probar un número en el intervalo, con varios aledaños
    def test_en_intervalo(self):
        output:int = cant_aledaños(10,8,13)
        expected_output:int = 2
        self.assertEqual(output,expected_output)

    # Probar un número sin ningún aledaño en ese intervalo
    def test_sin_aledanos(self):
        output:int = cant_aledaños(32,1,32)
        expected_output:int = 0
        self.assertEqual(output,expected_output)

    # Probar un número menor que el intervalo, con aledaños en el intervalo
    def test_menor(self):
        output:int = cant_aledaños(1,4,32)
        expected_output:int = 3
        self.assertEqual(output,expected_output)

    # Probar un número cuyos aledaños sean el último, y primer número del intervalo
    def test_bordes(self):
        output:int = cant_aledaños(33,1,32)
        expected_output:int = 2
        self.assertEqual(output,expected_output)

# Tests para la función densidad_intervalo()
class TestDensidadIntervalo(unittest.TestCase):

    # Probar un intervalo cuya densidad binaria dé un número periódico
    def test_periodico(self):
        output:float = densidad_intervalo(10,8,13)
        expected_output:float = 0.33333
        self.assertEqual(output,expected_output)

    # Probar la mitad de los números del intervalo son aledaños
    def test_mitad_aledanos(self):
        output:float = densidad_intervalo(1,2,3)
        expected_output:float = 0.5
        self.assertEquals(output,expected_output)

    # Probar ningún número en el intervalo es aledaño
    def test_ningun_aledano(self):
        output:float = densidad_intervalo(32,1,31)
        expected_output:float = 0.0
        self.assertEqual(output,expected_output)

# Tests para la función bin_misma_len()
class TestBinMismaLen(unittest.TestCase):

    # Probar 2 números con la misma cantidad de bits
    def test_misma_len(self):
        output:list[str] = bin_misma_len(2,3)
        expected_output:list[str] = ['10','11']
        self.assertEqual(output,expected_output)

    # Probar 2 números con diferentes cantidades de bits
    def test_distina_len(self):
        output:list[str] = bin_misma_len(1,8)
        expected_output:list[str] = ['0001','1000']
        self.assertEqual(output,expected_output)

    # Probar 2 números con diferentes cantidades de bits, pero arrancando con el mayor
    def test_distina_len_mayor_primero(self):
        output:list[str] = bin_misma_len(8,1)
        expected_output:list[str] = ['1000','0001']
        self.assertEqual(output,expected_output)

    # Probar el mismo número, 2 veces
    def test_distina_len(self):
        output:list[str] = bin_misma_len(2,2)
        expected_output:list[str] = ['10','10']
        self.assertEqual(output,expected_output)

# Tests para la función aledaños_en_intervalo()
class TestAledanosEnIntervalo(unittest.TestCase):
    # Probar ningún aledaño en el intervalo
    def test_ninguno(self):
        output:list[int] = aledaños_en_intervalo(32,1,31)
        expected_output:list[int] = []
        self.assertEqual(output,expected_output)

    # Probar un intervalo vacío
    def test_intervalo_vacio(self):
        output:list[int] = aledaños_en_intervalo(1,2,2)
        expected_output:list[int] = []
        self.assertEqual(output,expected_output)
        
    # Probar algunos aledaños en el intervalo
    def test_algunos(self):
        output:list[int] = aledaños_en_intervalo(10,8,13)
        expected_output:list[int] = [8,11]
        self.assertEqual(output,expected_output)

    # Probar un número cuyos aledaños sean el último, y primer número del intervalo
    def test_bordes(self):
        output:list[int] = aledaños_en_intervalo(33,1,32)
        expected_output:list[int] = [1,32]
        self.assertEqual(output,expected_output)


unittest.main()
