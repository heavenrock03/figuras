from math import *
class coordenada():
    def __init__(self):
        self.x=0 #x, y, son dos objetos de la clase coordenada#
        self.y=0
        
    def distancia(self,coordenada):
        return sqrt((self.x - coordenada.x)**2 + (self.y - coordenada.y)**2)
        
        
