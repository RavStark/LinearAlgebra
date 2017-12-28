from decimal import Decimal, getcontext

from Vector import Vector

getcontext().prec=30

class Plane(object):
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
        basepoint_coords = [0]*self.dimension

        initial_index = Plane.first_nonzero_index(n)
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
        n1 = self.basepoint
        n2 = l.basepoint
        diff = n1 - n2
        return diff.isOrthogonal(self.basepoint)
        
class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
                


l1 = Plane(Vector([-0.412,3.806,0.728]), -3.46)
l2 = Plane(Vector([1.03,-9.515,-1.82]), 8.65)
print l1.isParallel(l2)
print l1==l2

l3 = Plane(Vector([2.611,5.528,0.283]), 4.6)
l4 = Plane(Vector([7.715,8.306,5.342]), 3.76)
print l3.isParallel(l4)
print l3==l4

l5 = Plane(Vector([-7.926,8.625,-7.212]), -7.952)
l6 = Plane(Vector([-2.642,2.875,-2.404]), -2.443)
print l5.isParallel(l6)
print l5==l6
