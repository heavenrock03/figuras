class coordenada():
    def __init__(self):
        self.x1=0
        self.x2=0
        self.y1=0
        self.y2=0

    def distancia(self):
        return sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        
        
