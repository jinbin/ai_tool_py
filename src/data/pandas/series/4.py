import pandas as pd

from src.utils.utils import utils

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#min-tut-03-subset

titanic = pd.read_csv(utils.getDataDir("/pandas/titanic.csv"))

# To select a single column, use square brackets
print(titanic["Age"])
print(titanic["Age"].max())
print(titanic["Age"].min())

# Have a look at the shape of titanic["Age"]
# shape is an attribute of a pandas Series so we don't need to add round brackets
print(titanic["Age"].shape)

# We can select two columns at the same time, use a list of column names within the selection brackets []
print(titanic[["Age", "Sex"]])
print(titanic[["Age", "Sex"]].shape)

# To select rows based on a conditional expression, use a condition inside the selection brackets [].
print(titanic[titanic["Age"] > 35])

# Another conditional expression
print(titanic[titanic["Pclass"].isin([2, 3])])
# When combining multiple conditional statements, each condition must be surrounded by parentheses ().
# Moreover, you can not use or/and but need to use the or operator | and the and operator &.
print(titanic[ (titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)])

# To select rows if Age is not NA
print(titanic[titanic["Age"].notna()])
print(titanic[titanic["Age"].isna()])

# Select specific rows and columns from a DataFrame
adult_survived = titanic.loc[titanic["Age"] > 35, "Survived"]
print(adult_survived)

# DataFrame.at : Access a single value for a row/column label pair.
# DataFrame.loc : Access a group of rows and columns by label(s).
# DataFrame.iloc : Access a group of rows and columns by integer position(s).
print(titanic.loc[titanic["Age"] > 35, ["Survived", "Cabin"]])

# select rows 10 till 25 and columns 3 to 5 in titanic.
print(titanic.iloc[9:25, 2:5])

# When selecting specific rows and/or columns with loc or iloc, new values can be assigned to the selected data.
titanic.iloc[0:3, 3] = "anonymous"
print(titanic["Name"])










