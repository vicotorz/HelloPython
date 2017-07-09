#!/usr/bin/python
# -*- coding:UTF-8-*-
import random
import random
import re



# 字符串函数
def demo_string():
    strs = "hello world"
    print strs.capitalize()
    print strs.replace("world", "zhangdi")
    print 1, strs.lstrip()
    print 2, strs.rstrip()
    print strs.startswith("hello")
    print strs.endswith("world")
    print len(strs)
    print '-'.join(['a', 'b', 'c'])
    print strs.split(" ")
    print strs.find('ll')


# 操作符运算
def demo_operation():
    print 1 + 2, 3 - 1, 4 * 2, 5 / 6
    print True,not False
    print 1<<2, 55>>2
    print 5|3,5&3,5^3
    x=3
    print type(x)



#内置函数
def demo_buildinfunction():
   print max(5,3)
   print len("xxx")
   print abs(-2)
   print range(1,10,3)#每隔3个取数
   print dir(list)
   x=7
   print eval('x+2')#执行某一段文本
   print chr(65),ord('a')
   print divmod(6,4)

#控制流
def demo_controlflow():
    a=3
    b=4
    if a>b:
        print 'hi'
    else:
        print 'no hi'

    for i in range(0,10,1):
        print i

#list
def demo_list():
    list=[1,2,3]
    print list
    lista=[4]
    list.append(lista)
    print list
    print len(list)
    print '4' in list
    list.insert(0,'w')
    print list
    list.pop(1)
    print list
    list.sort()
    print list
    print list[1]
    print list*2

    tuple=(1,2,3)
    print tuple
    print tuple.count(1)

def add(a,b):
    return a+b

#dic
def demo_dic():
    dic={1:'value',2:'rrr'}
    print dic
    print dic.keys()
    print dic.values()
    for key,value in dic.items():
        print key,value

    #函数指针
    dict={'+':add}
    print dict['+'](5,3)
    del dict['+']
    print dict
    #加入
    dict['x']='y'
    print dict['x']

#demo_set
def demo_set():
    listA=(1,2,3)
    setA=set(listA)
    print setA
    listB=(2,3,4)
    setB=set(listB)

    print setA&setB,setA|setB,setA-setB
    print setA.union(setB)


#面向对象
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return self.name

class Admin(User):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return self.name

def demo_obj():
    user1=User("vic",1)
    print user1
    user2=Admin("qiqi",5)
    print user2


#异常
def demo_exception():
    try:
        6/0
        raise Exception('hello exception',"errir")
    except Exception as e:
        print "异常"
        print e
    finally:
        print "finally"

#随机数
def demo_random():
    random.seed(1)
    print random.randint(0,100)
    print random.random()
    print random.choice(range(0,10,5))
    print random.sample(range(0,100,10),5)
    listA=[1,2,3,4,5]
    random.shuffle(listA)
    print listA

#正则表达式
def demo_pattern():
    str="123dfgg56ett12"
    pl= re.compile("123")
    print pl.findall(str)

if __name__ == '__main__':
    demo_string()
    demo_operation()
    demo_buildinfunction()
    demo_controlflow()
    demo_list()
    demo_dic()
    demo_set()
    demo_obj()
    demo_exception()
    demo_random()
    demo_pattern()

