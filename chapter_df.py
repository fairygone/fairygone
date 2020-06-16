import pandas as pd
import numpy as np

# 读取停用词
def getstop_words():
    try:
        with open(r"txt/hlm_ANSI", "r", encoding="ANSI") as f:
            lines = f.readlines()
            f.close()
        # for line in lines:
           # print(line)
    except Exception as e:
        e.__format__
        with open(r"txt/hlm_UTF-8.txt", "r", encoding="UTF-8") as f:
            lines = f.readlines()
            f.close()
        # for line in lines:
           # print(line)
    finally:
        # listlines = list(lines)
        return lines
# 读取停用词，readcsv


def get_chapter_df():
    stopwords = pd.read_csv(r"txt/stop_words.txt", header=None,
                            encoding="ANSI", names=["Stopwords"])
    name_dict = pd.read_csv(r"txt/name_table_UTF-8.txt",
                            header=None, names=["Character table"])

    print(stopwords)
    print('#'*20)
    print(name_dict)
    hlm = pd.read_csv(r"txt/hlm_ANSI.txt", encoding="ANSI",
                      header=None, names=["the_story_of_a_stone"])
    print(hlm)
    # 查看数据是否有空行，有则删除。
    hlm_isnull = np.sum(pd.isnull(hlm))
    hlm_isnull
    # 没有空行，说明没有缺失值，继续分析。
    # 删除多余的行,regex
    # 删除不需要的段，并重新设置索引
    hlm.to_csv(r"output/csv/hlm.csv", encoding="ANSI")
    # 找出每一章节的头部索引和尾部
    # 每一章节的标题
    index_chapterall = hlm.the_story_of_a_stone.str.contains("^正文")
    chapterall = hlm.the_story_of_a_stone[index_chapterall].reset_index(
        drop=True)  # 删除的话前面加~
    print("每一章节的标题")
    print(chapterall)
    chapterall.to_csv(r"output/csv/chaperall.csv", encoding="ANSI")
    # 提取标题切分
    print("按照空格切分的列表")
    # 替换'正文 '为''
    chapters = chapterall.str.replace("正文 ", "")
    # 按照空格分隔字符串,split方法转换为列表,只是值为列表
    chaptersplit = chapters.str.split(" ").reset_index(drop=True)
    print(chaptersplit)
    # 将切分后 的列表内容处理为数据框,list去除index
    chaptersplit.to_csv(r"output/csv/chaptersplit.csv", encoding="ANSI")
    chapter_df = pd.DataFrame(list(chaptersplit), columns=[
                              "Chapter", "Leftname", "Rightname"])
    print(chapter_df)
    return chapter_df, index_chapterall, hlm, stopwords


def analysis_chapter(chapter_df, index_chapterall, hlm):
    # 给数据框添加新的变量columns
    chapter_df['chaptername'] = np.arange(1, 121)
    chapter_df["chaptertitle"] = chapter_df.Leftname+","+chapter_df.Rightname
    # 每章的开始行（段）索引，在hlm里面位置
    chapter_df["start"] = index_chapterall[index_chapterall == True].index
    # 每章的结束行数,后一章节开始行数-1
    chapter_df["end"] = chapter_df["start"][1:len(
        chapter_df["start"])].reset_index(drop=True)-1
    chapter_df["end"][[len(chapter_df["end"])-1]] = hlm.index[-1]
    # 每章的段落长度
    chapter_df["context"] = chapter_df.end-chapter_df.start
    chapter_df["artical"] = "artical"
    print(chapter_df)
    chapter_df.to_csv("output/csv/analysis_chapter.csv", encoding="ANSI")
    return chapter_df


def count_chapter(analysis_chapter_df, hlm):
    # 计算每个章节的字符长度，应将所有的段落使用''连接起来，
    # 然后将空格字符 '＼u3000'替换为''，最后使用apply 方法计算每个章节的长度，作为字数。
    for i in analysis_chapter_df.index:
        id = np.arange(
            analysis_chapter_df.start[i]+1, int(analysis_chapter_df.end[i]))
        # ＃每章节的内容替换掉空格
        analysis_chapter_df["artical"][i] = ''.join(
            list(hlm.the_story_of_a_stone[id])).replace("\u3000", '')
        # 计算某章有多少个字
    analysis_chapter_df["wordcount"] = analysis_chapter_df.artical.apply(len)
    print(analysis_chapter_df)
    analysis_chapter_df.to_csv(r"output/csv/chapter_all.csv", encoding="ANSI")
    return analysis_chapter_df


def main():
    chapter_df, index_chapterall, hlm, ___= get_chapter_df()

    analysis_chapter_df = analysis_chapter(chapter_df, index_chapterall, hlm)

    hlm_df = count_chapter(analysis_chapter_df, hlm)
    return hlm_df


if __name__ == "__main__":
    main()
