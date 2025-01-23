import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Run in Local environment
import requests #Jupyter version:from pyodide.http import pyfetch

#async def download(url, filename):
#    response = await pyfetch(url)
#    if response.status == 200:
#       with open(filename, "wb") as f:
#            f.write(await response.bytes())

filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod1.csv"

df = pd.read_csv(filepath)
print(df.head())


df[['Screen_Size_cm']] = np.round(df[['Screen_Size_cm']], 2)

# Display the first 5 rows of the DataFrame
print(df.head())

missing_data = df.isnull() #Turns a data frame same shape as df. Missing lines will be True and filled lines will be False
print(missing_data.head()) #Displays first 5 columns as False/True

for column in missing_data.columns.values.tolist(): #Gets a list of all column names in DataFrame
    print(column)
    print (missing_data[column].value_counts()) #Count how many cells have missing data (True) and how many are complete (False)
    print("--------------------") #Adds this mark between columns (This can be anything)

#Replacing missing data with Mean
df.replace({'Weight_kg': {np.nan: avg_weight}}, inplace=True)
