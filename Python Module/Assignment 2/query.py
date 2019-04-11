
"""
#AUTHOR = Dean Hope Robertson
Std Number: RBRDEA003
Titele: Analysis

"""

#packages
import pandas as pd
from datetime import time

#------------ DEFINE FUCNTIONS---------
def print_list():
    #prints out the list of commands if needed 
    print("Available commands:\nload <route number>\nnext <embark_point> <from_time>\narrival <embark_point> <embark_time> <destination>\ndepartures <embark_point> <destination> <earliest_arrival> <latest_arrival>")
    
def departure_exist(place,file_input):
    places =[]
    for line in file_input:
        places.append(line.split(" %")[0])
    if place in places:
        return(True)
    else:
        return(False)


def load_data(txt_file):
    #fucntion reads in the file(csv format) and create a dataframe
    #The function then reformats the dataframe into a usable format.
    data = pd.read_csv(txt_file, header=None)
    new = data[0].str.split(" %", expand=True)
    data.drop(columns =[0], inplace = True) 
    data[0] = new[1]
    data["Place"] = new[0]
    data=data[["Place",0,1,2,3,4,5]]
    data = data.set_index("Place")
    return(data)

def convert_time(t1):
    #converts a string and into object of datetime.time
    hour = int(t1.split(":")[0]) #extract hours
    mins = int(t1.split(":")[1]) #extract mins
    t1=time(hour,mins)
    return(t1)

def next_time(command):
    # The function is called when the user executes the "Next" command
    # extracts place and time from string inout by user

    place = command.split()[1]
    t1 = convert_time(command.split()[2])
    #get the times for the requested embark station
    times = list(data.loc[place]) 
    converted_times = [convert_time(time.strip()) for time in times] #convert times
    #conditional list comprehension to remove the times that have already past 
    converted_times = [x for x in converted_times if x >= t1] 
    if len(converted_times) ==0:
        #if no route available, then print:
        print("Sorry, no departures found")
    else: 
        #return the next time available
        print("The next bus departing from %s is at %s" %(place,converted_times[0].strftime('%H:%M')))
        
def arrival(command): 
    # The function is called when the user executes the "Arrival" command
    # extracts both destination,embark station, and preferred time to leave 

    place1 = command.split()[1]
    place2 = command.split()[3]
    t1 = convert_time(command.split()[2])
    #get the times for the requested embark station
    times1 = list(data.loc[place1])
    converted_times1 = [convert_time(time.strip()) for time in times1]
    #conditional list comprehension to remove the times that have already past 
    converted_times1 = [x for x in converted_times1 if x >= t1]
    #get the times for the requested arrival station
    times2 = list(data.loc[place2])
    converted_times2 = [convert_time(time.strip()) for time in times2]
    #extract the arival time of the bus that arrives at the destination
    arrival_time=converted_times2[-len(converted_times1):][0]

    if len(converted_times1) ==0:
        #if no route available, then print:
        print("Sorry, no departures found")
    else: 
        #return the next the ariival time of the next bus leaving embrak station to destination
        print("The next bus departing from %s arrives at %s at %s" %(place1,place2,arrival_time.strftime('%H:%M')))
    
def convert_time_list(t2):
    #convert times to new %H:%M format for printing
    return(t2.strftime('%H:%M'))

def departures(command):
    # extracts both destination,embark station, earliest arrival and latest arrival times
    place1 = command.split()[1]
    place2 = command.split()[2]
    t1 = convert_time(command.split()[3])
    t2 = convert_time(command.split()[4])
    #get the times for the requested destination station
    times2 = list(data.loc[place2])
    converted_times= [convert_time(time.strip()) for time in times2]
    #conditional list comprehension to find the times between early-late arrival
    converted_times2 = [x for x in converted_times if x >= t1 and x <=t2]

    loc1 = converted_times.index(converted_times2[0])
    loc2 = converted_times.index(converted_times2[-1])

    #departures
    times1 = list(data.loc[place1])
    converted_times1 = [convert_time(time.strip()) for time in times1]
    ouput_times = converted_times1[loc1:loc2+1]
    #cconvert times to new format
    ouput_times = [convert_time_list(x) for x in ouput_times]

    if len(ouput_times) ==0:
            print("Sorry, no departures found")
    else: 
        #return the next the bus time of the bus from embrak station to destination in that period
        print("Buses arriving at %s in that period depart from %s at"%(place2,place1))
        print(*ouput_times,sep = ", ")


status = "running"

#prompt user for command
print("please enter command:\n")

#initialize while loop
while status is "running":
    command = input(">")

    #if "quit" command is executed
    if command =="quit":
        status="quit" #change status

    #if "help" command is executed
    elif command == "help":
        print_list()
    
    #if "load" command is executed
    elif command.split()[0] == "load":
        data = load_data(command.split()[1]+".txt")
        print("Done")
    
    #if "next" command is executed
    elif command.split()[0] == "next":
        try:
            next_time(command)
        except NameError:
            print("You must load a route first.")
    
    #if "arrival" command is executed
    elif command.split()[0] == "arrival":
        try:
            arrival(command)
        except NameError:
            print("You must load a route first.")
    
    #if "departures" command is executed
    elif command.split()[0] == "departures":
        try:
            departures(command)
        except NameError:
            print("You must load a route first.")

