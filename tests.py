import unittest
import enigma


abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotor_types={
    "I": ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    "II": ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    "III": ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    "IV": ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    "V": ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
    "VI": ("JPGVOUMFYQBENHZRDKASXLICTW", "ZM"),
    "VII": ("NZJHGRCXMYSWBOUFAIVLPEKQDT", "ZM"),
    "VIII": ("FKQHTLXOCBJSPDZRAMEWNIUYGV", "ZM"),
}
r = "ABCDEFGHIJKLMNOPYQRSTUVWXZ"
UKW = ["ABCDEFGHIJKLMNOPYQRSTUVWXZ", r[::-1]]

class ReflectorTest(unittest.TestCase):
    def test_reflejaOK(self):
        reflector = enigma.Reflector(UKW)
        self.assertEqual(reflector.refleja(0), 25)

    def test_crea_con_error(self):
        with self.assertRaises(AttributeError):
            reflector = enigma.Reflector(conf=['AAB', 'BCA'])
        

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

class EnigmaTest(unittest.TestCase):
    def test_creaEnigmaOk(self):
        rotor = enigma.Rotor(abecedario, rotor_types['I'][0], rotor_types['I'][1])
        rotor.ini = 'K'
        reflector = enigma.Reflector(conf=UKW)
        maquina = enigma.Enigma(rotores=[rotor], reflector=reflector)

        self.assertEqual(maquina.ini, "A")
        self.assertEqual(rotor.pos_ini, "A")

    def test_cambia_ini(self):
        rotor = enigma.Rotor(abecedario, rotor_types['I'][0], rotor_types['I'][1])
        rotor.ini = 'K'
        reflector = enigma.Reflector(conf=UKW)
        maquina = enigma.Enigma(rotores=[rotor], reflector=reflector, ini="C")

        self.assertEqual(maquina.ini, "C")
        self.assertEqual(maquina.rotores[0].pos_ini, "C")

        maquina.ini = "T"
        self.assertEqual(maquina.ini, "T")
        self.assertEqual(maquina.rotores[0].pos_ini, "T")

    def test_creaEnigmaErrores(self):
        with self.assertRaises(AttributeError) as e:
            rotor = enigma.Rotor(abecedario, rotor_types['I'][0]+'Ñ', rotor_types['I'][1])

        rotor = enigma.Rotor(abecedario, rotor_types['I'][0], rotor_types['I'][1])
        rotor.ini = 'K'
        reflector = enigma.Reflector(conf=['ABC', 'CBA'])

        with self.assertRaises(AttributeError):
            maquina = enigma.Enigma(rotores=[rotor], reflector=reflector)


    def test_codifica_frase(self):
        rotor1 = enigma.Rotor(abecedario, rotor_types['I'][0], rotor_types['I'][1])
        rotor2 = enigma.Rotor(abecedario, rotor_types['I'][0], rotor_types['I'][1])
        rotor3 = enigma.Rotor(abecedario, rotor_types['I'][0], rotor_types['I'][1])
        reflector = enigma.Reflector(UKW)

        maquina = enigma.Enigma([rotor1, rotor2, rotor3], reflector=reflector, ini='ZAA')
        
        self.assertEqual(maquina.codifica("HOLA"), "LHCD")





if __name__== '__main__':
    unittest.main()