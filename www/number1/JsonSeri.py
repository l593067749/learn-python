# -*- coding: utf-8 -*-
import json

class Student(object):
    def __init__(self,name,age,score):
        self._name=name
        self.age=age
        self.score=score

def number01():
    d=dict(name='zhangsan',age=20,score=99)
    str=json.dumps(d)
    print str
    print json.loads(str,"utf8")

number01()


# 自定义转换
def dict2student(d):
        return Student(d['_name'], d['age'], d['score'])

def number02():
    s=Student('lisi',15,100)
    str=json.dumps(s,default=lambda obj:obj.__dict__)
    print str
    d=json.loads(str)
    print d['age'],d['score'],d ['_name']
    d2=json.loads(str,object_hook=dict2student)
    print d2.age

number02()