print("======================= RESTART ================")
filename = input("请输入文件名：")
savefile = open("D:\\PythonWorkFile\\1\\" + filename,'w')
inputbuff = input("请输入内容【单独输入':w'保存退出】:\n")

while 1:
    if inputbuff != ":w":
        inputbuff = inputbuff + '\n'
        savefile.write(inputbuff)
        inputbuff = input()
    else:
        savefile.close()
        break
