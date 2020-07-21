
import easygui as g
import os



def OpenTextFile():
    msg = "请选择一个文件"
    title = "文件选择"
    filename = g.fileopenbox(msg,title)
    back_buff = None

    with open(filename) as f_read:
        msg = f"文件{os.path.basename(filename)}的内容如下:"
        title = "显示文件内容"
        read_buff = f_read.read()
        back_buff = g.textbox(msg,title,read_buff)

    if back_buff != None:
        if back_buff != read_buff:
            msg = "检测到文件内容发生改变，请选择以下操作:"
            title = "警告"
            choices = ("覆盖保存","放弃保存","另存为")
            user_choice = g.buttonbox(msg,title,choices,default_choise = choices[1])

            if user_choice == choices[0]:
                #覆盖保存
                with open(filename,"w") as f_write:
                    f_write.write(back_buff)                    
            elif user_choice == choices[2]:
                #另存为
                title = "另存为"
                file_name = f.filesavebox("",title,default="newfile.txt")
                #这里应该做取消处理

                with open(file_name,"w") as f_write:
                    f_write.write(back_buff)
                

                


    
    






OpenTextFile()
