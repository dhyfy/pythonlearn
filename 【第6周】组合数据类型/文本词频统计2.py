import jieba
def getText():
    txt=open('threekingdoms.txt', 'r',encoding='utf-8').read()
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
for i in range(15):
    word,counts=items[i]
    print('{0:<10}:{1:>5}'.format(word,counts))

