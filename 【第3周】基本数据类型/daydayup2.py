#每天增加减少0.005，0.01
def dayday(dayfactor):
    dayup=pow(1+dayfactor,365)
    daydown=pow(1-dayfactor,365)
    print("天天向上{:.2f},天天向下{:.2f}".format(dayup,daydown))

dayday(0.005)
dayday(0.01)