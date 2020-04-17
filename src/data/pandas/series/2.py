import pandas as pd

# https://pandas.pydata.org/docs/getting_started/index.html#getting-started

# init a DataFrame by Python list
# When using a Python dictionary of lists, the dictionary keys will be used as column headers
# and the values in each list as rows of the DataFrame
df = pd.DataFrame({
    "col0": ["val00", "val10", "val20"],
    "col1": ["val01", "val11", "val21"],
    "col2": ["val02", "val12", "val22"]
})

# Python list: list1 = ['physics', 'chemistry', 1997, 2000];
# Python dictionary: dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print(df)
#     col0   col1   col2
# 0  val00  val01  val02
# 1  val10  val11  val12
# 2  val20  val21  val22

# Each column in a DataFrame is a Series
# When selecting a single column of a pandas DataFrame,
# the result is a pandas Series. To select the column,
# use the column label in between square brackets [].
print(df["col0"])

# You can create a Series from scratch as well.
df = pd.Series(["Jack", "Mike", "Lucy"], name="Name")

print(df)
# 0    Jack
# 1    Mike
# 2    Lucy
# Name: Name, dtype: object

# A pandas Series has no column labels, as it is just a single column of a DataFrame. A Series does have row labels.

df = pd.Series([33, 44, 55], name="VALUE")
print(df)
# 0    33
# 1    44
# 2    55
# Name: VALUE, dtype: int64
print(df.max())
# 55
print(df.describe())
# count     3.0
# mean     44.0
# std      11.0
# min      33.0
# 25%      38.5
# 50%      44.0
# 75%      49.5
# max      55.0
# Name: VALUE, dtype: float64

# Many pandas operations return a DataFrame or a Series.
# The describe() method is an example of a pandas operation returning a pandas Series.

