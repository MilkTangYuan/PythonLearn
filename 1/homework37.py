"""
0.多态
1.使用继承 class B(A):
2.传递实例化对象--------绑定方法
3.__name
4.__init__
5.类没有实例化 也就没有self

"""

class Ticket():
    def __init__(self,weekend = False,child=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calcPrice(self,num):
        return self.exp * self.inc * self.discount * num
# adult = Ticket()
# child = Ticket(child = True)
# print("2个成人和一个小孩的平日票价为：%.2f" %(adult.calcPrice(2) + child.calcPrice(1)))


import random

legal_x = (0,10)
legal_y = (0,10)
turtle_step = (-2,-1,1,2)
fish_step = (-1,1)
class Turtle:
    def __init__(self):
        self.power = 100
        self.x = random.randint(legal_x[0],legal_x[1])
        self.y = random.randint(legal_y[0],legal_y[1])
    def move(self):
        direction = random.choice([0,1])
        if direction == 0:
            self.x = self.x + random.choice(turtle_step)
            if self.x < legal_x[0]:
                self.x = legal_x[0] + (legal_x[0] - self.x)
            elif self.x > legal_x[1]:
                self.x = legal_x[1] - (self.x - legal_x[1])
        else:
            self.y = self.y + random.choice(turtle_step)
            if self.y < legal_y[0]:
                self.y = legal_y[0] + (legal_y[0] - self.y)
            elif self.y > legal_y[1]:
                self.y = legal_y[1] - (self.y - legal_y[1])
        self.power -= 1
        return (self.x,self.y)

    def eat(self):
        # if self.power <= 80:
        self.power += 35
        # else:
        #     self.power = 100
        print("吃了一条小鱼，当前体力值 %d" %(self.power))


class Fish:
    def __init__(self):
        self.x = random.randint(legal_x[0],legal_x[1])
        self.y = random.randint(legal_y[0],legal_y[1])

    def move(self):
        direction = random.choice([0,1])
        if direction == 0:
            self.x = self.x + random.choice(fish_step)
            if self.x < legal_x[0]:
                self.x = legal_x[0] + (legal_x[0] - self.x)
            elif self.x > legal_x[1]:
                self.x = legal_x[1] - (self.x - legal_x[1])
        else:
            self.y = self.y + random.choice(fish_step)
            if self.y < legal_y[0]:
                self.y = legal_y[0] + (legal_y[0] - self.y)
            elif self.y > legal_y[1]:
                self.y = legal_y[1] - (self.y - legal_y[1])
        return (self.x,self.y)


def TubleEatFishGame():
    turtle = Turtle()
    fish = []
    for i in range(10):
        fish.append(Fish())
    while True:
        if not len(fish):
            print("鱼被吃完了，游戏结束")
            break
        if not turtle.power:
            print("乌龟体力耗尽，饿死了")
            break


        pos = turtle.move()

        for each_fish in fish[:]:
            if each_fish.move() == pos:
                turtle.eat()
                fish.remove(each_fish)
                print("还剩 %d 条小鱼" %(len(fish)))



TubleEatFishGame()