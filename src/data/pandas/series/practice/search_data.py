import pandas as pd

from src.utils.utils import utils
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',200) #设置显示列数
pd.set_option('display.max_rows',10) #设置显示行数

df = pd.read_csv(utils.getDataDir("/pandas/content_search_query2020-04-08.csv"))
print(df)

# 按照预测行业进行统计
# 'DataFrame' object has no attribute 'value_counts', only 'Series' has.
print(df["预测行业"].value_counts())

# 筛选出买家数>0的数据
# print(df[df["买家数"] > 0])

# 筛选出曝光点击率 > 0.3的查询词
df["曝光点击率"] = df["曝光点击率"].str.strip('%').astype(float)/100
print(df["曝光点击率"])
print(df[df["曝光点击率"] > 0.3])

# 计算搜索词的平均uv
print(df["搜索uv"].mean())

print(df["曝光点击率"])
df[df["曝光点击率"]].plot()
plt.show()

df = df.rename(columns={"搜索uv": "search uv", "搜索pv": "search pv"})
# 根据搜索uv和pv，画出图形
ax = df.plot.scatter(x="search uv",
                y="search pv",
                color='b',
                label='搜索 uv / pv')
plt.show()

# 如何解决中文无法展示的问题： https://blog.csdn.net/sinat_40875078/article/details/104326625

plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False

df.plot.scatter(x="曝光uv",
                y="曝光pv",
                color='g',
                label="曝光 uv / pv", ax=ax)
plt.show()

# 除了蔡徐坤遥遥领先，其他搜索uv量均在0-100区间，uv跟pv的比例也基本成正比







