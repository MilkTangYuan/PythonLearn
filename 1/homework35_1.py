

import easygui as g

def LoginPage():
    title = "账号中心"
    msg = "带【*】为必填项"
    fields = ["*用户名","*真实姓名","固定电话","*手机号码","QQ","*E-mail"]
    input_ok = True
    values = ["","","","","",""]
    values = g.multenterbox(msg = msg,title = title,fields = fields)
    
    while True:
        input_ok = True
        for each in fields:
            if each[:1] == "*":
                if values[fields.index(each)] == "":
                    g.msgbox("带*的为必填项，请输入!!")
                    values = g.multenterbox(msg = msg,title = title,fields = fields,values = values)
                    input_ok = False
                    break
        if input_ok == True:
            print("输入正确")
            return

LoginPage()
            
