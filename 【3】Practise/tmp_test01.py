import math
import cmath
import random
# print(dir(math))
# print(dir(cmath))
# print('choice效果：', random.choice([1, 2, 35, 7]), random.choice('a string'))
# print('randrange效果：', random.randrange(100, 1000, 2))
# print('random效果：', random.random())
# print('randint效果：', random.randint(1, 10))
# print('uniform效果：', random.uniform(1.5, 5.5))

# print("\tI'm tabbed in.")
# print("I'm split\non a line.")
# print("I'm \\ a \\ cat.")
# a = "Hello"
# print('c'+'h'+'e'+'e'+'s'+'e')
# print("-"*20)
# print(a[1],'/',a[1:4])
# print("H" in a,'/',"M" not in a)
# print("连接多个字符串示例: %s 连接多个 %s 字符串 %s " % ('eyes', 'hair', 'teeth'))
# print("连接数字number用百分之%d" % 12)
# print("连接百分数用%.0d%%" % 100)
# print("%r %r %r %r" % ('one', 'two', 'three', 'four'))

# # 将元组转换为列表
# aTuple = (123, 'xyz', 'zara', 'abc')
# print(list(aTuple))
# # append()/extend()方法区别：
# aList = [123, 'xyz', 'zara', 'abc']
# aList.append('abc'), print(aList)
# aList.append([7, 8, 9]), print(aList)
# aList.extend([7, 8, 9]), print(aList)
# # append() 方法向列表的尾部添加一个新的元素
# # extend()方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中
# # 统计某个元素在列表中出现的次数
# print(aList.count(123), aList.count('abc'))
# # 从列表中找出某个值第一个匹配项的索引位置
# print(aList.index('zara'))
# # 将对象插入列表
# aList.insert(3, 2018), print(aList)
# # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# print(aList.pop(-4), aList.pop(-1))
# # 移除列表中某个值的第一个匹配项
# aList.remove('abc'), print(aList)
# # 反向列表中元素
# aList.reverse(), print(aList)

# #浅拷贝
# a = {1: [1, 2, 3]}
# b = a.copy()
# print('原始：%s,%s' % (a, b))
# a[1].append(4)  # 修改字典a
# print('修改后：%s,%s' % (a, b))  # 浅拷贝字典b也改变
# #深拷贝
# import copy
# c = copy.deepcopy(a)
# print('原始：%s,%s' % (a, c))
# a[1].append(5)  # 修改字典a
# print('修改后：%s,%s,%s' % (a, b, c))  # 深拷贝字典c不改变

# # dict.fromkeys(seq[, value])函数
# seq = ('Google', 'Runoob', 'Taobao')
# dict = dict.fromkeys(seq)
# print("新字典为 : %s" % str(dict))
# dict = dict.fromkeys(seq, 10)
# print("新字典为 : %s" % str(dict))

# # dict.get(key, default=None)函数
# dict = {'Name': 'Zara', 'Age': 27}
# print("Value : %s" % dict.get('Age'))
# print("Value : %s" % dict.get('Sex'))

# # dict.__contains__(key)/dict.has_key(key)函数(python3/2)
# print("Value : %s" % dict.__contains__('Age'))
# print("Value : %s" % dict.__contains__('Sex'))

# # dict.items()
# print("字典值 : %s" % dict.items())

# # dict.keys()/dict.values()
# dict = {'Name': 'Zara', 'Age': 7}
# print("Value : %s" % dict.keys())
# print("Value : %s" % dict.values())

# # dict.update(dict2)
# dict = {'Name': 'Zara', 'Age': 7}
# dict2 = {'Sex': 'female'}
# dict.update(dict2)
# print("Value : %s" % dict)

# # pop(key[,default])
# site = {'Name': 'Zara', 'Age': 7}
# pop_obj = site.pop('Name')
# print(pop_obj)

# # popitem()
# site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# pop_obj = site.popitem()
# print(pop_obj)
# print(site)

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# print('L[0:3] =', L[0:3])
# print('L[:3] =', L[:3])
# print('L[1:3] =', L[1:3])
# print('L[-2:] =', L[-2:])

# R = list(range(100))
# print('R =', R)
# print('R[:10] =', R[:10])
# print('R[-10:] =', R[-10:])
# print('R[10:20] =', R[10:20])
# print('R[:10:2] =', R[:10:2])
# print('R[::5] =', R[::5])


# print('list(range(1,10)) = ', list(range(1, 11)))
# print([x * x for x in range(1, 11)])
# print([x * x for x in range(1, 11) if x % 2 == 0])
# print([m + n for m in 'ABC' for n in 'XYZ'])
# print('+'*50)

