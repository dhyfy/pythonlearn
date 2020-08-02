def getNum():
    nums = []
    iNumStr = input('请输入数字(回车退出)：')
    while (iNumStr != ''):
        nums.append(eval(iNumStr))
        iNumStr = input('请输入数字(回车退出)：')
    return nums


def mean(ls):
    sum = 0
    for i in ls:
        sum += i
    return sum / len(ls)


def dev(ls, mean):
    sum = 0
    for i in ls:
        sum += (i - mean)**2
    return pow(sum / len(ls), 0.5)


def median(ls):
    ls.sorted()
    sizes = len(ls)
    if sizes % 2 == 0:
        med = (ls[sizes // 2 - 1] + ls[sizes // 2]) / 2
    else:
        med = ls[sizes // 2]
    return med


ls = getNum()
average = mean(ls)
print("平均值:{}-方差:{:.2}-中位值:{}".format(average, dev(ls, average), median(ls)))
