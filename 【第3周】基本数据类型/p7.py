'''获得输入的一个字符串s，以字符减号(-)分割s，将其中首尾两段用加号(+)组合后输出。'''
str=input()
strlist=str.split('-')
print(strlist[0]+'+'+strlist[-1])