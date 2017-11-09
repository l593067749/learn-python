# -*- coding: UTF-8 -*-
class Cat(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def call(self):
        print 'Cat:hello'