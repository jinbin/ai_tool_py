import pandas as pd

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html
from src.utils.utils import utils

air_quality = pd.read_csv(utils.getDataDir("/pandas/air_quality_no2.csv"), index_col=0, parse_dates=True)
# print(air_quality)

# To create a new column, use the [] brackets with the new column name at the left side of the assignment.
# The calculation of the values is done element_wise.
# This means all values in the given column are multiplied by the value 1.882 at once.
# You do not need to use a loop to iterate each of the rows!
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
# print(air_quality)

# columns cannot be omitted
air_quality_rename = air_quality.rename(columns={"station_antwerp": "antwerp"})
# print(air_quality_rename)

# The mapping should not be restricted to fixed names only, but can be a mapping function as well.
# For example, converting the column names to capitalized letters can be done using a function as well:
air_quality_rename = air_quality.rename(columns=str.capitalize)
print(air_quality)
print(air_quality_rename)

# REMEMBER
# Create a new column by assigning the output to the DataFrame with a new column name in between the [].
# Operations are element-wise, no need to loop over rows.
# Use rename with a dictionary or function to rename row labels or column names.









