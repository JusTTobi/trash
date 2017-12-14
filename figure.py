#!/usr/bin/python3
import math
class Figure():
    sum_id=0
    sum_id_del=0
    def __init__(self, a, n):
        self.a, self.n = self.check(a, n)
        self.id_add()
        self.id = self.sum_id

    @staticmethod
    def check(a, n):
        if not ((type(a) is int) or (type(a) is float)) or a < 0:
            raise ValueError('Incorrect a!')
        if type(n) is not int or not (n == 0 or n > 2):
            raise ValueError('Incorrect n!')
        return a, n

    @classmethod
    def id_add(cls):
        cls.sum_id+=1

    @classmethod
    def id_del(cls):
        cls.sum_id_del+=1

    def set_params(self, a, n):
        self.a, self.n = self.check(a, n)

    def get_params(self):
        return self.a, self.n

    def print_id(self):
        print("""Экземпляров класса {0:s} создано - {1:d}
Экземпляров класса {0:s} удалено - {2:d}
id экземпляра - {3:d}""".format(
        self.__class__.__name__, self.sum_id, self.sum_id_del, self.id))

    def area(self):
        if self.n == 0:
            s = math.pi*(self.a**2)
        else:
            s = ((self.n*self.a**2)/4)*(1/(math.tan(math.pi/self.n)))
        return s

    def __str__(self):
        if self.n == 0:
            return "Круг радиусом " + str(self.a)
        elif self.n == 3:
            return "Равносторонний треугольник со стороной " + str(self.a)
        elif self.n == 4:
            return "Квадрат со стороной " + str(self.a)
        else:
            return "Равносторонний {:d}-угольник со стороной ".format(self.n) + str(self.a)

    def __eq__(self, other):
         return self.n == other.n and self.a == other.a

    def __repr__(self):
       return super().__repr__() + ' >>> ' + self.__str__()

    def __del__(self):
        self.id_del()
