# Author: Isabelle Kuehn
# Assignment Due Date: 10/07/2026
# ENV 859


#%% Task 1 - Edit code to print as requested
#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation == 20322 

print (mountain + ", formerly\nknown as "+ nickname + ",")
print ("is " + str(elevation) + "' above sea level." )


#%% Task 2 - Lists and Iteration

data_folder = "W:/859_data/triangle"
data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]
user_item = "roads.shp"
# Add user_item to data_list
data_list.append(user_item)

# Create empty list
full_path = []

# Create for loop that creates list of full path names
for file in data_list:
    windows_path = data_folder + "/" + file
    print(windows_path)
    full_path.append(windows_path)
    
# %% Task 3

user_numbers = []

# Create for loop that adds user input and sorts values in ascending order
# Print only the last item in the user_numbers list
for i in range(3):
    value = int(input("Enter an integer: "))
    user_numbers.append(value)
    user_numbers.sort()
    print(user_numbers[-1])


# %% Task 3- Challenge

# Repeat task 3 but sort values in descending order
# Print all items in user_numbers list
user_numbers = []

for i in range(3):
    value = int(input("Enter an integer: "))
    user_numbers.append(value)
    user_numbers.sort(reverse=True)
    print(user_numbers)
    