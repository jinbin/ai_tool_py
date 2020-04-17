import pandas as pd

from src.utils.utils import utils

print(pd.__version__)

file = utils.getDataDir("/pandas/pd_csv.csv")

print("******\n")
csv_data = pd.read_csv(file)
print(csv_data)

print("******\n")
csv_data1 = pd.read_csv(file)
print(csv_data1)

# nrows=1, 取第一行
print("******\n")
csv_data1 = pd.read_csv(file, nrows=1)
print(csv_data1)

print("******\n")
csv_data1 = pd.read_csv(file, header=None)
print(csv_data1)

print("******\n")
csv_data1 = pd.read_csv(file, header=1, names=['A', 'B'])
print(csv_data1)