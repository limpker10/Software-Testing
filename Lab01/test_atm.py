import unittest
from atm import Cajero

class CajeroTest(unittest.TestCase):
    def setUp(self):
        self.cajero = Cajero()
    
    """
    def test_retiro_saldo_suficiente(self):
        #Se comprueba que el retiro sea un monto menor o igual al monto disponible(5000)
        self.assertTrue(self.cajero.validar_retiro(5000))
        
    def test_retiro_saldo_insuficiente(self):
        #Se comprueba que el retiro no sea mayor al monto disponible(5000)
        self.assertFalse(self.cajero.validarRetiro(5001))
    """

    def test_retiro_saldo_disponible(self):
        #Se comprueba que el retiro sea un monto igual al monto disponible(5000)
        self.assertTrue(self.cajero.validar_retiro(5000))
        #Se comprueba que el retiro sea un monto menor al monto disponible(5000)
        self.assertTrue(self.cajero.validar_retiro(450))
        #Se comprueba que el retiro no sea mayor al monto disponible(5000)
        self.assertFalse(self.cajero.validar_retiro(5001))

    def test_retiro_minimo(self):
        #Se comprueba que el retiro no sea igual a una cantidad nula(0)
        self.assertFalse(self.cajero.retiro_minimo(0))
        #Se comprueba que el retiro no sea un valor negativo
        self.assertFalse(self.cajero.retiro_minimo(-450))
        #Se comprueba que el retiro sea mayor a 0
        self.assertTrue(self.cajero.retiro_minimo(100))

    def test_retiro_maximo(self):
        #Se comprueba que el retiro sea menor al retiro maximo establecido(3000)
        self.assertTrue(self.cajero.retiro_maximo(2000))
        #Se comprueba que el retiro no sea mayor al retiro maximo establecido(3000)
        self.assertFalse(self.cajero.retiro_maximo(4000))
    
    def test_retirar(self):
        #Se comprueba que la operacion de retiro descuenta el retiro del monto inicial
        self.assertEqual(self.cajero.realizar_retiro(1500),(5000-1500))

    def test_depositar(self):
        #Se comprueba que la operacion de deposito añade el deposito al monto inicial
        self.assertEqual(self.cajero.realizar_deposito(2343), (5000+2343))

    def test_deposito_minimo(self):
        #Se comprueba que el deposito no sea igual a una cantidad nula(0)
        self.assertFalse(self.cajero.deposito_minimo(0))
        #Se comprueba que el deposito no sea un valor negativo
        self.assertFalse(self.cajero.deposito_minimo(-450))
        #Se comprueba que el deposito sea mayor a 0
        self.assertTrue(self.cajero.deposito_minimo(200))
    
    def test_deposito_maximo(self):
        #Se comprueba que el deposito sea menor al deposito maximo establecido(10000)
        self.assertTrue(self.cajero.deposito_maximo(5000))
        #Se comprueba que el deposito no sea mayor al deposito maximo establecido(10000)
        self.assertFalse(self.cajero.deposito_maximo(15000))

    def test_ver_saldo(self):
        #Se comprueba que se muestra el saldo inicial por consola
        self.assertEqual(self.cajero.obtener_saldo(),5000)
        #Se comprueba que se muestra el saldo despues de haber hecho un deposito
        self.cajero.realizar_deposito(20)
        self.assertEqual(self.cajero.obtener_saldo(),5020)
        #Se comprueba que se muestra el saldo despues de haber hecho un retiro
        self.cajero.realizar_retiro(20)
        self.assertEqual(self.cajero.obtener_saldo(),5000)


if __name__ == '__main__':
    unittest.main()