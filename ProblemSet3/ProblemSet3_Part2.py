#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
with open(file='V:/ProblemSet3/ProblemSet3/data/raw/transshipment_vessels_20180723.csv',mode='r') as file_obj:

    #Read the entire contents into a list object
    line_list = file_obj.readlines()

#Save the contents of the first line in the list of lines to the variable "headerLineString"
header_line = line_list[0]

#Print the contents of the headerLine
print(header_line)

#%% Task 4.2

#Split the headerLineString into a list of header items
header_items = header_line.split(',')

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = header_items.index("mmsi")
name_idx = header_items.index("shipname")
fleet_idx = header_items.index("fleet_name")

#Print the values
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3

#Create an empty dictionary
vessel_dict = {}

#Iterate through all lines (except the header) in the data file:
for line in line_list[1:]:
    #Split the data into values
    line_data = line.split(',')
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = line_data[mmsi_idx]
    #Extract the fleet value
    fleet = line_data[fleet_idx]
    #Adds info to the vesselDict dictionary
    vessel_dict[mmsi] = fleet

# %% Task 4.4

# Assign vesselID to string value
vesselID = '312887000'

# Use dictionary made in 4.3 to extract fleet value at the vesselID mmsi value
fleetID = vessel_dict[vesselID]

# Print the required statement
print(f'Vessel # {vesselID} flies the flag of {fleetID}')




# %% Task 5

# Construct a list of all lines from the contents of the loitering_events_20180723.csv file
with open(file='V:/ProblemSet3/ProblemSet3/data/raw/loitering_events_20180723.csv',mode='r') as task5_file_obj:

    # Read the entire contents into a list object
    loitering_list = task5_file_obj.readlines()

# Loop through each data line (i.e. skip the header line) in this line list, and at each iteration:
for event in loitering_list[1:]:

    # Split the line string into a list of data items
    event_data = event.split(',')

    # Store the transshipment_mmsi, starting & ending latitude, and starting & ending longitude values into their own respective variables
    t_mmsi = event_data[0]
    start_lat = float(event_data[1])
    start_long = float(event_data[2])
    end_lat = float(event_data[3])
    end_long = float(event_data[4])

    # Examines the starting and ending latitude to determine if event crosses the equator
    # Passing south to north means looking for change from negative to positive.
    lat_condition = start_lat < 0 and end_lat > 0

    # Examines the ending longitude to see whether it falls between 120 and 135 degrees.
    end_long_condition = 120 < end_long < 135

    # If both conditions are met, print the mmsi and fleet value from vessel_dict
    if lat_condition and end_long_condition:
        fleet_value = vessel_dict[t_mmsi]
        print(f'Vessel # {t_mmsi} flies the flag of {fleet_value}')
    # If conditions are not met, print "No vessels met criteria."
    #else:
        #print('No vessels met criteria.')

    start_long_condition = 145 < start_long < 155

    if lat_condition and start_long_condition:
        fleet_value = vessel_dict[t_mmsi]
        print(f'Vessel # {t_mmsi} flies the flag of {fleet_value}')
    #else:
        #print('No vessels met criteria.')

# Else statements were commented out to clean up output and clearly view vessels that met both conditions
