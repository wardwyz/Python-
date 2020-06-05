def wordcount(file='E:\sample.txt'):
    chars = '''~！@#￥%……&*（）_+{}[]|\\/"'=;:.-<>,_'''
    charset = set(chars)

    with open(file,encoding='utf-8') as f:
        word_count = {}
        for line in f:
            words = line.split()

            for k,v in zip(words,(1,)*len(words)): #(1,)元组配二元组
                k = k.strip(chars)
                if len(k) < 1:
                    continue
                k = k.lower()
                start = 0
                for i,c in enumerate(k):
                    if c in charset:
                        if start == i:
                            start = i + 1
                            continue
                        key = k[start:i]
                        word_count[key] = word_count.get(key,0)+1 #若k不存在返回缺省值0，k存在返回对应的Value
                        start = i + 1
                else:
                    key = k[start:]
                    word_count[key] = word_count.get(key,0) + 1
                print()
    lst = sorted(word_count.items(),key=lambda x: x[1],reverse=True)
    for i in range(10):
        if i < len(lst):
            print(str(lst[i]).strip("'()").replace("'",""))

    return lst

wc = wordcount()
print(wc)
print(len(wc))