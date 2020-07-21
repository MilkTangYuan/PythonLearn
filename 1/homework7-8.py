temp = input("请输入分数：")
num = 90
while (not temp.isdigit() or (not(0<= num <=100))):
    temp = input("输入有误，请输入0-100的数值")
    if temp.isdigit():
        num = int(temp)
        print("转换",num)
    else:
        print("tg")
        num = 90
num = int(temp)
if 80> num >= 60:
    print("C")
elif num >= 90:
    print("A")
elif num >= 80:
    print("B")
else:
    print("D")
    


temp = input("x:")
x = int(temp)
temp = input("y:")
y = int(temp)
temp = input("z:")
z = int(temp)
temp = (x if x<y else y)
small = temp if temp<z else z
print(small)

small = x if (x < y and x < z) else (y if y < z else z)
print(small)





small =  x if( x < z and x < z) else (y if(y < z)else z)
