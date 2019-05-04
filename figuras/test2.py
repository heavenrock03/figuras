from coordenada2 import *
from rectangulo import *
from circulo import *
from triangulo import *
from cuadrado import *

p1 = coordenada()
p2 = coordenada()
p1.x = 1
p1.y = 4
p2.x = 5
p2.y = 2

r = rectangulo()
r.setcoordenadas(p1, p2)
r.calculararea()
print r.area

c = circulo()
c.setcoordenadas(p1, p2)
c.calculararea()
print c.area

t = triangulo()
t.setcoordenadas(p1, p2)
t.calculararea()
print t.area

cu = cuadrado()
cu.setcoordenadas(p1, p2)
cu.calculararea()
print t.area

