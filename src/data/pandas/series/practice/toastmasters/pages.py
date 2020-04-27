import pandas as pd
import matplotlib.pyplot as plt

from src.utils.utils import utils

# header指定用哪一行作列名, index_col指定用作索引的列
# https://blog.csdn.net/weixin_38546295/article/details/83537558
df_pages = pd.read_excel(utils.getDataDir("/pandas/头马助手使用分析_页面分析.xlsx"), header=2, index_col=0)
print(df_pages.dtypes)
print(df_pages)

# 百分比转化为float类型用于排序
df_pages_quit = df_pages["退出率"].str.strip('%').astype(float)/100
print(df_pages_quit.sort_values(ascending=False))


