# -*- coding: UTF-8 -*-
' partial 偏函数的应用 '
__author__ ='Wenqiang Liao'
import functools

def say(name,base="我是"):
    print '%s:%s' %(base,name)

say("Tom")
say2=functools.partial(say,base="大家好，我是")
say2("Tom")