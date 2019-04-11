
"""
#AUTHOR = Dean Hope Robertson
Std Number: RBRDEA003
Titele: Analysis

"""
#-----------DEFIFNE FUNCTIONS-----------
def process_line(line):
    parts = line.split(' ')
    name = parts[0]
    trials = int(parts[1])
    average = float(parts[2])
    return (name, trials, average)

def get_max(entries):
    max = entries[0]
    for i in range(1, len(entries)):
        if entries[i][2] <max[2]:
            max = entries[i]
            
    entries.remove(max)
    return max

def sort(entries):
    sorted_entries = []
    while len(entries)>0:
        sorted_entries.append(get_max(entries))
    return sorted_entries

def output(entries):
    print('Subject        | Average Time')
    print('************** | ************')
    for entry in entries:
        print('{:14} | {:.6}'.format(entry[0], entry[2]))


def main():

    #initilize while loop by status 
    status = "unknown"
    while not status == "okay":
        try:
            #prompt user for file name and read it using open
            file_name = input('Enter the name of the file:\n')
            file_input = open(file_name, 'r')
            status = "okay"
            #cater for file not been found and thus being opened
        except IOError as err:
            print(err)
            
    entries = []
    
    try: 
        for line in file_input:
            entries.append(process_line(line))
        file_input.close()
        entries = sort(entries)
        output(entries)
    except (ValueError) as val_err:
        print("Line Number:",(len(entries)+1),"- ValueError")
        print(val_err)
        print("Line:",line)
        
          
main()