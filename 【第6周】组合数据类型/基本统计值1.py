#请在...补充一行或多行代码
#CalStatisticsV1.py
def getNum():       #获取用户不定长度的输入
    nums=[]
    iNumStr = input()
    lsnums = iNumStr.split(',')
    for i in lsnums:
        nums.append(eval(i))
      
    return nums

def mean(numbers):  #计算平均值
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)
    
def dev(numbers, mean): #计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)

def median(numbers):    #计算中位数
    numbers.sort()
    sizes = len(numbers)
    if sizes % 2 == 0:
        med = (numbers[sizes // 2 - 1] + numbers[sizes // 2]) / 2
    else:
        med = numbers[sizes // 2]
    return med
    
n =  getNum() #主体函数
m =  mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m,dev(n,m),median(n)))