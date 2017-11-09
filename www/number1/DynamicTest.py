# -*- coding: UTF-8 -*-
'动态创建类 type 和 metaclass'
def helloWord(self,name='world'):
    print 'Hello,%s' % name

'''
要创建一个class对象，type()函数依次传入3个参数：

class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数helloWord绑定到方法名hello上。

'''

Hello=type('Hello',(object,),dict(hello=helloWord))
h=Hello()
print h.hello()

# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)#增加了一个add方法,原list没有add
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类

'''
当我们写下__metaclass__ = ListMetaclass语句时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

__new__()方法接收到的参数依次是：

1.当前准备创建的类的对象；

2.类的名字；

3.类继承的父类集合；

4.类的方法集合。

'''
l=MyList()
l.add(1)
print l
