"""打出0-100所有奇数"""
i = 0
while i <= 100:
    if i % 2:
        print(i,end = ' ')
    i += 1
print("打印完了")



"""计算机崩溃"""
"""
while 1:
    print("I love fishc.com")
"""

"""爱因斯坦的难题"""
i = 0
while 1:
    if i%2 == 1:
        if i%3 == 2:
            if i%5 == 4:
                if i%6 == 5:
                    if i%7 == 0:
                        break
    i += 1



print("\n阶梯至少要有"+str(i)+"阶",end = '\n')
