import random


letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def CreaRotor():
    resultado = ''
    for l in letras:
        n = random.randrange(len(letras))
        if letras[n] in resultado:
            pass
        else:
            resultado += letras[n]
    return resultado


def CreaRotorM():
    resultado = []
    otrasLetras = list(letras)
    for l in letras:
        n = random.randrange(len(otrasLetras))
        resultado.append((l, otrasLetras[n]))
        otrasLetras.pop(n)
    return resultado

r = CreaRotorM()