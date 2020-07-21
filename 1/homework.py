"""
PassWord = "FishC.com"
PassWord = PassWord.strip()
times = 3
while times:
    string = input("请输入密码:")
    string = string.strip()
    if string == PassWord:
        print("密码正确，进入程序")
        break
    elif "*" in string:
        print('密码中不能含有"*"号！您还有',times,"次机会!")
        continue
    else:
        times -= 1
        print("密码错误！您还有",times,"次机会!")
        
"""
Ge = 0
Shi= 0
Bai = 0
for i in range(100,999,1):
    Ge = i%10
    Shi = i/10%10
    Bai = i%100
    if(Ge ** 3 + Shi ** 3 + Bai ** 3 == i):
        print(i)
