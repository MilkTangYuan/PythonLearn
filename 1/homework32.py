
def int_input():
    num = 0
    str = input("请输入一个整数:")
    try:
        num = int(str)
        return num
    except ValueError:
        print("出错，您输入的不是整数")
        return int_input()

#print(int_input())

def int_input2(prompt=''):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("出错，您输入的不是整数!")

#print(int_input2('请输入一个整数:'))
    
try:
    f = open('My_File.txt') # 当前文件夹中并不存在"My_File.txt"这个文件T_T
    print(f.read())
except OSError as reason:
    print('出错啦：' + str(reason))
finally:
    if 'f' in locals():
        f.close()
