import pandas as pd

# How to reshape the layout of tables
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html
from src.utils.utils import utils

pd.set_option('display.max_columns',200) #设置显示列数

titanic = pd.read_csv(utils.getDataDir("/pandas/titanic.csv"))
print(titanic.sort_values(by="Age").head())
print(titanic.sort_values(by="Age", ascending=False).head())
print(titanic)

# Sort table rows

# Sort the titanic data according to the age of the passengers.
titanic_descending = titanic.sort_values(by="Age", ascending=False)
titanic_descending.to_csv("./titanic_descending.csv")

# Sort the titanic data according to the cabin class and age in descending order.
titanic_descending1 = titanic.sort_values(by=["Pclass", "Age"], ascending=False)
titanic_descending1.to_csv("./titanic_descending1.csv")


