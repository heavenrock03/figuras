from coordenada2 import *
from math import *

class circulo():
    
    def __init__(self):
        self.p1 = coordenada()
        self.p2 = coordenada()
        self.area = 0

    def setcoordenadas(self, p, q):
        self.p1 = p
        self.p2 = q

    def calculararea(self):
        self.area = ((self.p1.distancia(self.p2))**2) * pi
