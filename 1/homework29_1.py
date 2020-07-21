def compare_file(file_name1,file_name2):
    file1 = open(file_name1)
    file2 = open(file_name2)
    site = 0
    diff_site = list()
    for each_line in file1:
        site += 1
        if each_line != file2.readline():
            diff_site.append(site)
    file1.close()
    file2.close()
    return diff_site

"""
file1_name = input("请输入需要比较的第一个文件名:")
file2_name = input("请输入需要比较的第二个文件名:")
diff_buff = compare_file(file1_name,file2_name)
diff_len = len(diff_buff)
print("两个文件共有【%d】除不同" %diff_len)
if diff_len > 0:
    for i in diff_buff:
        print("第%d行不一样" %i)
"""


def printfile(filename,line):
    file_f = open(filename)
    print("文件%s的前%d行内容如下"%(filename,line))
    line_num = 0
    for each_line in file_f:
        if line_num < line:
            print(each_line)
            line_num += 1
        else:
            print("=="*8)
            break
"""
file1_name = input("请输入要打开的文件:")
line_num = input("请输入要显示的行数")
line_num = int(line_num)
printfile(file1_name,line_num)
"""

def printfile_(filename,line):
    file_f = open(filename)
    buf = line.split(sep = ':')
    beagin = 0
    end = -1
    
    if buf[0] != '':
        beagin = int(buf[0])
    if buf[1] != '':
        end = int(buf[1])
        
    if beagin == 0:
        if end == -1:
            buf = "全文"
        else:
            buf = f"从开始到第{end}行"
    else:
        if end == -1:
            buf = f"从{beagin}行到末尾"
        else:
            buf = f"从{beagin}行到{end}行"
    print(f"文件{filename}的{buf}的内容如下：")
    for i in range(beagin-1):
        file_f.readline()
    lines = end - beagin + 1
    if lines < 0:
        print(file_f.read())
    else:
        for i in range(lines):
            print(file_f.readline())
        
"""

file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
line_num = input('请输入需要显示的行数【格式如 13:21 或 :21 或 21: 或 : 】：')
printfile_(file_name,line_num)
"""

def MyReplace(filename,oldstr,newstr):
    file_f = open(filename)

    content = list()
    count = 0

    for each_line in file_f:
        if oldstr in each_line:
            count += each_line.count(oldstr)
            each_line = each_line.replace(oldstr,newstr)
        content.append(each_line)
    decide = input(f"文件[{filename}]中共有[{count}]个【{oldstr}】\n您确定要把所有的【{oldstr}】替换为【{newstr}】吗？【YSE/NO】")
    if decide in ['YSE','Yes','yes']:
        file_f_write = open("D:\\PythonWorkFile\\1\\" + filename,'w')
        file_f_write.writelines(content)
        file_f_write.close()
    file_f.close()     
file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
MyReplace(file_name, rep_word, new_word)
