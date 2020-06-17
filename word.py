import jieba
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from imageio import imread
from collections import Counter
import matplotlib.pyplot as plt
import chapter_splitwords

hlm_df=chapter_splitwords.splitchapter()
ima_mask = imread(r"image/ninja.jpg")
for c in range(3):
    words=hlm_df.splitwords[c]
    frequency =Counter(words).most_common(30)
    freq =dict(frequency)
    wc =WordCloud(font_path="simhei.ttf",background_color="white",max_words=2000,mask=ima_mask).fit_words(freq)
    plt.imshow(wc)
    plt.axis('off')
    plt.title(c+1)
    plt.show()
    wc.to_file(r"output/image_wc_freq.png")

    name_list_sort = []
    name_list_count = []
    for k, v in frequency:
        name_list_sort.append(k)
        name_list_count.append(v)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.pie( name_list_count,labels=name_list_sort,autopct='%.2f')
    plt.title("词频")
    plt.show()
