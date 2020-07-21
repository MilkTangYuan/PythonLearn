import random
Answer = random.randint(1,100)
print("--------------我爱鱼工作室---------------")
print("--------------猜数字游戏-----------------\n")
times = 5
temp = input("请输入数字：")
guess = int(temp)
if guess == Answer:
    print("哇呜，第一次就被你猜中了，你真是我肚子里的小蛔虫")
else:
    if guess > Answer:
        print("猜大了")
    else:
        print("猜小了")
    while times > 0:
        temp = input("请重新输入数字：")
        guess = int(temp)
        if guess == Answer:
            print("恭喜你猜对了")
            break;
        else:
            if guess > Answer:
                print("猜大了")
            else:
                print("猜小了")
        times = times - 1
    if times == 0:
        print("猜了那么多次也没猜对！！！")

print("游戏结束")
