def Fbnq(x):
    prep = 0
    pre = 1
    for i in range(1,x):
        num = prep + pre
        prep = pre
        pre = num
    print(num)
Fbnq(35)



def DGfbnq(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return DGfbnq(x-1)+DGfbnq(x-2)
print(DGfbnq(35))