# # 列出当前目录下的所有文件和目录名
# import os
# print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录
# print('+'*50)

# # 列表生成式也可以使用两个变量来生成list
# d = {'x': 'A', 'y': 'B', 'z': 'C'}  # 字典
# print([k + '=' + v for k, v in d.items()])
# print('+'*50)

# # list中所有的字符串变成小写
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])
# print('+'*50)

# # 生成器
# g = (x * x for x in range(5))
# for n in g:
#     print(n)
# print('+'*50)
# # 斐波拉契数列（Fibonacci）


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# print(fib(6))
# print('+'*50)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# g = fib(6)
# while True:
# 	try:
# 		x = next(g)
# 		print('g:', x)
# 	except StopIteration as e:
# 		print('Generator return value:', e.value)
# 		break


# n = 0
# results = []
# for t in triangles():
# 	print(t)
# 	results.append(t)
# 	n = n + 1
# 	if n == 10:
# 		break

# # 判断是否为迭代器
# from collections import Iterator
# print(isinstance((x for x in range(10)), Iterator))
# print(isinstance([], Iterator))
# print(isinstance({}, Iterator))
# print(isinstance('abc', Iterator))

# # Iterable转化为Iterator
# print(isinstance(iter([]), Iterator))
# print(isinstance(iter('abc'), Iterator))


# def f(x):
#     return x * x
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r), '\r', '+' * 50)

# s = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(s, '\r', '+' * 50)


# from functools import reduce


# def add(x, y):
#     return x + y


# def fn(x, y):
#     return x * 10 + y
# print(reduce(add, [1, 3, 5, 7, 9]), '\r', reduce(
#     fn, [1, 3, 5, 7, 9]))


# def is_odd(n):
#     return n % 2 == 1
# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# def main():
#     for n in primes():
#         if n < 1000:
#             print(n)
#         else:
#             break

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n


# def _not_divisible(n):
#     return lambda x: x % n > 0


# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)

# if __name__ == '__main__':
#     main()

# # 默认排序
# print(sorted([36, 5, -12, 9, -21]))
# # 使用key函数来实现自定义的排序
# print(sorted([36, 5, -12, 9, -21], key=abs))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# # 反向排序
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# 返回函数
# def lazy_sum(*args):
# 	def sum():
# 		ax=0
# 		for n in args:
# 			ax=ax+n
# 		return ax
# 	return sum
# f=lazy_sum(1,3,5,7,9)
# print(f)
# print(f())


# # 装饰器
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


# @log  # 把@log放到now()函数的定义处，相当于执行了语句now = log(now)
# def now():
#     print("20180817")
# f = now
# print(f())
# print(f.__name__)
# print('+' * 50)

# # 一个完整的decorator
# import functools


# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


# @log
# def now():
#     print("20180817")
# f = now
# print(f())
# print(f.__name__)
# print('+' * 50)

# # 或带参数的装饰器
# import functools


# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


# @log('execute')
# def now():
#     print("20180817")
# f = now
# print(f())
# print(f.__name__)
# print('+' * 50)

# import functools
# import time


# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         startTime = time.time() # 记录函数运行前的时间
#         result = fn(*args, **kw) # 执行函数，同时保留返回值
#         endTime = time.time() # 记录函数运行后的时间
#         print('%s executed in %s ms' % (fn.__name__, endTime-startTime))  # 输出装饰器的内容
#         return result # 返回函数的执行结果
#     return wrapper

# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')


# # 定义类Student


# class Student(object):
#     pass

# # 创建实例，根据student类创建出student的实例
# bart = Student()

# # 给实例变量绑定属性
# bart.name = 'bank'

# # 在创建实例时，通过__init__方法把必需的属性绑定上去，第一个参数永远是self，它表示创建的实例本身，可以把各种属性绑定到self


# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# # 类内部定义访问数据的函数，封装数据的函数和类本身关联起来就称为类的方法
# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def print_score(self):
#         print("%s,%s" % (self.name, self.score))

#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'

# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.print_score(), lisa.get_grade())
# print(bart.print_score(), bart.get_grade())

# # 如果要让内部属性不被外部访问，就在属性的名称前加上两个下划线__，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
# class Student(object):

#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score

#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))

# bart = Student('Bart Simpson', 59)
# print(bart.__name)

# # 如果外部代码要获取name和score，需要给Student类增加get_name和get_score这样的方法：
#     def get_name(self):
#         return self.__name

