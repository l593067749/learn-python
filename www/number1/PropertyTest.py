# -*- coding: UTF-8 -*-
'@property装饰器就是负责把一个方法变成属性调用的'
class PropertyTest(object):

    def __init__(self):
        self.__name='name'

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if(age<0):
            age=1
        self.__age=age

    

propertyTest=PropertyTest()
propertyTest.age=15
print "name:%s,age:%d" % (propertyTest.name, propertyTest.age)