import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def getFile():
    f = open(r'txt/hlm_UTF-8.txt','r',encoding = 'utf-8')
    txt = f.read()
    f.close()
    jieba.load_userdict('txt\\name_table_UTF-8.txt')
    all_words = jieba.lcut_for_search(txt)
    words = []
    for i in all_words:
        if i in keyWord():
            words.append(i)
    return words

def keyWord():
    f = open('txt\\name_table_UTF-8.txt','r',encoding = 'utf-8')
    txt = f.read()
    f.close()
    name = txt.split()
    return name

def changeWord(words):
    with open(r'txt/similar_name_UTF-8.txt','r',encoding = 'utf-8') as f:
        txt = f.read()
    word_dict = eval(txt)
    keys = []
    values = []
    for k,v in word_dict.items():
        keys.append(k)
        values.append(v)
    for i in words:
        if i in keys:
            words.append(values[keys.index(i)])
    last_word = []
    for ch in words:
        if ch not in keys:
            last_word.append(ch)
    new_words = ' '.join(last_word)
    return last_word,new_words

def wordCount(last_word):
    counts = {}
    for word in last_word:
        counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key = lambda x:x[1],reverse = True)
    for i in range(10):
        word,count = items[i]
        print("{0:<10}{1:>5}".format(word,count))

def wordCloud(new_words):
    fontpath = 'STHUPO.TTF'
    wc = WordCloud(font_path = fontpath,
                   width=800,
                   height=600,
                   max_words=50,
                   max_font_size=150,
                   background_color = 'white', #背景板颜色
                   collocations = False,#去除重复单词 
                   prefer_horizontal=0.5
                   ).generate(new_words) 
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    wc.to_file('output/png/红楼梦人物词云图.png')  
def main():
    words = getFile()
    last_word,new_words = changeWord(words)
    wordCount(last_word)
    wordCloud(new_words)
if __name__ =="__main__":
    main()