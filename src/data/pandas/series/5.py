import pandas as pd
import matplotlib.pyplot as plt

from src.utils.utils import utils

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html

# Column(s) to use as the row labels of the DataFrame, either given as string name or column index.
# Note: index_col=False can be used to force pandas to not use the first column as the index
# index_col=0 define the first (0th) column as index of the resulting DataFrame
# parse_dates convert the dates in the column to Timestamp objects, respectively

# air_quality = pd.read_csv(utils.getDataDir("/pandas/air_quality_no2.csv"), parse_dates=True)
air_quality = pd.read_csv(utils.getDataDir("/pandas/air_quality_no2.csv"),  index_col=0, parse_dates=True)
# print(air_quality)
print(air_quality)
print(air_quality.dtypes)

# a quick visual check of the data.
air_quality.plot()
plt.show()

# plot only the columns of the data table with the data from Paris.
air_quality["station_paris"].plot()
plt.show()

# Visually compare the 𝑁02 values measured in London versus Paris.
# Scatter create a scatter plot（散点图）with varying marker point size and color.
air_quality.plot.scatter(x="station_london",
                         y="station_paris",
                         alpha=0.5)
plt.show()



