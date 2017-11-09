# -*- coding: UTF-8 -*-

from Cat import Cat
from Animal import Animal
'import module 和 from module import，区别是前者所有导入的东西使用时需加上模块名的限定，而后者不要。'
class BigCat(Cat,Animal):
    def __init__(self,name,age,weight,priName="tomCat"):
        Cat.__init__(self,name,age)
        self.weight=weight
        self.__priName=priName#__前缀表示是私有属性，不允许外部访问
    def animalCall(self):
        print '-------------'
        Animal.call(self)
        print '----------------'
    def catCall(self):
        print '-------------'
        Cat.call(self)
        print '----------------'
    def getPriName(self):
        return self.__priName

cat=BigCat("大猫TOM",5,50)
cat.animalCall()
cat.catCall()
print cat.weight
print cat.getPriName()
print isinstance(cat,Cat)#判断对象是否是某种类型
print hasattr(cat,"x")
setattr(cat,"x","我是x")
print hasattr(cat,"x")
print getattr(cat,"x")
