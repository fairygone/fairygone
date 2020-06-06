from collections import Counter
import jieba

list1 = jieba.cut("我爱你中国家", cut_all=True)
print("/".join(list1))

list1 = jieba.cut("我爱你中国家", cut_all=False)
print("/".join(list1))
#自定义词典
jieba.load_userdict(r"F:/the story of a stone/test/user_dict.txt")
list2 = jieba.cut_for_search("小明硕士毕业于中国科学院九三三")
for i in list2:
    print(i)
list(list2)
Counter(list2).most_common(10)

c = Counter("小明硕士毕业于中国科学院九三三")
c.most_common(3)  # 词频前三

content =open(r"F:/VS Code Workspace of python/红楼梦ANSI.txt","r",encoding="ANSI").read()
c=Counter(content).most_common(10)
c
con_words = [x for x in jieba.cut_for_search(content) if len(x) >= 2]
Counter(con_words).most_common(10)
#自定义词典
jieba.load_userdict(r"F:/the story of a stone/test/user_dict.txt")
