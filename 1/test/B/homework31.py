import pickle


def WriteFile(PartCount,BoyList,GirlList):
    F_Girl_txt = open(f"girl_{PartCount}.txt","w")
    F_Girl_pkl = open(f"girl_{PartCount}.pkl","wb")
    F_Boy_txt = open(f"boy_{PartCount}.txt","w")
    F_Boy_pkl = open(f"boy_{PartCount}.pkl","wb")

    F_Girl_txt.writelines(GirlList)
    F_Boy_txt.writelines(BoyList)
    pickle.dump(GirlList,F_Girl_pkl)
    pickle.dump(BoyList,F_Boy_pkl)

    F_Girl_txt.close()
    F_Girl_pkl.close()
    F_Boy_txt.close()
    F_Boy_pkl.close()
    

def homework31(FilePath):
    F_read = open(FilePath)
    PartCount = 0
    BoyList = list()
    GirlList = list()
    for each_line in F_read:
        if each_line[:5] == "=====":
            PartCount += 1
            WriteFile(PartCount,BoyList,GirlList)
            BoyList.clear()
            GirlList.clear()
        else:
            Buff = each_line.split(":",1)
            if Buff[0] == "小客服":
                GirlList.append(Buff[1])
            elif Buff[0] == "小甲鱼":
                BoyList.append(Buff[1])
    PartCount += 1            
    WriteFile(PartCount,BoyList,GirlList)
    F_read.close() 
homework31("record.txt")
