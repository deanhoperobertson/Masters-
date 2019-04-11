
"""
#AUTHOR = Dean Hope Robertson
Std Number: RBRDEA003
Titele: Analysis

"""
#import packages
import pandas as pd


#prompt user for file name
filename=input('Enter the name of the CSV file:\n')

#read csv file in
data = pd.read_csv(filename)

#rename columns
data=data.rename(columns={"dam":"DAM NAME",
                     " last_year": "LAST YEAR",
                     " fsc":"FSC",
                     " this_week":"THIS WEEK"})

#subsect the data to only relevant columns 
data=data[["THIS WEEK", "LAST YEAR", "FSC","DAM NAME"]]

#converting % to actual storage volumes
data["THIS WEEK"] = round((data["THIS WEEK"]/100)*data["FSC"],1)
data["LAST YEAR"] = round((data["LAST YEAR"]/100)*data["FSC"],1)

#summation of FSC figures
total = round(data["FSC"].sum(),1)
percentage = round((data["THIS WEEK"].sum()/total)*100,1) #convert to percentages

## PRINT OUTPUT
print(data)
print("Total FSC is %s million cubic metres." %total)
print("Currently at {}%.".format(percentage))