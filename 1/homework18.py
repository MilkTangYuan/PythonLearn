def Function1(*para,base = 3):
    'a) 计算打印所有参数的和乘以基数（base=3）的结果.\nb) 如果参数中最后一个参数为（base=5），则设定基数为5，基数不参与求和计算。'
    sum = 0
    for i in para:
        sum = sum + i
    print(sum*base)


Function1(1,2,3,4)
Function1(1,2,3,4,base = 5)
#print(Function1.__doc__)
help(Function1)


def Function2():
    '寻找水仙花数，并打印'
    NumBuff = list()
    for i in range(100,1000):
        ge = i%10
        shi = i//10%10
        bai = i//100
        if ge**3 + shi**3 + bai**3 == i:
            NumBuff.append(i)
    print(NumBuff)

            
Function2()


def findstr( ):
    str1 = input("请输入目标字符串:")
    str2 = input("请输入子字符串（两个字符）:")
    print("子字符串在目标字符串中共出现 %d次"%str1.count(str2))

findstr()

    
