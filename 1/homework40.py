'''
0.issubclass(class,classinfo)
1.isinstance(object,classinfo)
2. 先使用 hasattr(object,name)判断 "name"是否是object的对象，再访问
    直接使用 getattr(object,name,err),返回object指向的name 如果name 不存在则返回 err
3. 允许编程人员轻松有效地管理 属性 访问。
4. x = property(getXSize,setXSize,delXSize)

'''

import time
 
def timeslong(func):
    def call():
        start = time.clock()
        print("It's time starting ! ")
        func()
        print("It's time ending ! ")
        end = time.clock()
        return "It's used : %s ." % (end - start)
    return call

@timeslong
def f():
    y = 0
    for i in range(10):
        y = y + i + 1
        print(y)
    return y

print(f())