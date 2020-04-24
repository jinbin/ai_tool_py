import pandas as pd
import numpy as np

# 填充空值
df = pd.DataFrame(np.random.randn(10,6))

df.iloc[:4, 1] = None
df.iloc[2,2] = None
print(df)

print(df.fillna(0))

# 横向填充，用同一行前一个值填充
print(df.fillna(axis=1, method="ffill"))

# 纵向填充，用用一列前一个填充
print(df.fillna(axis=0, method="ffill"))

# 根据指定的值进行填充
info = {0:0, 1:1, 2:2}
print(df.fillna(value=info))


