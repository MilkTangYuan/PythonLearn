"""
0.就是调用这个又调用那个
1.横向关系用组合，纵向关系用继承
2.类对象在定义类后即产生了
3.方法会被属性替换掉
4.num count 是类属性，x,y是实例属性
5.方法是要绑定实例对象的，printBB 没有绑定
"""



class Cntnum():
    num = 0
    def __init__(self):
        Cntnum.num += 1
    def __del__(self):
        Cntnum.num -= 1

    def getNum(self):
        return Cntnum.num


# a = Cntnum()
# b = Cntnum()
# c = Cntnum()
# print(Cntnum.num)

# del a

# print(Cntnum.num)


# class MyStack(list):
#     def __init__(self,x):
#         super().__init__(x)
    
#     def isEmpty(self):
#         if len(self) == 0:
#             return True
#         else:
#             return False
    
#     def push(self,x):
#         self.append(x)

#     def top(self):
#         return self[-1]

#     def bottom(self):
#         return self[0]



# statick1 = MyStack((1,2,3,4))

# print(statick1)

# print(statick1.isEmpty())
# statick1.push(7)
# print(statick1)
# print(statick1.top())
# print(statick1.bottom())
# print(statick1.pop())
# print(statick1)
    

class MyStack():
    def __init__(self,start=[]):
        self.stack = []
        for i in start:
            self.stack.append(i)
    
