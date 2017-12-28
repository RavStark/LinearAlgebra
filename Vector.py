import math
from decimal import Decimal, getcontext

getcontext().prec=3

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        coords = [sum(t) for t in zip(self.coordinates,v.coordinates)]
        return Vector(coords)

    def __sub__(self, v):
        coords = [x-y for (x,y) in zip(self.coordinates,v.coordinates)]
        return Vector(coords)

    def times_scalar(self, v):
        coords = [x * v for x in self.coordinates]
        return Vector(coords)

    def magnitude(self):
        coords = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coords))

    def normalized(self):
        try:
            coords = self.magnitude()
            return self.times_scalar(1./coords)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dotProduct(self, v):
        return sum([a * b for a,b in zip(self.coordinates,v.coordinates)])

    def angle(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            result = u1.dotProduct(u2)
            a = math.acos(result)
            print a
            if in_degrees:
                return a * 180./pi
            else:
                return a
        except ZeroDivisionError:
            raise Exception('Cannot find angle with a zero vector')

    def isParallel(self, v, tolerance=1e-7):
        return (self.isZero() or v.isZero() or abs(self.angle(v)) < tolerance or self.angle(v) == math.pi)
        

    def isOrthogonal(self, v, tolerance=1e-10):
        return abs(self.dotProduct(v)) < tolerance

    def isZero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def projOn(self, v):
        normV = v.normalized()
        projMagnitude = self.dotProduct(normV)
        return normV * projMagnitude
        
    def perpOn(self, v):
        p = self.projOn(v)
        return self - p
    
    def crossProduct(self, v):
        if self.dimension != 3 or v.dimension != 3:
            raise Exception('Dimension uncorrect to produce cross product')
        coords = []
        coords.append(self.coordinates[1] * v.coordinates[2] - self.coordinates[2] * v.coordinates[1])
        coords.append(self.coordinates[2] * v.coordinates[0] - self.coordinates[0] * v.coordinates[2])
        coords.append(self.coordinates[0] * v.coordinates[1] - self.coordinates[1] * v.coordinates[0])
        return Vector(coords)

v1 = Vector([8.462,7.893,-8.187])
v2 = Vector([6.984,-5.975,4.778])
print v1.crossProduct(v2)
