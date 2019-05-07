from coordenada2 import *

class rectangulo():
    
    def __init__(self):
        self.p1 = coordenada() #p1, va a tener los atributos de coordenada igual que p2, que son X y Y#
        self.p2 = coordenada()
        self.area = 0

    def setcoordenadas(self, p, q):
        self.p1 = p
        self.p2 = q

    def calculararea(self):
        p3 = coordenada()
        p3.x = self.p1.x #x de p3 va a ser igual al x de p1#
        p3.y = self.p2.y #y de p3 va a ser igual al y de p2# 
        self.area = p3.distancia(self.p1) * p3.distancia(self.p2)#el area es el producto entre las distancias entre (p3 y p1) y (p3 y p2)#
