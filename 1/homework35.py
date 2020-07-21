import easygui as g
import random

TargetNum = random.randint(0,100)


def GuessNum():
    choices = ("开始","退出")
    user_sel = g.buttonbox("欢迎来到猜数字游戏","猜数字游戏",choices = choices,default_choice = choices[1],cancel_choice = choices[1])

    if user_sel == choices[0]:
        #print("选择了开始")

        user_input = g.integerbox("你猜我心里想的是什么数字？(0-100内的整数):",lowerbound = 0,upperbound = 100)
        while True:
            
            if user_input == TargetNum:
                g.msgbox("哇!猜对了!!真棒!!")
                break
            elif user_input > TargetNum:
                user_input = g.integerbox("猜大啦,再试一次(0-100):",lowerbound = 0,upperbound = 100)
            else:
                user_input = g.integerbox("猜小啦,再试一次(0-100):",lowerbound = 0,upperbound = 100)
            

        
GuessNum()
