import random

class Rotor_():

    def __init__(self, abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario = abecedario
        self.rotor = []
        self.ix = 0
        otrasLetras = list(self.abecedario)
        for l in self.abecedario:
            n = random.randrange(len(otrasLetras))
            self.rotor.append((l, otrasLetras[n]))
            otrasLetras.pop(n)

        self.rotorC = self.rotor[:]
        

    def codifica(self, letra):
        pLetra = self.abecedario.index(letra)
        return self.rotorC[pLetra][1]
        self.avanza()

        #raise ValueError("{} no pertenece al abecedario".format(letra))



    def posicionInicial(self, letra):
        position = self.abecedario.index(letra)
        self.rotorC = self.rotor[position:] + self.rotor[:position]

    def avanza(self):
        self.rotorC = self.rotorC[1:] + self.rotorC[0]


class Reflector():
    '''
        TODO:
            - Configuración: lista de pares del abecedario
              solo se repite uno si la longitud es impar
              es biunivoca
            - refleja(letra_entrada) -> letra  
    '''    

    def __init__(self, conf=["ABCDEFGHIJKLMNÑOPQRSTUVWXYZ","ZYXWVWTSRQPOÑNMLKJIHGFEDCBA"]):
        '''
            si conf viene vacio, crear uno (abecedario)
            si conf viene lleno, comprobar que cumple las especificaciones
        '''
        self.configuracion = conf



    def refleja(self, letra_entrada):
        posE = self.configuracion[0].index(letra_entrada)
        return self.configuracion[1][posE]


class Rotor():
    '''
        TODO:
            - Conexion: Lista de cadenas (abecedario, cortocircuito) que 
              determina la entrada y salida según el caracter de salida o entrada
            - Posicion: Indice/caracter en posición cero de la conexión
            - Pasos ¿?: Número de pasos girados desde que empezamos a codificar
            - Salto: Indice, caracter de abecedario en que se obliga al salto del 
              siguiente rotor si lo hubiera
            - swSalto ¿?: True o False
            - codifica(indice): Devuelve el pin de salida
            - decodifica(indice): Devuelve el pin de entrada
            - avanza(): Rota una posición la conexión. Comprueba si debe activar swSalto 
    '''
    def __init__(self, abecedario, cortocircuito=None):
        self.conexion = [abecedario, cortocircuito]
        self._pos_ini = None

    def codifica(self, indice):
        letra = self.conexion[0][indice]
        indice_izda = self.conexion[1].index(letra)
        return indice_izda

    def decodifica(self, indice):
        letra = self.conexion[1][indice]
        indice_dcha = self.conexion[0].index(letra)
        return indice_dcha

    @property
    def pos_ini(self):
        return self._pos_ini

    @pos_ini.setter
    def pos_ini(self, value):
        self._pos_ini = self.conexion[0].index(value)

class Enigma():
    pass
    '''
    TODO:
        - reflector: su configuración prefijada en principio
        - rotor: su conexión prefijada en principio
        - posi_inicial: Letra inicial del rotor (indice?)
        - codifica(mensaje): Transforma el mensaje en uno nuevo. Solo hay una dirección.
          Si se pasa la salida de codifica como entrada volviendo la posi_inicial. Obtenemos
          la otra entrada. 
    '''