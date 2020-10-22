# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:31:42 2020

@author: Nika
"""
import numpy as np


'''
#класс-это контейнер, который имеет атрибуты и методы. когда определяем класс мы определяем тип.
class MyClass():
    attr=100
    def myMethod(self):
        print(self.attr)
# встроенные методы-конструктор. они начинаются с __ и зак
# init сщздание экземпляра класса
    def __init__(self,a):
        self.attr = a
        print(self.attr)
        
    def my_method(self,*b):
        for i in b:
            print(i)


inst_1 =MyClass(100)
inst_2 = MyClass(1000)
#inst.my_method(1,2,4)
#print(inst.attr)


class MyRational():
    def __init__(self, numerator, denumenator):
        self.num=numerator
        self.denom=denumenator
        
    
    def __str__(self):
        return str(self.num)+ ' / ' + str(self.denom)
    
    def __add__(self,inst):
        print(self)
        print(inst)
        return MyRational(self.num* inst.denom+self.denom*self.num, self.denom*inst.denom)
    
    def __mul__(self,inst):
        return MyRational(self.num*inst.num,self.denom*inst.denom)
    
    def __mul__(self,inst):
        if type(inst)==int:
            inst=MyRational(inst,1)
        return MyRational(self.num*inst.num,self.denom*inst.denom)

    def _rmul__(self,inst):
        if type(inst)==int:
            inst=MyRational(inst,1)
        return MyRational(self.num*inst.num,self.denom*inst.denom)
    def __matmul__(self,inst):
        print("something")
        return self*inst
        
rat_1 = MyRational(1,2)
rat_2 = MyRational(1,5)
print(rat_1+rat_2)
print(rat_1*rat_2)
print(rat_1 @ rat_2)
'''


#класс с трёх мерными векторами. (сложение==add,  вычитание==__sub__,
# умножение на число, 
#векторное умножение==__matmul__)==операторы overload, длина вектора,скаляр

class Vectors():
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c
        
    def __str__(self):
        return "(" + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    
    def __add__(self, other):
        return Vectors(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vectors(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def norm(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __matmul__(self, other):
        return Vectors(self.y*other.z - self.z*other.y,
                       - self.x*other.z + self.z*other.x,
                       self.x*other.y - self.y*other.x)
    
    def number(self, k):
        return Vectors(self.x * k, self.y * k, self.z * k)
    
    def scal(self, other):
        return (self.x*other.x + self.y*other.y + self.z*other.z)
    
    
v1 = Vectors(1, 1, 1)
v2 = Vectors(2, 2, 2)
print(v1 + v2)
print(v1 - v2)
print(v1.norm())
print(Vectors.number(v1, 5))
print(Vectors.scal(v1, v2))
print(v1 @ v2)