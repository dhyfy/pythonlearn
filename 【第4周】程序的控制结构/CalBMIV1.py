height,weight=eval(input('请输入身高体重，用逗号分割开来：'))
bmi=weight/height**2
print('BMI:{:.2f}'.format(bmi))
who,nat="",""
if bmi<18.5:
    who,nat='偏瘦','偏瘦'
elif 18.5<=bmi<24:
    who,nat='正常','正常'
elif 24<=bmi<25:
    who,nat='正常','偏胖'
elif 25<=bmi<28:
    who,nat='偏胖','偏胖'
elif 28<=bmi<30:
    who,nat='偏胖','肥胖'
else:
    who,nat='肥胖','肥胖'
print("国际标准：{0}，国家标准：{1}".format(who,nat))