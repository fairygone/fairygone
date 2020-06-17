import chapter_df
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


class bar0(object):

    def __init__(self, hlm_df):
        self.hlm_df = hlm_df

    def bars(self):
        # 处理中文乱码
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 默认字体
        plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
        plt.bar(self.hlm_df.chaptername, self.hlm_df.wordcount)
        plt.title("章节字数")
        plt.xlabel("章节")
        plt.ylabel("字数")
        plt.show()
    def pie0(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.pie( self.hlm_df.wordcount,labels=self.hlm_df.chaptername)
        plt.title("章节")
        plt.show()

if __name__ == "__main__":

    hlm_df = chapter_df.main()
    b = bar0(hlm_df)
    b.bars()

