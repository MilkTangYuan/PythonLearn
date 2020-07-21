#0 属性是变量 方法是函数
#1 对象是类的实例化
#2 咖啡猫 英短猫
#3 属性：长 宽  方法，求周长，求面积，求对角线
#4 抽象
#5 不必知道的不用知道 拥有父类的方法和属性 不同实例可拥有不同方法
#6 方法是封装起来的函授



class Rectangle:

    def __init__(self):
        self.wight = 4.00
        self.length = 5.00

    def getRect(self):
        print(f"这个矩形的长是:{self.length},宽是:{self.wight}")

    def setRect(self):
        print("请输入矩形的长和宽...")
        self.length = float(input("长:"))
        self.wight = float(input("宽:"))

    def getArea(self):
        print(self.length * self.wight)

class Person:
    def __init__(self,name = "小甲鱼"):
        self.name = name
    def print_name(self):
        print(self.name)
# teacher = Person()
# teacher.print_name()

rect = Rectangle()
rect.getRect()
rect.getArea()

rect.setRect()
rect.getRect()
rect.getArea()