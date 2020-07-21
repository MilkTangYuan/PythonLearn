"""
0,可以偷懒了
1,报错，__init__应该没有返回值      #不应该返回除 NONE 以外的任何对象
2,不会删除父类的相关属性或方法，但是在子类里面，相关属性或方法会被子类的替换    #子类对象调用的时候会调用到新属性或方法
3,重写？
4,可以自动指向父类的方法  #super 函数超级之处在于你不需要明确给出任何基类的名字，它会自动帮您找出所有基类以及对应的方法
5,D 类 的初始化 会调用两次A
6,
"""
import math

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def getx(self):
        return self.x
    def gety(self):
        return self.y



class Line():
    def __init__(self,pstart,pend):
        self.pstart = pstart
        self.pend = pend
    
    def getLen(self):
        self.length =  math.sqrt((self.pstart.x - self.pend.x)*(self.pstart.x - self.pend.x) + (self.pstart.y - self.pend.y)*(self.pstart.y - self.pend.y))
        return self.length

    def set_start_point(self,p_start):
        self.pstart = p_start
    def set_end_point(self,p_end):
        self.pend = p_end
p1 = Point(0,3)
p2 = Point(4,0)
line1 = Line(p1,p2)
print(line1.getLen())
