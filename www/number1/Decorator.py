# -*- coding: UTF-8 -*-
import functools

def log(func):
    def wrapper(*args,**kw):
        print 'call %s():' % func.__name__
        return func(*args,**kw)
    return wrapper

def log2(text):
    def decorator(func):#接收func函数
        @functools.wraps(func)#wrapper.__name__ = func.__name__
        def wrapper(*args, **kw):# 接收所有函数
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log
def now():
    print "20171106"

print now.__name__

now()

@log2("execute")
def now2():
    print "20171106"

print now2.__name__

now2()
