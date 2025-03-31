'''
Escarlet Zapana
30/03/25
AlgebraVectorial
'''
import math
class Vector:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    #suma de vectores
    def __add__(self, other):
        x1=self.x+other.x
        y1=self.y+other.y
        z1=self.z+other.z
        return Vector(x1,y1,z1)
    #multiplicacion
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x1 = self.x * other
            y1 = self.y * other
            z1 = self.z * other
            return Vector(x1, y1, z1)
        elif isinstance(other, Vector):
            x1 = self.x * other.x
            y1 = self.y * other.y
            z1 = self.z * other.z
            if (x1+y1+z1)==0:
                return f"un vector ortogonal"
            else:
                return Vector(x1, y1, z1)
        else:
            return False

    def __sub__(self,other):
        x1=self.y*other.z-self.z*other.y
        y1=self.z*other.x-self.x*other.z
        z1=self.x*other.y-self.y*other.x
        return Vector(x1,y1,z1)
    #longitud  de vector
    def __pow__(self,dos=0):
        r=math.sqrt(self.x**dos+self.y**dos+self.z**dos)
        return r
    #normal de un vector
    def __truediv__(self,other):
        x1=self.x/other
        y1=self.y/other
        z1=self.z/other
        return Vector(x1,y1,z1)
    def __str__(self):
        return "(x={},y={},z={})".format(self.x,self.y,self.z)

v1=Vector(5,4,2)
v2=Vector(-2,3,-1)
print(v1)
print(v2)
v3=v1+v2
print("el vector suma es",v3)
v4=v1*3
print("producto por un escalar",v4)
v5=v1-v2
print("producto vectorial",v5)
v6=v1**2
print("la longitud del vector es",v6)
v7=v1/v6
print("la normal es",v7)
v8=v1*v2
print("el producto de dos vectores es ",v8)
