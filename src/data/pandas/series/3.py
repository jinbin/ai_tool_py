import pandas as pd

from src.utils.utils import utils

# Read data from CSV file
# pd_csv.csv
# 1,2,3
# 2,3,4
# 7,8,9
df = pd.read_csv(utils.getDataDir("/pandas/pd_csv.csv"))
print(df)
#    1  2  3
# 0  2  3  4
# 1  7  8  9

# Read a large amount of data from CSV file
df = pd.read_csv(utils.getDataDir("/pandas/pandas.csv"))
print(df)

print(df.head(3))

# A check on how pandas interpreted each of the column data types
# When asking for the dtypes, no brackets are used! dtypes is an attribute of a DataFrame and Series.
print(df.dtypes)

# Read data from Excel
# pip3.7 install xlrd if ImportError: Missing optional dependency 'xlrd'.
df = pd.read_excel(utils.getDataDir("/pandas/simple.xlsx"), sheet_name="Sheet1")
print(df)
print(df.info())

# Read data from json file
df = pd.read_json(utils.getDataDir("/pandas/simple.json"))
print(df)

# Write data to dict
result = df.to_dict()
print(result)

# Write data to clipboard
# Amazing !
df.to_clipboard()

# Write data to CSV file
df.to_csv("./xxx.csv")
# Content of CSV file
# ,Name,Sex,City
# 0,Jin Bin,M,Hangzhou
# 1,Lucy,F,Japan

# Write data to xls file
# pip install xlwt if ModuleNotFoundError: No module named 'xlwt'
df.to_excel("./xxx.xls")
# Content of EXCEL file
# 	Name	Sex	City
# 0	Jin Bin	M	Hangzhou
# 1	Lucy	F	Japan

# Write data to xlsx file
# pip install openpyxl if No module named 'openpyxl'
# if pip process timeout then pip --default-timeout=1000 install openpyxl
df.to_excel("./xxx.xlsx", index=False)








