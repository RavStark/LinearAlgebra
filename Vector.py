import math
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

    def __mul__(self, v):
        coords = [x * v for x in self.coordinates]
        return Vector(coords)

    def magnitude(self):
        coords = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coords))

    def normalized(self):
        try:
            coords = self.magnitude()
            return self * (1/coords)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dotProduct(self, v):
        result = [a * b for a,b in zip(self.coordinates,v.coordinates)]
        return sum(result)

    def angle(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            result = u1.dotProduct(u2)
            if result > 1.0 and result < 1 + 1e-5:
                result = 1
            a = math.acos(result)
            print a
            if in_degrees:
                return a * 180./pi
            else:
                return a
        except ZeroDivisionError:
            raise Exception('Cannot find angle with a zero vector')

    def isParallel(self, v):
        return (self.isZero() or v.isZero() or self.angle(v) == 0 or self.angle(v) == math.pi)
        

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
    

