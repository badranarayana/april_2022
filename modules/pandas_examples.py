"""
Pandas library.

$ pip install pandas
"""

"""
--> Pandas is a Python library.

--> Pandas is used to analyze data.

What is Pandas?

 --> Pandas is a Python library used for working with data sets.
     It has functions for analyzing, cleaning, exploring, and manipulating data.

 --> The name "Pandas" has a reference to both "Panel Data", and "
     Python Data Analysis" and was created by Wes McKinney in 2008.


Why Use Pandas?
 --> Pandas allows us to analyze big data and make conclusions based on statistical theories.
 --> Pandas can clean messy data sets, and make them readable and relevant.
 --> Relevant data is very important in data science.

"""

# Pandas Getting Started
"""
# Installation of Pandas
$ pip install pandas
"""


# lets import pandas lib
# example #1 # create pandas data frame
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
df = pd.DataFrame(mydataset)
print(df)


# # Pandas Series
# """
# What is a Series?
# A Pandas Series is like a column in a table.
#
# It is a one-dimensional array holding data of any type.
# """
# # Example
a = [1, 7, 2, 4]
#
df = pd.Series(a)

print("series: ******")
print(df)
#
# # Create Labels
# # With the index argument, you can name your own labels.
# # Example: Create you own labels:
a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])
print("&&&&&&&&&&&&&&&&")
print(myvar)
#
# # When you have created labels, you can access an item by referring to the label.
# # example : Return the value of "y":
print(myvar["y"])
#
#
# # Key/Value Objects as Series
# # You can also use a key/value object, like a dictionary, when creating a Series.
# # Example: Create a simple Pandas Series from a dictionary:
data = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(data)
print(myvar)
# # Note: The keys of the dictionary become the labels.
#
# # DataFrames
# """
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
# """
# # Example: Create a DataFrame from two Series:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
#
#
# # Pandas DataFrames
# """
# What is a DataFrame?
# A Pandas DataFrame is a 2 dimensional data structure,
# like a 2 dimensional array, or a table with rows and columns.
# """
#
# # Example
# # Create a simple Pandas DataFrame:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#
# # load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
#
# # Locate Row:
# """
# # As you can see from the result above, the DataFrame is like a table with rows and columns.
# # Pandas use the loc attribute to return one or more specified row(s)
# """
# # Example
# # Return row 0:
# # refer to the row index:
print(df.loc[0])  # Note: This example returns a Pandas Series.
#
# # Return row 0 and 1:
# # use a list of indexes:
print("*********^^^^^************")
print(df.loc[[0, 1]])  # Note: When using [], the result is a Pandas DataFrame.
print(df.loc[0])
#
# # Named Indexes
# # --------------
# # With the index argument, you can name your own indexes.
# # Example
# # Add a list of names to give each row a name:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

print("&&&&&************************")
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df.loc[['day1']])
#
print(df.loc[['day1', 'day3']]) # dataframe
#
# # Locate Named Indexes
# # Use the named index in the loc attribute to return the specified row(s).
print(df.loc["day2"])  # series
#
#
# # Load Files Into a DataFrame
# # If your data sets are stored in a file, Pandas can load them into a DataFrame.
#
# # Example
# # Load a comma separated file (CSV file) into a DataFrame:
# df = pd.read_csv('data/data.csv')  # give file path
# print(df)
#
#
# # Pandas Read CSV
# """
# Read CSV Files
# A simple way to store big data sets is to use CSV files (comma separated files).
#
# CSV files contains plain text and is a well know format
# that can be read by everyone including Pandas.
#
# """
# # Example
print("Data reading from file and loading to df")
# # Load the CSV into a DataFrame:
df = pd.read_csv('data/data.csv')
#
print(df.to_string())
#
# # Tip: use to_string() to print the entire DataFrame.
#
# # Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows = 50
df = pd.read_csv('data/data.csv')
print(df)
#
# # Pandas - Analyzing DataFrames
# """
# Viewing the Data
# One of the most used method for getting a quick overview of the DataFrame,
# is the head() method.
# The head() method returns the headers and a specified number of rows,
#  starting from the top."""
#
# # Example
# # Get a quick overview by printing the first 10 rows of the DataFrame
df = pd.read_csv('data/data.csv')
print("HEAD output")
print(df.head(5))
#
#
# # Example
# # Print the first 5 rows of the DataFrame:
df = pd.read_csv('data/data.csv')
print(df.head())
#
# # There is also a tail() method for viewing the last rows of the DataFrame.
# # The tail() method returns the headers and a specified number of rows,
# # starting from the bottom.
# # Example
# # Print the last 5 rows of the DataFrame:
print(df.tail(10))
#
#
# # Info About the Data
# # The DataFrames object has a method called info(),
# # that gives you more information about the data set.
# # Example

