import unittest

from security import validar_password

class TestSecurity(unittest.TestCase):
	def test_password_curta(self):
		self.assertFalse(validar_password("12345"))
	def test_password_llarga(self):
		self.assertTrue(validar_password("contrasenyaSegura123"))

if __name__ == '__main__':
	unittest.main()
