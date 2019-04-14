
"""
#AUTHOR = Dean Hope Robertson
Std Number: RBRDEA003
Titele: Analysis

"""
#import packages
import csv

#prompt use for file name
filename=input('Enter the name of the CSV file:\n')

#read in the csv file
file = open(filename,'r')
data = csv.reader(file, delimiter=',')
dictionary =  csv.DictReader(file, delimiter=',') #read in a dictionary to index from

#get columns names in a list
cols = dictionary.fieldnames
cols = [x.strip() for x in cols]

#retrieve indexes of the nessecary columns
fsc_index = cols.index("fsc")
this_week_index = cols.index("this_week")
last_year_index = cols.index("last_year")
names_index = cols.index("dam")

#declare empty lists to be populated
fsc = []
this_week = []
last_year = []
names = []

#define function for list multuplication
def multiply_list(a,b):
    output=[]
    for x,y in zip(a,b):
        output.append(x*y)
    return(output)

#run through data file extract the nessecary data points for specfic columns
for file in data:
    fsc.append(float(file[fsc_index]))
    this_week.append(float(file[this_week_index]))
    last_year.append(float(file[last_year_index]))
    names.append(file[names_index])
    
#------------Calculations--------
total = round(sum(fsc),1) #total FSC
per = [x/100 for x in this_week] #this week as decimals 
this_week = multiply_list(per,fsc) # list multiplication
per = [x/100 for x in last_year]#last year as decimals
last_year = multiply_list(per,fsc) # list multiplication
percentage= round((sum(this_week)/total)*100,1)

#create a dictionaries to print from
dd = {}
dd['THIS WEEK'] = [round(x,1) for x in this_week]
dd['LAST YEAR'] = [round(x,1) for x in last_year]
dd['FSC'] = fsc
dd['DAM NAME'] = names
cols = ['THIS WEEK','LAST YEAR','FSC','DAM NAME']

##---------------OUTPUT----------
#print columns
print("{:>10}{:>10}{:>10}{:>9}".format(cols[0],cols[1], cols[2], cols[3]))

#print data columns
for i in range(len(dd['THIS WEEK'])):
    print("{:>10}{:>10}{:>10}{:<10}".format(dd['THIS WEEK'][i],dd['LAST YEAR'][i],dd['FSC'][i]," "+dd['DAM NAME'][i]))
print("\nTotal FSC is %s million cubic metres." %total)
print("Currently at {}%.".format(percentage))