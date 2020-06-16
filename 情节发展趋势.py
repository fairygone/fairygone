import chapter_df
from matplotlib.pylab import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties 
font=FontProperties(fname=r"C:\Windows\Fonts\FZSTK.TTF",size=14)

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# ＃字长和段落数的散点图一

plt.figure(figsize=(12, 10))
plt.subplot(2, 1, 1)
hlm_df = chapter_df.main()
plt.plot(hlm_df.chaptername, hlm_df.context)

plt.ylabel("章节段数", Fontproperties=font)
plt.title("<<the story of a stone>>", Fontproperties=font)
# 添加平均值
plt.hlines(np.mean(hlm_df.context), -5, 125, "b")
plt.xlim((-5, 125))
plt.subplot(2, 1, 2)
plt.plot(hlm_df.chaptername, hlm_df.wordcount)
plt.xlabel("章节", Fontproperties=font)
plt.ylabel("章节字数", Fontproperties=font)
# 添加平均值
plt.hlines(np.mean(hlm_df.wordcount), -5, 125, "b")
plt.xlim((-5, 125))
plt.show()
