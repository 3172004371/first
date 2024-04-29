# 您可以使用 type() 函数获取任何对象的数据类型：
x = 10
print(type(x))

# Python 没有 random() 函数来创建随机数，但 Python 有一个名为 random 的内置模块，可用于生成随机数：
import random

print(random.randrange(1,10))


# 您可以使用裁切语法返回一定范围的字符。
# 指定开始索引和结束索引，以冒号分隔，以返回字符串的一部分。
# 搜索将从索引 2（包括）开始，到索引 5（不包括）结束
b = "Hello, World!"
print(b[2:5])

# 使用负索引从字符串末尾开始切片：
# 负索引表示从末尾开始，-1 表示最后一个项目，-2 表示倒数第二个项目
print(b[-5:-2])

# strip() 方法删除开头和结尾的空白字符：
a = " Hello, World! "
print(a.strip())

txt = "China is a great country"
x = "ina" in txt
print(x)
x = "ain" not in txt
print(x)
# 可以使用 format() 方法组合字符串和数字
quantity = 3
itemno = 567
price = 49.95
# 使用索引号 {0} 来确保参数被放在正确的占位符中
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


# 元组（Tuple）是有序且不可更改的集合。在 Python 中，元组是用圆括号编写的。
thistuple = ("apple", "banana", "cherry")
mylist = list(thistuple)
mylist[1] = "au"
thistuple = tuple(mylist)
print(thistuple)
# 如需创建仅包含一个项目的元组，您必须在该项目后添加一个逗号，否则 Python 无法将变量识别为元组。
thistuple = ("apple",)
print(type(thistuple))


# 集合（Set）是无序和无索引的集合。在 Python 中，集合用花括号编写。
thisset = {"apple", "banana", "cherry"}
# 要将一个项添加到集合，请使用 add() 方法。
# 要向集合中添加多个项目，请使用 update() 方法。
thisset.update(["orange"])
# 删除集合中的项目，请使用 remove() 或 discard() 方法
thisset.discard("banana")
# 使用 pop() 方法删除项目，但此方法将删除最后一项。请记住，set 是无序的，因此您不会知道被删除的是什么项目。
print(thisset)
# 使用 union() 方法返回包含两个集合中所有项目的新集合
set1 = {"a", "b", "c"}
set2 = {1, 2, "a"}
set3 = set1.union(set2)
print(set3)

# 字典（Dictionary）是一个无序、可变和有索引的集合。在 Python 中，字典用花括号编写，拥有键和值。
thisdict =	{
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}
# 使用 items() 函数遍历键和值
for x, y in thisdict.items():
  print(x, y)

# 使用 dict() 构造函数创建新的字典：
thisdict = dict(brand="Porsche", model="911", year=1963)
# 请注意，关键字不是字符串字面量
# 请注意，使用了等号而不是冒号来赋值
print(thisdict)

# if 语句不能为空，但是如果您处于某种原因写了无内容的 if 语句，请使用 pass 语句来避免错误
a = 66
b = 200
if b > a:
  pass

# for x in range(2, 29, 3):
#   print(x)


# 如果您不知道将传递给您的函数多少个参数，请在函数定义的参数名称前添加 *。
# 这样，函数将接收一个参数元组，并可以相应地访问各项：
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Phoebe", "Jennifer", "Rory")

# lambda 函数是一种小的匿名函数。
# lambda 函数可接受任意数量的参数，但只能有一个表达式。
# lambda arguments : expression
x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))

print("\n")
# Python 中的几乎所有东西都是对象，拥有属性和方法。
# 类（Class）类似对象构造函数，或者是用于创建对象的“蓝图”。
# 所有类都有一个名为 __init__() 的函数，它始终在启动类时执行。
# 使用 __init__() 函数将值赋给对象属性，或者在创建对象时需要执行的其他操作：
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Bill", 63)
p1.myfunc()

# 继承允许我们定义继承另一个类的所有方法和属性的类。
# 父类是继承的类，也称为基类。子类是从另一个类继承的类，也称为派生类。
# 创建父类
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# 使用 Person 来创建对象，然后执行 printname 方法：

x = Person("Bill", "Gates")
x.printname()

# 创建子类
class Student(Person):
  pass
x = Student("Elon", "Musk")
x.printname()
class Student(Person):
  def __init__(self, fname, lname, year):
    # 添加属性等
    Person.__init__(self, fname, lname)
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

    x = Student("Elon", "Musk", 2019)


pizza = {
      'crust': 'thick',
      'toppings': ['mushrooms', 'extra cheese'],
      }
  # 概述所点的比萨。
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
      print("\f" +topping)

# 迭代器是一种对象，该对象包含值的可计数数字。
# 迭代器是可迭代的对象，这意味着您可以遍历所有值。
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
