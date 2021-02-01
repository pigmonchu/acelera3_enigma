from enigma import *

rotor_pruebas = [('A', 'Ñ'), ('B', 'M'), ('C', 'H'), ('D', 'C'), ('E', 'K'), ('F', 'W'), 
                 ('G', 'N'), ('H', 'O'), ('I', 'J'), ('J', 'F'), ('K', 'Z'), ('L', 'E'), 
                 ('M', 'P'), ('N', 'S'), ('Ñ', 'U'), ('O', 'B'), ('P', 'G'), ('Q', 'R'), 
                 ('R', 'X'), ('S', 'A'), ('T', 'I'), ('U', 'Q'), ('V', 'T'), ('W', 'V'), 
                 ('X', 'Y'), ('Y', 'L'), ('Z', 'D')]

("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ", "ÑMHCKWNOJFZEPSUBGRXAIQTVYLD")
r = Rotor()
r.rotor = rotor_pruebas

print(r.codifica('S'))

r.posicionInicial('S')
print(r.rotorC)

'''
[('A', 'Ñ'), ('B', 'M'), ('C', 'H'), ('D', 'C'), ('E', 'K'), ('F', 'W'), 
('G', 'N'), ('H', 'O'), ('I', 'J'), ('J', 'F'), ('K', 'Z'), ('L', 'E'), 
('M', 'P'), ('N', 'S'), ('Ñ', 'U'), ('O', 'B'), ('P', 'G'), ('Q', 'R'), 
('R', 'X'),('S', 'A'), ('T', 'I'), ('U', 'Q'), ('V', 'T'), ('W', 'V'), 
('X', 'Y'), ('Y', 'L'), ('Z', 'D') ]
'''
