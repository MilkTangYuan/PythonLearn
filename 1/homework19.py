def HLWassert(str1):
    num = len(str1)
    for i in range(num):
        if str1[i] != str1[ -1 -i]:
            print("不是回联文！")
            return
    print("是回联文！")

#str0 = input("请输入一句话：")
#HLWassert(str0)




def ParamCountStr(str2):
    phaNum = 0
    numNum = 0
    NoneNum = 0
    elseNum = 0
    for i in str2:
        if i.isalpha():
            phaNum += 1
        elif i.isdigit():
            numNum += 1
        elif i.isspace():
            NoneNum += 1
        else:
            elseNum += 1
    return phaNum,numNum,NoneNum,elseNum
    
            
        



def ParamCount(*p):
    for str_buff in p:
        print("第%d个字符串共有:" %(p.index(str_buff)+1),end = '')
        result = ParamCountStr(str_buff)
        print("英文字母%d个,"%result[0],end = '')
        print("数字%d个,"%result[1],end = '')
        print("空格%d个,"%result[2],end = '')
        print("其他字符%d个。"%result[3])




ParamCount("今天是2020年04月17日","我正在www.fishC.com学习python","I love FishC.com")


        
