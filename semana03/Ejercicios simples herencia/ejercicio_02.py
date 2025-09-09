import unittest

class Vehiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self) -> str:
        return f'Datos del Vehiculo\nMarca: {self.marca}\nModelo: {self.modelo}'
    
class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, num_puertas: int):
        super().__init__(marca, modelo) 
        self.num_puertas = num_puertas

    def es_deportivo(self) -> bool: 
        return(self.num_puertas == 2)
    
# Prueba unitaria
class TestPruebaAutomovil(unittest.TestCase):
    def setUp(self):
        auto1 = Automovil('Mazda', '3', 4)
        auto2 = Automovil('Ferrari', 'Z', 2)

    def test_auto_no_deportivo(self):
        self.assertFalse(self.auto1.es_depotivo())

    def test_auto_deportivo(self):
        self.assertTrue(self.auto2.es_deportivo())

    def test_auto_deportivo_2(self):
        self.assertEqual(self.auto2.es_deportivo(), True)

    def test_auto_deportivo_3(self):
        self.assertLess(self.auto2.num_puertas, 3)
    
if __name__ == '__main__':
    # unittest.main()
    # Prueba de la clase automovil
    auto3 = Automovil('Honda', 'Accord', 2)
    if auto3.es_deportivo():
        print (auto3.mostrar_info() + '\n (Auto deportivo)')
    else:
        print (auto3.mostrar_info() + '\n (Auto sedán)')
        