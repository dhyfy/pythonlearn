import jieba
excludes=['却说','二人','将军','不可','不能','不敢','不知','如此','荆州','如何','引兵','次日','军士','军马','大喜','天下',\
    '左右','主公','东吴','于是','今日','商议','魏兵','陛下','都督','人马','一人','汉中','众将','只见',\
        '上马','大叫','蜀兵','太守','此人','夫人','先主','后人','背后','城中','天子','一面','何不','后主',\
            '大军','忽报','先生','百姓','何故','不如','赶来','原来','先锋','然后','令人','江东','喊声','正是','下马',\
            '徐州','忽然','因此','成都','不见','未知','大败','大事','之后','一军','接应','军中','起兵','引军','可以',\
                '大惊','进兵','大怒','以为','不得','心中','下文','一声','追赶']
threekingdomsTxt=open('threekingdoms.txt', 'r',encoding='utf-8').read()
words=jieba.lcut(threekingdomsTxt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=='孔明' or word=='孔明曰':
        rword='诸葛亮'
    elif word=='关公' or word=='云长' or word=='关云长':
        rword='关羽'
    elif word=='玄德' or word=='玄德曰' or word=='刘皇叔':
        rword='刘备'
    elif word=='孟德' or word=='丞相':
        rword='曹操'
    else:
        rword = word
    counts[rword]=counts.get(rword,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,counts=items[i]
    print('{0:<10}:{1:>5}'.format(word,counts))

