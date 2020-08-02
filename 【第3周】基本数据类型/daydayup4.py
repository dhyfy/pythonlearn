#每周5天每天增加，周六周日休息每天减少
def dayday1(dayfactor):
    dayup=1
    for i in range(365):
        if i%7 in [0,6]:
            dayup*=1-0.01
        else:
            dayup*=1+dayfactor
    return dayup
def dayday2(dayfactor):
    dayup=pow(1+dayfactor,365)
    return dayup

dayupeveryday=dayday2(0.01)
dayfactor=0.01
while dayday1(dayfactor)<dayupeveryday:
    dayfactor+=0.001
print("工作日的努力参数:{:.3f}".format(dayfactor))