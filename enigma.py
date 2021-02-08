import random

def miFuncionCreaAbecedario():
    pass

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

    def validate_conf(self, conf):
        if ''.join(sorted(list(conf[0]))) != ''.join(sorted(list(conf[1]))):
            raise AttributeError('Reflector inconsistente')
        elif conf[0] != conf[1][::-1]:
            raise AttributeError('Reflector no simétrico')


    def __init__(self, conf=["ABCDEFGHIJKLMNÑOPQRSTUVWXYZ","ZYXWVWTSRQPOÑNMLKJIHGFEDCBA"]):
        '''
            si conf viene vacio, crear uno (abecedario)
            si conf viene lleno, comprobar que cumple las especificaciones
        '''
        self.validate_conf(conf)
        self.configuracion = conf



    def refleja(self, pin):
        letra = self.configuracion[0][pin]
        return self.configuracion[1].index(letra)


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
    def __init__(self, abecedario, cortocircuito, paso=None):
        self.abecedario = abecedario 
        self.cortocircuito = cortocircuito

        if ''.join(sorted(list(abecedario))) != ''.join(sorted(list(cortocircuito))):
            raise AttributeError('abecedario y cortocircuito incoherentes')

        if not paso:
            self.paso = self.abecedario[-1]
        else:
            self.paso = paso

        self._pos_ini = 0

    def codifica(self, indice):
        letra = self.abecedario[(indice + self._pos_ini) % len(self.abecedario)]
        indice_izda = self.cortocircuito.index(letra)
        indice_izda = (indice_izda - self._pos_ini) % len(self.abecedario)
        return indice_izda

    def decodifica(self, indice):
        letra = self.cortocircuito[(indice + self._pos_ini) % len(self.abecedario)]
        indice_dcha = self.abecedario.index(letra)
        indice_dcha = (indice_dcha - self._pos_ini) % len(self.abecedario)
        return indice_dcha

    def avanza(self):
        self._pos_ini = (self._pos_ini + 1) % len(self.abecedario)
        return self.pos_ini in self.paso


    @property
    def pos_ini(self):
        return self.abecedario[self._pos_ini]

    @pos_ini.setter
    def pos_ini(self, value):
        self._pos_ini = self.abecedario.index(value)

class Enigma():
    def __init__(self, rotores, reflector, ini=None):
        self.rotores = rotores
        self.reflector = reflector

        self.abecedario = self.rotores[0].abecedario
        for rotor in self.rotores:
            if rotor.abecedario != self.abecedario:
                raise AttributeError('{} no es igual al abecedario de la maquina: {}'.format(rotor.abecedario, self.abecedario) )
    
        alfareflector = self.reflector.configuracion[0]
        if ''.join(sorted(list(alfareflector))) != ''.join(sorted(list(self.abecedario))):
                raise AttributeError('{} no es igual al abecedario de la maquina: {}'.format(self.reflector.configuracion[0], self.abecedario) )

        if not ini:
            self.ini = self.rotores[0].abecedario[0]*len(self.rotores)
        else:
            self.ini = ini


    def codifica(self, frase):
        frase_output = ""
        for letra in frase:
            input = self.abecedario.index(letra)
            _next = True
            for rotor in self.rotores:
                if _next:
                    _next = rotor.avanza()
                input = rotor.codifica(input)

            output = self.reflector.refleja(input)

            for rotor in self.rotores[::-1]:
                output = rotor.decodifica(output)

            frase_output += self.abecedario[output]
        return frase_output

    @property
    def ini(self):
        return self._ini

    @ini.setter
    def ini(self, value):
        self._ini = value
        for ix, rotor in enumerate(self.rotores):
            rotor.pos_ini = self._ini[ix]






    '''
    TODO:
        - reflector: su configuración prefijada en principio
        - rotor: su conexión prefijada en principio
        - posi_inicial: Letra inicial del rotor (indice?)
        - codifica(mensaje): Transforma el mensaje en uno nuevo. Solo hay una dirección.
          Si se pasa la salida de codifica como entrada volviendo la posi_inicial. Obtenemos
          la otra entrada. 
    '''

