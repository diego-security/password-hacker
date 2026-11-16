import unittest
import string

from main import generar_contrasena
from zxcvbn import zxcvbn


class TestPasswordHacker(unittest.TestCase):

    def test_longitud_segura(self):
        password = generar_contrasena(16)
        self.assertEqual(len(password), 16)

    def test_longitud_muy_segura(self):
        password = generar_contrasena(20)
        self.assertEqual(len(password), 20)

    def test_longitud_mega_segura(self):
        password = generar_contrasena(28)
        self.assertEqual(len(password), 28)

    def test_tiene_minusculas(self):
        password = generar_contrasena(20)
        self.assertTrue(any(c in string.ascii_lowercase for c in password))

    def test_tiene_mayusculas(self):
        password = generar_contrasena(20)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))

    def test_tiene_numeros(self):
        password = generar_contrasena(20)
        self.assertTrue(any(c in string.digits for c in password))

    def test_tiene_simbolos(self):
        password = generar_contrasena(20)
        simbolos = "!@#$%^&*()-_=+?"
        self.assertTrue(any(c in simbolos for c in password))

    def test_analizador_funciona(self):
        resultado = zxcvbn("pepito123")
        self.assertIn(resultado["score"], range(5))


if __name__ == "__main__":
    unittest.main()