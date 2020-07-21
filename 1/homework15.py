
while True:
    temp = input("请输入一个整数（输入Q结束程序）:")
    if temp.isdigit():
        num = int(temp)
    elif temp == 'Q' or temp == 'q':
        break
    else:
        print("输入有误，请重新输入：")
        continue
    print("十进制 -> 十六进制：{0:d}->{1:#x}".format(num,num))
    print("十进制 -> 八进制：{0:d}->{1:#o}".format(num,num))
    print("十进制 -> 二进制：{0:d}->{1:#b}".format(num,num))

    
