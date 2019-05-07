from coordenada2 import *

class rectangulo():
    
    def __init__(self):
        self.p1 = coordenada() #p1, va a tener los atributos de coordenada igual que p2#
        self.p2 = coordenada()
        self.area = 0

    def setcoordenadas(self, p, q):
        self.p1 = p
        self.p2 = q

    def calculararea(self):
        p3 = coordenada()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.area = p3.distancia(self.p1) * p3.distancia(self.p2)
