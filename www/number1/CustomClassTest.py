# -*- coding: UTF-8 -*-
'定制类'
class CustomClassTest(object):

    def __init__(self):
        self.name="custom"

    def __str__(self):
        return "custome{name:%s}" % self.name

    __repr__ = __str__ #java toString()

    def __call__(self, *args, **kwargs):#实例化自己调用的方法
        print "this is call()"

    def __getattr__(self, attr):#在没有找到属性的情况下，才调用__getattr__，已有的属性
        if attr=='score':
            return 99

custom=CustomClassTest()
print custom
print custom()
print custom.score