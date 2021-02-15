original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def reordena(abc):
    resultado = [' ']*len(original)
    for ix, letra in enumerate(original):
        nuevaletra = abc[ix]
        pos = original.index(nuevaletra)
        resultado[pos]=letra

    return ''.join(resultado)