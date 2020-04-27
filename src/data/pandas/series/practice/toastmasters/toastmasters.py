import pandas as pd
import matplotlib.pyplot as plt

from src.utils.utils import utils

df_income = pd.read_csv(utils.getDataDir("/pandas/头马助手收入明细2020-03-25至2020-04-24.csv"))
print(df_income)

# key中可能包含空格，可以通过keys()方法输出查看
print("近31天总收入")
print(format(df_income["总收入(元)"].sum(), ".2f"))

print("近31天平均每天收入")
all = format(df_income["总收入(元)"].mean(), ".2f")
print(all)

print("近31天原生视频总收入")
# format产出的是str
原生视频 = format(df_income["原生视频"].sum(), ".2f")
print(原生视频)

print("近31天格子广告总收入")
格子广告 = format(df_income["格子广告"].sum(), ".2f")
print()

print("近31天banner总收入")
banner = format(df_income["banner"].sum(), ".2f")
print(banner)

# series = pd.Series([原生视频,格子广告,banner], index=["原生视频", "格子广告", "banner"], name="总收入")
series = pd.Series([float(原生视频),float(格子广告),float(banner)], index=["原生视频", "格子广告", "banner"], name="总收入")
series.plot.pie()
plt.show()

# https://www.yiibai.com/pandas/python_pandas_visualization.html
# 创建区域块图形 Draw a stacked area plot.
df_pic = df_income[["原生视频", "banner", "格子广告"]]
print(df_pic)
df_pic.plot.area()
plt.show()
