import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from imageio import imread
from PIL import Image

text = open(r"txt/hlm_ANSI.txt", "r", encoding="ANSI")
list_text = list(text)
word_list = ["".join(jieba.cut(sentence)) for sentence in list_text]
new_text = ' '.join(word_list)
ima_mask = imread(r"image/run_man.jpg")
wc = WordCloud(font_path='simhei.ttf',
               max_words=2000, mask=ima_mask,background_color='#ffaaffff',mode="RGBA").generate(new_text)
plt.imshow(wc)
plt.axis('off')
plt.show()
# 保存到文件
wc.to_file(r"output/image_wc.png")
#根据词频生成词云
import jieba
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from imageio import imread
from collections import Counter
import matplotlib.pyplot as plt

text = open(r"txt/hlm_ANSI.txt", "r", encoding="ANSI")
mylist = list(text)
word_list = ["".join(jieba.cut(sentence)) for sentence in mylist]
new_text = ''.join(word_list)
ima_mask = imread(r"image/run_man.jpg")
words= [x for x in jieba.cut(new_text)]

frequency =Counter(words).most_common()
freq =dict(frequency)
wc =WordCloud(font_path="simhei.ttf",background_color="white",max_words=2000,mask=ima_mask).fit_words(freq)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file(r"output/image_wc_freq.png")

