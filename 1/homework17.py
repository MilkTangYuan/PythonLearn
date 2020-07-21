def MyPower(x,y):
    time = y
    result = 1
    while(time):
        result = x*result
        time = time -1
    print(result)
    return result


MyPower(2,0)


def gcd(x,y):
    if x > y:
        max = x
        min = y
    else:
        max = y
        min = x
    if min == 0:
        return min

    remain = max % min
    while(remain):
        max = min;
        min = remain
        remain = max % min
    return min

print(gcd(15,9))
        

def MyBin(num):
    result = ''
    while(num//2):
        result = str(num%2) + result
        num = num//2
    result = str(num) + result
    print(result)
    return result



MyBin(2)