#     def get_score(self):
#         return self.__score

# # 如果又要允许外部代码修改score，就需要再给Student类增加set_score方法
#     def set_score(self, score):
#         self.__score = score

# # 需注意：在Python中，变量名类似__xxx__的，是特殊变量，特殊变量是可以直接访问的，不是private变量，
# # 所以不能用__name__、__score__这样的变量名作为属性命名。

# # 小习题
# class Student(object):

#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender

#     def get_gender(self):
#         return self.__gender

#     def set_gender(self, gender):
#         self.__gender = gender


# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')


# # 继承
# class Animal(object):

#     def run(self):
#         print("animal is runing.....")

# # Animal是父类，Cat/Dog是Animal子类


# class Cat(Animal):
#     pass


# class Dog(Animal):
#     pass

# a = Animal()
# dog = Dog()
# print(dog.run())
# cat = Cat()
# print(cat.run())

# # 多态


# class Dog(Animal):

#     def run(self):
#         print('Dog is running...')


# class Cat(Animal):

#     def run(self):
#         print('Cat is running...')
# b=Dog()
# print(b.run())
# c=Cat()
# print(c.run())

# print(isinstance(b, Dog))
# print(isinstance(b, Animal))
# print(isinstance(c, Cat))
# print(isinstance(c, Animal))
# print(isinstance(a, Dog))

# # 获取数据类型函数
# print(type(123), '///', type('asd'), '///', type(abs))
# print(type('123') == str, '///', type(123) ==
#       type('123'), '///', type('asd') == type('123'))
# print(isinstance([1, 2, 3], (list, tuple)))

# import types


# def fn():
#     pass
# print(type(fn), '///', type(fn) == types.FunctionType,
#       '///', type(abs) == types.BuiltinFunctionType)

# # dir的使用及获取具体属性及方法
# class myobject(object):

#     def __init__(self):
#         self.x = 9

#     def power(self):
#         return self.x * self.x

# print(dir(myobject)) #获取myobject类的所有属性及方法
# obj = myobject()
# print(hasattr(obj, 'x'), '\t', hasattr(obj, 'y'))  # 判断是否含有某属性
# setattr(obj, 'y', 20)  # 设置一个属性
# print(hasattr(obj, 'y'), '\t', getattr(obj, 'y'))  # 获取某属性
# print(hasattr(obj, 'power'),'\t',getattr(obj, 'power')) #获取对象的方法
# print(obj.power())


# # 动态绑定方法到类
# class Student(object):
#     pass

# s = Student
# s.name = 'jeck'  # 动态给实例绑定一个属性
# print(s.name)


# def set_age(self, age):  # 定义一个函数作为实例方法
#     self.age = age

# from types import MethodType
# s.set_age = MethodType(set_age, s)  # 动态给实例绑定一个方法
# s.set_age(26)  # 调用实例方法
# print(s.age)

# # 动态绑定是在程序运行的过程中动态给class加上方法
# Student.set_age = set_age  # 给class动态绑定方法
# s2 = Student()  # 实例化
# s2.set_age(30)  # 调用实例方法
# print(s2.age)

# # 动态绑定中限制所绑定实例的属性
# # 定义class的时候，定义一个特殊的__slots__变量，限制该class实例能添加的属性


# class Student(object):
#     __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

# s = Student()
# s.name = 'jaspuer'
# s.age = 26
# s.score = 100  # 此句报错，由于class定义时score没有被放入__slots__中
# # 注意：__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用


# # @property装饰器
# class Student(object):

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0~100')
#         self._score = value

# s = Student()
# s.score = 60  # 实际转化为s.set_score(60)
# print(s.score)  # 实际转化为s.get_score()

# # 定义只读属性
# class Student(object):

#     @property
#     def birth(self):
#         return self._birth

#     # birth是可读写属性
#     @birth.setter
#     def birth(self, value):
#         self._birth = value

#     # age就是一个只读属性
#     @property
#     def age(self):
#         return 2015 - self._birth

# # 枚举类型
# from enum import Enum, unique


# @unique  # 装饰器可以帮助我们检查保证没有重复值
# class Gender(Enum):
#     Male = 0
#     Female = 1


# class Student(object):

#     def __init__(self, name, gender):
#         self.name = name
#         if isinstance(gender, Gender):
#             self.gender = gender
#         else:
#             raise ValueError("只允许接收Gender类型的参数")

# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print("pass!")
# else:
#     print("fail")


from functools import reduce


def str2num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)   


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
