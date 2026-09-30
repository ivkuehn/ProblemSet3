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
data_list.append(user_item)
full_path = []

for file in data_list:
    windows_path = data_folder + "/" + file
    print(windows_path)
    full_path.append(windows_path)
    
# %%
