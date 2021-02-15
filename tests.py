import unittest
import enigma

    '''
                      1         2
            01234567890123456789012345
            ABCDEFGHIJKLMNOPQRSTUVWXYZ
            EKMFLGDQVZNTOWYHXUSPAIBRCJ
    '''



abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotor_types={
    "I": ("UWYGADFPVZBECKMTHXSLRINQOJ", "Q"),
    "II": ("AJPCZWRLFBDKOTYUQGENHXMIVS", "E"),
    "III": ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    "IV": ("TAGBPCSDQEUFVNZHYIXJWLRKOM", "J"),
    "V": ("QCYLXWENFTZOSMVJUDKGIARPHB", "Z"),
    "VI": ("SKXQLHCNWARVGMEBJPTYFDZUIO", "ZM"),
    "VII": ("QMGYVPEDRCWTIANUXFKZOSLHJB", "ZM"),
    "VIII": ("QJINSAYDVKBFRUHMCPLEWZTGXO", "ZM"),
}
reflector_types= {
    'D': "ZXWVUTSRQYPONMLKIHGFEDCBJA",
    'Bfine': 'ENKQAUYWJICOPBLMDXZVFTHRGS',
    'Cfine': 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'
}
r = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
UKW = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ",
       "ZXWVUTSRQYPONMLKIHGFEDCBJA"]
Bfine = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ",
         "ENKQAUYWJICOPBLMDXZVFTHRGS"]
Cfine = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ",
         "RDOBJNTKVEHMLFCWZAXGYIPSUQ"]


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
        
        self.assertEqual(maquina.codifica("HOLA"), "LCHD")
        self.assertEqual(maquina.ini, "DAA")





if __name__== '__main__':
    unittest.main()