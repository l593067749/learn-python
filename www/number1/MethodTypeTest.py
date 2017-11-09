# -*- coding: UTF-8 -*-
'给实例或类绑定方法'
from types import MethodType

class MethodTypeTest(object):
    __slots__ = ('setName','name','age') # 用tuple定义允许绑定的属性(方法)名称
    pass

def setName(self,name):
    self.name=name

methodTypeTest=MethodTypeTest()
methodTypeTest.setName=MethodType(setName,methodTypeTest,MethodTypeTest)#给实例绑定方法，作用范围仅为该实例
methodTypeTest.setName("new name")
print methodTypeTest.name

#其他实例引用就会报错
'''
m2=MethodTypeTest()
m2.setName("new name")
print m2.name

'''
#类绑定
MethodTypeTest.setName=MethodType(setName,None,MethodTypeTest)
m2=MethodTypeTest()
m2.setName("new m2")
print m2.name