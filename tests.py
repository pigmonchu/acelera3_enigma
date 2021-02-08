import unittest
import enigma

class ReflectorTest(unittest.TestCase):
    def test_reflejaOK(self):
        reflector = enigma.Reflector()
        self.assertEqual(reflector.refleja('A'), 'Z')
        

class RotorTest(unittest.TestCase):
    def test_construyeOK(self):
        rotor = enigma.Rotor("ABCDEFG", "CFAGBDE")
        self.assertEqual(rotor.abecedario, "ABCDEFG")
        self.assertEqual(rotor.cortocircuito, "CFAGBDE")
        self.assertEqual(rotor.pos_ini, "A") 

    def test_codificaOK(self):
        rotor = enigma.Rotor("ABCDEFG", "CFAGBDE")
        self.assertEqual(rotor.codifica(0), 2)
        self.assertEqual(rotor.decodifica(4), 1)

    def test_codificaOK_con_pos_ini(self):
        rotor = enigma.Rotor("ABCDEFG", "CFAGBDE")
        rotor.pos_ini = "C"
        self.assertEqual(rotor.pos_ini, "C")
        self.assertEqual(rotor._pos_ini, 2)
        self.assertEqual(rotor.codifica(0), 5)
        self.assertEqual(rotor.decodifica(4), 2)

if __name__== '__main__':
    unittest.main()