print("info output ")
print(df.info())
#
#
# print("--------------------------------------------------------")
#
print("  Pandas - Cleaning Data  ")
#
# # Pandas - Cleaning Data
# """
# Data Cleaning:
# -------------
# Data cleaning means fixing bad data in your data set.
#
# Bad data could be:
#   * Empty cells
#   * Data in wrong format
#   * Wrong data
#   * Duplicates
# """
#
# # Pandas - Cleaning Empty Cells
# # -----------------------------
# # Empty Cells
# # Empty cells can potentially give you a wrong result when you analyze data.
#
# # Remove Rows
# # One way to deal with empty cells is to remove rows that contain empty cells.
# # This is usually OK, since data sets can be very big,
# # and removing a few rows will not have a big impact on the result.
#
# # Example
print(" DROP NA")
# # Return a new Data Frame with no empty cells:
df = pd.read_csv('data/dirtydata.csv')
new_df = df.dropna()
print(new_df.to_string())
#
# # Note: By default, the dropna() method returns a new DataFrame,
# # and will not change the original.
#
# # If you want to change the original DataFrame, use the inplace = True argument:
# # Example
# # Remove all rows with NULL values:
df = pd.read_csv('data/dirtydata.csv')
print("______________________")
df.dropna(inplace=True)
print(df.to_string())
#
# # Note: Now, the dropna(inplace = True) will NOT return a new DataFrame,
# # but it will remove all rows containg NULL values from the original DataFrame.
#
#
# # Replace Empty Values
# """
# Another way of dealing with empty cells is to insert a new value instead.
#
# This way you do not have to delete entire rows just because of some empty cells.
#
# The fillna() method allows us to replace empty cells with a value:
# """
#
# # Example
# # Replace NULL values with the number 130:
print("Replace output")
df = pd.read_csv('data/dirtydata.csv')
df.fillna(130, inplace=True)
print(df.to_string())
#
# # Replace Only For Specified Columns
# # The example above replaces all empty cells in the whole Data Frame.
# # To only replace empty values for one column, specify the column name for the DataFrame:
#
# # Example
# # Replace NULL values in the "Calories" columns with the number 130:
df = pd.read_csv('data/dirtydata.csv')
df["Calories"].fillna(130000, inplace=True)
print(df.to_string())
#
# # Pandas - Cleaning Data of Wrong Format
# """
# Data of Wrong Format
# Cells with data of wrong format can make it difficult,
#  or even impossible, to analyze data.
#
# To fix it, you have two options: remove the rows,
# or convert all cells in the columns into the same format.
# """
#
# # Let's try to convert all cells in the 'Date' column into dates.
# # Pandas has a to_datetime() method for this:
# # Example
# # Convert to date:
print("Date format output")
df = pd.read_csv('data/dirtydata.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())
#
# # Example
# # Remove rows with a NULL value in the "Date" column:
df.dropna(subset=['Date', 'Calories'], inplace=True)
print('DROP NA output')
print(df.to_string())
#
#
# # Removing Rows
# # Example
# # Delete rows where "Duration" is higher than 120:
for x in df.index:
  if df.loc[x, "Duration"] < 30:
         df.drop(x, inplace=True)

print(" delete ***********")
print(df.to_string())

#
# # Pandas - Removing Duplicates
# """
# Discovering Duplicates
# Duplicate rows are rows that have been registered more than one time.
#
# To discover duplicates, we can use the duplicated() method.
#
# The duplicated() method returns a Boolean values for each row:
# """
# # Example
# # Returns True for every row that is a duplicate, otherwise False:
print(df.duplicated())


#
#
# # Removing Duplicates
# # To remove duplicates, use the drop_duplicates() method.
df.drop_duplicates(inplace=True)
print(df.to_string())
#
# #  Pandas - Plotting
#
# """
# Plotting
#
# Pandas uses the plot() method to create diagrams.
#
# We can use Pyplot,
# a submodule of the Matplotlib library to visualize the diagram on the screen.
# """
# # Example
# # Import pyplot from Matplotlib and visualize our DataFrame:
#


# install matplot
# $ pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt
#
df = pd.read_csv('data/dirtydata.csv')
df.plot()
plt.show()
#
# # Histogram
df["Duration"].plot(kind='hist')
plt.show()

# """
#
# import Yahoo Finance for stock data,
# Pandas for data processing,
# Numpy for mathematical calculation
# Matplotlib for visualization


# pip install yfinance

# import yfinance as yf
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# #
# #
# # # Create a list with Nifty and Top 10 stocks.
# nifty_top = ["^NSEI",
#              "RELIANCE.NS",
#              "HDFCBANK.NS",
#              "INFY.NS",
#              "HDFC.NS",
#              "ICICIBANK.NS",
#              "TCS.NS",
#              "KOTAKBANK.NS",
#              "HINDUNILVR.NS",
#              "ITC.NS",
#              "AXISBANK.NS"]
# #
# # # Create an empty list that is used to store the stock data.
# stocks_list = []
# for stock in nifty_top:
#     print(stock)
#     df = yf.download(stock, period='10y', interval='1d')
#     # drop any “Not a number” data using dropna() funtion
#     df.dropna(inplace=True)
#     # “Adjusted Close” price
#     stocks_list.append(df['Adj Close'])
# #
# #
# data = pd.concat(stocks_list, axis=1)
# print(data)
#
# # The column name of “Adj Close” doesn't make sense to refer back.
# # Change the column name
# data.columns = nifty_top
# print(data.to_string())
# #
# # # calculate 10 years returns
# ten_year_percent = ((data.iloc[-1] - data.iloc[0])/data.iloc[0]) * 100
# print(ten_year_percent)
