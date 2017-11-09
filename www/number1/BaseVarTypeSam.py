# -*- coding: UTF-8 -*-
id = 1
name = "张三"
money = 150.24
sex = 0;
isB = sex == 1
# 特殊的空值
address = None
CREATE = "!@@!"
hobby = ['看书', '跑步', '吃']
# 增加
hobby.append("睡")
# 删除
hobby.pop(1)
# 元组 只读
alias = ("小黑", "灰子")
show = {"name": name, "id": id}


# *args 是只读，**kw是可变
def func(*args, **kw):
    print 'args=', args, 'kw=', kw


def showList(hobby2, show2):
    for val in hobby2:
        print val
        val=val+"--"

    for key, val in show2.iteritems():
        print 'key=', key, ';val=', val

# 列表生成式
def test02():
    # x*x(要生成的元素) 后面跟for循环，把list创建出来，后边可以加上if判断
    list = [x * x for x in range(1, 11) if x % 2 == 0]
    print list



# 生成器 循环的过程中创建后续的元素
def generatorTest():
    count=10
    g=(x*x for x in range(count))
    while(count>0):
        print g.next()
        count=count-1

def add(x):
    return x+x

def add2(x,y):
    return x+y

print id
print name
print money
print isB
print address
print CREATE
# 切片
print hobby[0:]
showList(hobby, show)
print len(hobby)
print alias[0]
print show.keys()
print show.values()
func(*alias, **show)
print "-----------------"
func(alias,show)
test02()
generatorTest()

# map() 函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
print map(add,[1,2,3])
# reduce() 把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算。
print reduce(add2,[1,2,3])
# filter() 用于过滤序列
def is_ood(n):
    return n%2==1

print filter(is_ood,[1,2,3,4])
# sorted
print sorted([36,23,10,25,6])
def reversed_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0
print sorted([36,23,10,25,6],reversed_cmp)


