# 文本词云图
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

s1 = """在克鲁伊夫时代，巴萨联赛中完成了四连冠，后三个冠军都是在末轮逆袭获得的。在 91/92 赛季，
        巴萨末轮前落后皇马
        1 分，结果皇马客场不敌特内里费使得已萨
        逆转。一年之后 ，巴萨用几乎相同的方式逆袭 ， 皇马还是末轮输给了特内里费。在 93/94
        赛季中， 巴萨末轮前落后拉科 1 分。 巴萨末轮 5 比 2 屠杀塞维利亚，拉科则 。 比 0 战平
        瓦伦西亚，巴萨最终在积分相同的情况下靠直接交锋时的战绩优势夺冠。神奇的是，拉
        科球员久基奇在终场前踢丢点球，这才有了 巴萨的逆袭。"""

s2 = """巴萨上一次压哨夺冠，发生在 09/10 赛季中 。末轮前 巴萨领先皇马
1 分，只
要赢球就将夺冠。末轮中巴萨 4 比 0 大胜巴拉多利德，皇马 则与对手踢平。
巴萨以 99
分的佳绩创下五大联赛积分纪录，皇马则以 96 分成为了悲情的史上最强亚军。
"""
s3 = """在 48/49 赛季中，巴萨末轮 2 比 l 拿下 同城死敌西班牙人，以 2 分优势夺冠。
52/53 赛季，巴萨末轮 3 比 0 战胜毕 巴，
以 2 分优势力压瓦伦西亚夺冠。在 59/60 赛
季，
巴萨末轮 5 比 0 大胜萨拉戈萨。皇马 巴萨积分相同，
巴萨靠直接交锋时的战绩优势
夺冠。"""
mylist = [s1, s2, s3]
word_list = [" ".join(jieba.cut(sentence)) for sentence in mylist]
lis = " ".join(word_list)

wordcloud = WordCloud(font_path="simhei.ttf",
                      background_color="green").generate(lis)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
#########################
text=open(r"txt/hlm_ANSI.txt","r",encoding="ANSI")
mylist = list(text)
jieba.load_userdict(r"txt/name_table.txt")
word_list = ["".join(jieba . cut(sentence)) for sentence in mylist]
new_text = " " . join(word_list)
wordcloud = WordCloud(font_path='simhei.ttf',
                      background_color="black") . generate(new_text)
plt.imshow(wordcloud)
plt.axis("off")
plt . show()
#使用 pandas 库中的read_csv
name=pd.read_csv(r"txt/name_table.txt",header=None,names=["name"])
#
hlm=pd.read_csv(r"txt/hlm_ANSI.txt",header=None,names=["hlm"],encoding="ANSI")
