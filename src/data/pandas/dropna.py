import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,6))

df.iloc[:4, 1] = None
df.iloc[2,2] = None
print(df)

# 滤除缺失数据 dropna

print(df)
print(df.dropna())
print(df.dropna(how="all"))
# 非空置 >= 5 满足条件
print(df.dropna(thresh=5))
# 根据指定的列名当中删除有空值的行
print(df.dropna(subset=[2,4]))
# 根据指定的行名当中删除有空值的列
print(df.dropna(subset=[3,4], axis=1))