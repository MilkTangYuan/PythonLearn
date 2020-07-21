'''判定一个年份是否为闰年'''
print("--------判定闰年--------")
temp = input("请输入一个年份：")
while not temp.isdigit():
    print("输入错误！请直接输入年份值！(eg.2020)")
    temp = input("请重新输入：")
year = int(temp)
if ((not year%4) and (year % 100) or (not year % 400)):
    print(str(year) + "年是闰年")
else:
    print(temp + "年是平年")
    
