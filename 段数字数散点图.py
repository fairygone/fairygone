from pylab import *
import chapter_df
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# ＃字长和段落数的散点图一
plt.figure(figsize=(8, 6))
hlm_df = chapter_df.main()
plt.scatter(hlm_df.context, hlm_df.wordcount)
for i in hlm_df.index:
    plt.text(hlm_df.context[i]+1, hlm_df.wordcount[i],
             hlm_df.chaptername[i], size=7)
plt.xlabel("章节段数")
plt.ylabel("章节字数")
plt.title("<<the story of a stone>>")
plt.show()
#散点图二
plt.figure(figsize=(8, 6))
hlm_df = chapter_df.main()
plt.scatter(hlm_df.context, hlm_df.wordcount)
for ii in hlm_df.index:
    plt.text(hlm_df.context[ii]-2, hlm_df.wordcount[ii]+100,
             hlm_df.Chapter[ii], size=7)
plt.xlabel("章节段数")
plt.ylabel("章节字数")
plt.title("<<the story of a stone>>")
plt.show()

#整体的趋势为段落越多，字数越多