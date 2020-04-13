import pandas as pd
import numpy as np

# 填充空值
df = pd.DataFrame({"k1":["one", "two"] * 3 + ["two"] * 2, "k2": [1,1,2,3,3,4,4,4], "k3": [1,2,3,4] * 2})

print(df)

# 记录重复，特征重复
# 识别记录重复：duplicated
# duplicated(self, subset=None, keep="first")
# keep: first 除了第一个，其他全部标记为true
# keep: last 除了最后一个，其他全部标记为true
# keep: False 全部标记为true
print(df.duplicated())
print(df.duplicated(keep=False))

# 去除记录重复：drop_duplicates
print(df.drop_duplicates())
print(df.drop_duplicates(keep="last"))
print(df.drop_duplicates(keep=False))

print(df.duplicated(subset="k1"))
print(df.drop_duplicates(subset="k1"))

# 特征重复：利用特征间的相似度将两个相似度为1的特征去除一个
# corr计算相似度

print(df[["k2", "k3"]])
# 只针对数字计算
corr = df[["k2", "k3"]].corr(method="pearson")
print(corr)

# 处理异常值（离群点）
# 方法：
# 简单统计分析法
# 3西格玛原则
# 箱线图分析











