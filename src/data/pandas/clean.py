import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,6))

df.iloc[:4, 1] = None
df.iloc[2,2] = None
print(df)

# 找出缺失数据

result = df.isnull()
# print(result)

# 列级别的判断
result = df.isnull().any()
# print(result)

# 只显示存在缺失值的行列，[]内是筛选条件，drop_duplicates()去重
result = df[df.isnull().values==True]
print(result)

result = df[df.isnull().values==True].drop_duplicates()
print(result)

# 获取为空的列索引
print(df.columns[df.isnull().any()==True])

# 填充缺失值

