#每周5天每天增加，周六周日休息每天减少
def dayday(dayfactor):
    dayup=1
    for i in range(365):
        if i%7 in [0,6]:
            dayup*=1-dayfactor
        else:
            dayup*=1+dayfactor
    print("天天向上{:.2f}".format(dayup))

dayday(0.005)
dayday(0.01)