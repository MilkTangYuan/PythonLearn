"""
0 前后都有__
1 __new__
2 需要初始化时
3 __init__方法只能返回NONE
4 创建一个示例化对象
5 当所有引用都被删除，垃圾回收机制回收时

"""



class FileObject():
    ''' 给文件对象进行包装从而确定在删除文件时文件流关闭''' 

    def __init__(self,filename = 'sample.txt'):
        #读模式打开一个文件
        self.read_file = open(filename,"r+")
    def __del__(self):
        self.read_file.close()
        del self.read_file

class C2F(float):
    ''' 将摄氏度转换为华氏度''' 
    def __new__(cls,num=0.0):
        f = 0.0
        f = num*1.8 + 32
        return float.__new__(cls,f)
print(C2F(32))
        


class Nint(int):

    def __new__(cls,string):
        if isinstance(string,int):
            return int.__new__(cls,string)
        elif isinstance(string,float):
            string = int(string)
            return int.__new__(cls,string)
        elif isinstance(string,str):
            he = 0
            for each in string:
                he = he + ord(each)
            return int.__new__(cls,he)
        

# print(Nint(123))
# print(Nint(1.5))
# print(Nint("A"))
# print(Nint("FishC"))