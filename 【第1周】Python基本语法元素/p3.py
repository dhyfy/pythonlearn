'''获得用户输入的一个正整数输入，输出该数字对应的中文字符表示。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬
0到9对应的中文字符分别是：零一二三四五六七八九'''
tab='零一二三四五六七八九'
str=input('')
for c in str:
   print(tab[eval(c)-0],end="")