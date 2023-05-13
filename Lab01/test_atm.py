import unittest
from atm import Cajero

class CajeroTest(unittest.TestCase):
  def setUp(self):
      self.cajero = Cajero()
  
  def test_retiro_saldo_suficiente(self):
      self.assertTrue(self.cajero.validar_retiro(5000))

  def test_retiro_saldo_insuficiente(self):
      self.assertFalse(self.cajero.validar_retiro(5001))

  def test_retiro_maximo(self):
      self.assertTrue(self.cajero.retiroMaximo(2000))
      self.assertFalse(self.cajero.retiroMaximo(4000))
  
  def test_depositar(self):
      self.assertEqual(self.cajero.realizar_deposito(2343), (5000+2343))

  def test_deposito_maximo(self):
      self.assertTrue(self.cajero.depositoMaximo(5000))
      self.assertFalse(self.cajero.depositoMaximo(15000))

  def test_ver_saldo(self):
      self.assertEqual(self.cajero.obtener_saldo(),5000)
      self.cajero.realizar_deposito(20);
      self.assertEqual(self.cajero.obtener_saldo(),5020)
      self.cajero.realizar_retiro(20);
      self.assertEqual(self.cajero.obtener_saldo(),5000)


if __name__ == '__main__':
    unittest.main()
