import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
from imageio import imread
from PIL import Image

text = open(r"F:/VS Code Workspace of python/红楼梦ANSI.txt","r",encoding="ANSI")
list_text=list(text)
word_list=[" ".join(jieba.cut(i) for i in list_text)]
new_text=' '.join(word_list)

mask=imread("")
