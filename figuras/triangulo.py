from coordenada2 import *

class triangulo():
    
    def __init__(self):
        self.p1 = coordenada()
        self.p2 = coordenada()
        self.area = 0

    def setcoordenadas(self, p, q):
        self.p1 = p
        self.p2 = q

    def calculararea(self):
        p3 = coordenada()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.area = (p3.distancia(self.p1) * p3.distancia(self.p2))/2
