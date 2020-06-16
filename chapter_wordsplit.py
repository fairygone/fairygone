import jieba
import chapter_df
import numpy as np
import pandas as pd
# 对《红楼梦》全文进行分词

def splitchapter():
    stopwords = chapter_df.get_chapter_df()[3]
    # 数据表的行数
    hlm_df = chapter_df.main()
    row, ___ = hlm_df.shape
    hlm_df['splitwords'] = 'splitwords'
    for i in np.arange(row):
    # 分词,首先将每一章 的分词结果作为一个列表，然后转化为 pandas 中的 series （序列)
        splitwords = jieba.lcut(hlm_df.artical[i], cut_all=True)
    # ＃去除长度为 1 的词
        splitwords = pd.Series(splitwords)[pd.Series(splitwords).apply(len) > 1]
    # 去除停用词
        splitwords = splitwords[~splitwords.isin(stopwords)]
    # 将每一章 的词语组成列表，放入 Pandas 的 DataFrame 中 。
        hlm_df.splitwords[i] = splitwords.values
    # print(splitwords)
    # print(splitwords.values)
    hlm_df.splitwords
    return hlm_df
