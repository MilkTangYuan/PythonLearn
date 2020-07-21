import pickle

SaveFilename = "phone.pkl"
try:
    with open(SaveFilename,"rb") as f_r:
        try:
            contacts = pickle.load(f_r)
            print(f"init dict by file:{SaveFilename}")
        except EOFError:
            contacts = dict()
            print("file is empty .init dict.")
except FileNotFoundError as reason:
    print(f"{str(reason)}")
    contacts = dict()
    print("init dict.")
    
finally:
    try:
        print('|--- 欢迎进入通讯录程序 ---|')
        print('|--- 1：查询联系人资料  ---|')
        print('|--- 2：插入新的联系人  ---|')
        print('|--- 3：删除已有联系人  ---|')
        print('|--- 4：退出通讯录程序  ---|')
        while True:
            try:
                instr = int(input('\n请输入相关的指令代码：'))
            except ValueError as reason:
                print(f"错误：{str(reason)}")
            else:
                if instr == 1:
                    name = input('请输入联系人姓名：')
                    try:
                        print(name + ' : ' + contacts[name])
                    except KeyError:
                        print('您输入的姓名不再通讯录中！')

                if instr == 2:
                    name = input('请输入联系人姓名：')
                    try:
                        print(f'您输入的姓名在通讯录中已存在 -->> {name}:{contacts[name]}')
                        if input('是否修改用户资料（YES/NO）：') in ('YES','yes','Yes'):
                            contacts[name] = input('请输入用户联系电话：')
                    except KeyError:
                        contacts[name] = input('请输入用户联系电话：')
                if instr == 3:
                    name = input('请输入联系人姓名：')
                    try:
                        del(contacts[name])         # 也可以使用dict.pop()
                    except KeyError:
                        print('您输入的联系人不存在。')
                    else:
                        print("删除成功")
                if instr == 4:
                    break
    except KeyboardInterrupt:
        print("用户结束程序")
            
    finally:
        with open(SaveFilename,"wb") as f_w:
            pickle.dump(contacts,f_w)
        print('|--- 感谢使用通讯录程序 ---|')
