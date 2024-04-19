import unittest

# Se importa el código a testear.
from distancia_binaria import distancia_binaria, son_aledaños, aledaños_menores, cant_aledaños, densidad_intervalo

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

# class TestVecinosBinarios(unittest.TestCase):
#     ## ATENCION: los nombres de estas funciones deben empezar con test_

#     def test_...(self):
#         self.assertEqual(cant_vocales('aáAÁ', 4)
# 		self.assertEqual(cant_vocales('aeiouAEIOUáéíóúÁÉÍÓÚ', 22)
        

#     def test_...(self):
#         ...

## y asi con el resto de las funciones a testear.

unittest.main()
