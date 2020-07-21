import os

def GetFileNum(filename):
    typedict = dict(文件夹=0)#保存索引到的值
    FileBuff = os.listdir(filename)#获取文件夹下的所有文件名
    for number in FileBuff:
        if os.path.isdir(number):#如果是文件夹
            typedict["文件夹"] = typedict["文件夹"]+1
        else:
            buf = os.path.splitext(number)
            if buf[1] in typedict:
                typedict[buf[1]] = typedict[buf[1]] + 1
            else:
                typedict[buf[1]] = 1
    
                
    return typedict

"""
Rse = GetFileNum(os.curdir)
for i in Rse:
    print(f"该文件夹下共有类型为[{i}]的文件 {Rse[i]}个")
"""

def GetFileSize(filename):
    FileBuff = os.listdir(filename)#获取文件夹下的所有文件名
    SizeDict = dict()
    for number in FileBuff:
        SizeDict[number] = os.path.getsize(number)
    return SizeDict
'''
Rse = GetFileSize(os.curdir)
for i in Rse:
    print(f"{i}[{Rse[i]}Bytes]")
'''
def FindSubPosition(sub,Father):
    index_list = list()
    index = Father.find(sub)
    while index != -1:
        index_list.append(index+1)
        index = Father.find(sub,index+1)
    if len(index_list)>0:
        return index_list
    else:
        return -1


def FindWord(FilePath,KeyWord):
    
    F_read = open(FilePath)
    FindLine = 1
    FindList = list()
    for each_line in F_read:
        if KeyWord in each_line:
            FindList.append([FindLine,FindSubPosition(KeyWord,each_line)])
        FindLine += 1
    return FindList
def FindWordFromDir(Dir,KeyWord):
    os.chdir(Dir)#进入到文件夹中
    CurDir = os.getcwd()#获取当前工作目录

    FileBuff = os.listdir(os.curdir)#获取文件夹下的所有文件名
    for number in FileBuff:
        if os.path.isdir(number):#如果是文件夹
            FindWordFromDir(number,KeyWord)
        else:
            Find_list = FindWord(number,KeyWord)
            if len(Find_list) > 0:#文件中查找到
                print(f"在文件【{os.path.join(CurDir,number)}】中找到关键字【{KeyWord}】")
                for i in Find_list:
                    print(f"关键字出现在第{i[0]}行，第{i[1]}个位置")
    os.chdir(os.pardir)#当前目录遍历完成后返回上一个目录
        
                    



Key1 = input("请输入关键字:")
FindWordFromDir("test",Key1)





