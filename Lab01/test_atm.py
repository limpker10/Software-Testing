import unittest
from atm import Cajero

class CajeroTest(unittest.TestCase):
    def setUp(self):
        self.cajero = Cajero()

    
    def test_validacion_contraseña(self):
        #Se comprueba una contraseña correcta
        self.assertTrue(self.cajero.validar_contraseña("5467"), "Error: Se esperaba una contraseña correcta")
        #Se comprueba una contraseña Incorrecta
        self.assertFalse(self.cajero.validar_contraseña("4167"), "Error: Se esperaba una contraseña incorrecta")
        # Caso de prueba: contraseña incorrecta (mayor a 4 dígitos)
        self.assertFalse(self.cajero.validar_contraseña("55267"), "Error: Se esperaba una contraseña incorrecta")
        # Caso de prueba: contraseña incorrecta (valor negativo)
        self.assertFalse(self.cajero.validar_contraseña("-5467"), "Error: Se esperaba una contraseña incorrecta")
        # Caso de prueba: contraseña incorrecta (valor no numérico)
        self.assertFalse(self.cajero.validar_contraseña("abcd"), "Error: Se esperaba una contraseña incorrecta")

    def test_retiro_saldo_disponible(self):
         #Se comprueba que el retiro sea un monto igual al monto disponible(5000)
        self.assertTrue(self.cajero.validar_retiro(5000),"El retiro no se pudo realizar correctamente")
        #Se comprueba que el retiro sea un monto menor al monto disponible(5000)
        self.assertTrue(self.cajero.validar_retiro(450),"El saldo disponible no se actualizó")
        #Se comprueba que el retiro no sea mayor al monto disponible(5000)
        self.assertFalse(self.cajero.validar_retiro(5001),"El retiro excedio el saldo disponible")

    def test_retiro_minimo(self):
        #Se comprueba que el retiro no sea igual a una cantidad nula(0)
        self.assertFalse(self.cajero.retiro_minimo(0),"El retiro no debe ser igual a cero")
        #Se comprueba que el retiro no sea un valor negativo
        self.assertFalse(self.cajero.retiro_minimo(-450),"El retiro no debe ser un valor negativo")
        #Se comprueba que el retiro sea mayor a 0
        self.assertTrue(self.cajero.retiro_minimo(10),"El retiro debe ser mayor a cero")

    def test_retiro_maximo(self):
        #Se comprueba que el retiro sea menor al retiro maximo establecido(3000)
        self.assertTrue(self.cajero.retiro_maximo(2000),"El retiro es mayor al retiro máximo establecido")
        #Se comprueba que el retiro no sea mayor al retiro maximo establecido(3000)
        self.assertFalse(self.cajero.retiro_maximo(4000),"El retiro no excede el retiro máximo establecido")
    
    def test_retirar(self):
        #Se comprueba que la operacion de retiro descuenta el retiro del monto inicial
        self.assertEqual(self.cajero.realizar_retiro(1500),(5000-1500),"La operación de retiro no descuenta correctamente el monto del saldo inicial")

    def test_depositar(self):
        #Se comprueba que la operacion de deposito añade el deposito al monto inicial
        self.assertEqual(self.cajero.realizar_deposito(2343), (5000+2343), "La operación de depósito no añade correctamente el monto al saldo inicial")

    def test_deposito_minimo(self):
        #Se comprueba que el deposito no sea igual a una cantidad nula(0)
        self.assertFalse(self.cajero.deposito_minimo(0), "El depósito no debe ser igual a cero")
        #Se comprueba que el deposito no sea un valor negativo
        self.assertFalse(self.cajero.deposito_minimo(-450), "El depósito no debe ser un valor negativo")
        #Se comprueba que el deposito sea mayor a 0
        self.assertTrue(self.cajero.deposito_minimo(200), "El depósito debe ser mayor a cero")
    
    def test_deposito_maximo(self):
        #Se comprueba que el deposito sea menor al deposito maximo establecido(10000)
        self.assertTrue(self.cajero.deposito_maximo(5000), "El depósito es mayor al depósito máximo establecido")
        #Se comprueba que el deposito no sea mayor al deposito maximo establecido(10000)
        self.assertFalse(self.cajero.deposito_maximo(15000), "El depósito excede el depósito máximo establecido")

    def test_ver_saldo(self):
        #Se comprueba que se muestra el saldo inicial por consola
        self.assertEqual(self.cajero.obtener_saldo(),5000,"El saldo inicial no se muestra correctamente")
        #Se comprueba que se muestra el saldo despues de haber hecho un deposito
        self.cajero.realizar_deposito(20)
        self.assertEqual(self.cajero.obtener_saldo(),5020,"El saldo después del depósito no se muestra correctamente")
        #Se comprueba que se muestra el saldo despues de haber hecho un retiro
        self.cajero.realizar_retiro(20)
        self.assertEqual(self.cajero.obtener_saldo(),5000)


if __name__ == '__main__':
    unittest.main()