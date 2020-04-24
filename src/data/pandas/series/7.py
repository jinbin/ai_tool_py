import pandas as pd

from src.utils.utils import utils

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

titanic = pd.read_csv(utils.getDataDir("/pandas/titanic.csv"))
print(titanic)

# Aggregating statistics

# What is the average age of the titanic passengers?
# Different statistics are available and can be applied to columns with numerical data.
# Operations in general exclude missing data and operate across rows by default.
# mean: occupying a middle position, intermediate in space, order, time, kind, or degree
mean_age = titanic["Age"].mean()
print(mean_age)

# What is the median age and ticket fare price of the titanic passengers?
# Notice use double square brackets
median_data = titanic[["Age", "Fare"]].median()
print(median_data)

agg_data = titanic.agg({"Age": ['min', 'max', 'mean', 'median'],
             "Fare": ['min', 'max', 'mean', 'median']})
print(agg_data)

# Aggregating statistics grouped by category

# What is the average age for male versus female titanic passengers?
print(titanic[["Sex", "Age"]].groupby("Sex").mean())

# split-apply-combine pattern
# Split the data into groups
# Apply a function to each group independently
# Combine the results into a data structure

# The apply and combine steps are typically done together in pandas.

# What is the mean ticket fare price for each of the sex and cabin class combinations?
print(titanic.groupby(["Sex", "Cabin"])["Fare"].mean())
# Grouping can be done by multiple columns at the same time.
# Provide the column names as a list to the groupby() method.

# Count number of records by category

# What is the number of passengers in each of the cabin classes?
print(titanic.groupby("Pclass")["Pclass"].count())
print(titanic["Pclass"].value_counts())

# REMEMBER
# Aggregation statistics can be calculated on entire columns or rows
# groupby provides the power of the split-apply-combine pattern
# value_counts is a convenient shortcut to count the number of entries in each category of a variable



