'''附件是《沉默的羔羊》中文版内容，请读入内容，分词后输出长度大于2且最多的单词。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬

如果存在多个单词出现频率一致，请输出按照Unicode排序后最大的单词。'''
import jieba
def getText():
    txt=open('沉默的羔羊.txt', 'r',encoding='utf-8').read()
    # txt=txt.lower()
    # for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
    #     txt=txt.replace(ch,' ')
    return txt

threekingdomsTxt=getText()
words=jieba.lcut(threekingdomsTxt)
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
print(items[0][0])
