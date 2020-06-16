import jieba
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np

class Hlmwordcount():
    # 此函数用于绘制条形图
    def showNameBar(self, name_list_sort, name_list_count):
        # x代表条形数量
        x = np.arange(len(name_list_sort))
        # 处理中文乱码
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 绘制条形图，bars相当于句柄
        bars = plt.bar(x, name_list_count)
        # 给各条形打上标签
        plt.xticks(x, name_list_sort)
        # 显示各条形具体数量
        i = 0
        for bar in bars:
            plt.text((bar.get_x() + bar.get_width() / 2), bar.get_height(),
                     '%d' % name_list_count[i], ha='center', va='bottom')
            i += 1
        # 显示图形
        plt.show()

    # 此函数用于绘制饼状图
    def showNamePie(self, name_list_sort, name_list_fracs):
        # 处理中文乱码
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 绘制饼状图
        plt.pie(name_list_fracs, labels=name_list_sort,
                autopct='%1.2f%%', shadow=True)
        # 显示图形
        plt.show()

    def getwordcloud(self, hlm_path,name_path, similar_path):
        # 将所有人名临时添加到jieba所用字典，以使jieba能识别所有人名
        # 打开name文件,获取人物表
        #file_name=open(name_path,"r",encoding="UTF-8").read()
        # 打开并读取txt文件
        #file_obj = open(txt_path, 'r', encoding="ANSI").read()
        with open(hlm_path, "r", encoding="ANSI") as f ,open(similar_path,"r",encoding="UTF-8") as sf:
            hl = f.readlines()
            jieba.load_userdict(name_path)
            character = pd.read_csv(name_path, header=-1)
            mylist = [k[0].split(" ")[0] for k in character.values.tolist()] 
            tmpNames = []
            names = {}
            relationships ={}
            #姓名替换 字符替换就很不方便： 建立词典
            #similar_dict=eval(sf.read()) 
            #新建一个分词词典，包含人物姓名的别称，这样就尽可能的避免了人物出现，而未统计的情况。
            #把人物的别称替换成人物的全名
            for h in hl:
                h.replace("贾妃", "元春")
                h.replace("李宫裁", "李纨")
               # poss = pseg.cut(h) tmpNames.append([]) for w in poss: if w.flag != 'nr' or len(w.word) != 2 or w.word not in mylist: continue tmpNames[-1].append(w.word) if names.get(w.word) is None: names[w.word] = 0 relationships[w.word] = {} names[w.word] += 1 

        # jieba分词
        jieba_cut = jieba.cut(hl)
        # Counter重新组装以方便读取
        book_counter = Counter(jieba_cut)
        # 人名列表，因为要处理凤姐所以不直接用name_list
        name_dict = {}
        # 人名出现的总次数，用于后边计算百分比
        name_total_count = 0
        for k in name_list:
            if k == '熙凤':
                # 将熙凤出现的次数合并到凤姐
                name_dict['凤姐'] += book_counter[k]
            else:
                name_dict[k] = book_counter[k]
            name_total_count += book_counter[k]
        # Counter重新组装以使用most_common排序
        name_counter = Counter(name_dict)
        # 按出现次数排序后的人名列表
        name_list_sort = []
        # 按出现次数排序后的人名百分比列表
        name_list_fracs = []
        # 按出现次数排序后的人名次数列表
        name_list_count = []
        for k, v in name_counter.most_common():
            name_list_sort.append(k)
            name_list_fracs.append(round(v/name_total_count, 2)*100)
            name_list_count.append(v)
            # print(k+':'+str(v))
        # 绘制条形图
        self.showNameBar(name_list_sort, name_list_count)
        # 绘制饼状图
        self.showNamePie(name_list_sort, name_list_fracs)


if __name__ == '__main__':

    # 红楼梦txt文件所在路径，修改成自己文件所在路径
    hlm_path = r'txt/hlm_ANSI.txt'
    name_path = r"txt/nametable.txt"
    similar_path= r"txt/similar_name.txt"

    hlm = Hlmwordcount()
    hlm.getwordcloud(hlm_path,name_path,similar_path)

