#packages
from datetime import time

#functions----------
def print_list():
    print("Available commands:\nload <route number>\nnext <embark_point> <from_time>\narrival <embark_point> <embark_time> <destination>\ndepartures <embark_point> <destination> <earliest_arrival> <latest_arrival>")

def load_data(txt_file):
    rw_file = open(txt_file,'r')
    lines = rw_file.readlines()
    rw_file.close()
    places = []
    data = []
    for line in lines:
        places.append(line.lstrip().split()[0])
        data.append(line.lstrip().split("%")[1].rstrip().lstrip())
    return(places, data)

def convert_time(t1):
    hour = int(t1.split(":")[0])
    mins = int(t1.split(":")[1])
    t1=time(hour,mins)
    return(t1)

def next_time(command):
    place = command.split()[1]
    t1 = convert_time(command.split()[2])
    index = places.index(place)
    times = data[index].split(",")
    converted_times = [convert_time(time.strip()) for time in times]
    converted_times = [x for x in converted_times if x >= t1]

    if len(converted_times) ==0:
        print("Sorry, no departures found")
    else: 
        print("The next bus departing from %s is at %s" %(place,converted_times[0].strftime('%H:%M')))

def arrival(command): 
    place1 = command.split()[1]
    place2 = command.split()[3]
    t1 = convert_time(command.split()[2])
    index = places.index(place1)
    times1 = data[index].split(",")
    converted_times = [convert_time(time.strip()) for time in times1]
    converted_times1 = [x for x in converted_times if x >= t1]
    index = places.index(place2)
    times2 = data[index].split(",")
    converted_times2 = [convert_time(time.strip()) for time in times2]
    arrival_time=converted_times2[-len(converted_times1):][0]

    if len(converted_times1) ==0:
            print("Sorry, no departures found")
    else: 
        print("The next bus departing from %s arrives at %s at %s" %(place1,place2,arrival_time.strftime('%H:%M')))
        
def convert_time_list(t2):
    return(t2.strftime('%H:%M'))

def departures(command):
    place1 = command.split()[1]
    place2 = command.split()[2]
    t1 = convert_time(command.split()[3])
    t2 = convert_time(command.split()[4])
    index = places.index(place2)
    times2 = data[index].split(",")
    converted_times= [convert_time(time.strip()) for time in times2]
    converted_times2 = [x for x in converted_times if x >= t1 and x <=t2]
    try:
        loc1 = converted_times.index(converted_times2[0])
        loc2 = converted_times.index(converted_times2[-1])
        #departures
        index = places.index(place1)
        times1 = data[index].split(",")
        converted_times1 = [convert_time(time.strip()) for time in times1]

        ouput_times = converted_times1[loc1:loc2+1]
        ouput_times = [convert_time_list(x) for x in ouput_times]

        if len(ouput_times) ==0:
            print("Sorry, no departures found")
        else: 
            print("Buses arriving at %s in that period depart from %s at"%(place2,place1),', '.join(map(str, ouput_times)))
    except (IndexError):
        print("Sorry, no departures found")

status = "running"

while status is "running":
    command = input(">")
    if command =="quit":
        status="quit"
    elif command == "help":
        print_list()
        #break
    elif command.split()[0] == "load":
        places,data = load_data(command.split()[1]+".txt")
        print("Done")
    
    elif command.split()[0] == "next":
        try:
            next_time(command)
        except NameError:
            print("You must load a route first.")

    elif command.split()[0] == "arrival":
        try:
            arrival(command)
        except NameError:
            print("You must load a route first.")
    
    elif command.split()[0] == "departures":
        try:
            departures(command)
        except NameError:
            print("You must load a route first.")