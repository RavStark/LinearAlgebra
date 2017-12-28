from decimal import Decimal, getcontext

from Vector import Vector

getcontext().prec=30

class Line(object):
    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coeefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'
            if not is_initial_term:
                output += ' '
                constant = int(constant)
            output += ' = {}'.format(constant)

            return output

    @staticmethod
    def first_nonzero_index(iterable):
        #for k, item in enumerate(iterable):
        #   if not MyDecimal(item).is_near_zero():
        #        return k
        #raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)
        idx = 0
        for value in iterable.coordinates:
            if not MyDecimal(value).is_near_zero():
                return idx
            idx+=1
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)
    
    def set_basepoint(self):
        n = self.normal_vector
        c = self.constant_term
        basepoint_coords = ['0']*self.dimension

        initial_index = Line.first_nonzero_index(n)
        initial_coefficient = n.coordinates[initial_index]

        basepoint_coords[initial_index] = c/Decimal(initial_coefficient)
        self.basepoint = Vector(basepoint_coords)

    def isParallel(self, l):
        return self.normal_vector.isParallel(l.normal_vector)

    def isIntersection(self, l):
        try:
            A, B = self.normal_vector.coordinates
            C, D = l.normal_vector.coordinates
            k1 = float(self.constant_term)
            k2 = float(l.constant_term)

            x = (D * k1 - B * k2) / (A * D - B * C)
            y = (-C * k1 + A * k2) / (A * D - B * C)
            return Vector([x, y])
        except ZeroDivisionError:
            return None

    def __eq__(self, l):

        if not self.isParallel(l):
            return False
        n1 = self.normal_vector.normalized()
        n2 = l.normal_vector.normalized()
        diff = n1 - n2
        return diff.isOrthogonal(self.normal_vector)
        
class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
                
lt = Line(Vector([2,2]), 3)
lt2 = Line(Vector([4,4]), 1)

l1 = Line(Vector([4.046,5.836]), 1.21)
l2 = Line(Vector([10.115,7.09]), 3.025)
print l1.isIntersection(l2)
l3 = Line(Vector([7.204,3.182]), 8.68)
l4 = Line(Vector([8.172,4.114]), 9.883)
print l3.isIntersection(l4)
l5 = Line(Vector([1.182,5.562]), 6.744)
l6 = Line(Vector([1.773,8.343]), 9.525)
print l5.isIntersection(l6)

