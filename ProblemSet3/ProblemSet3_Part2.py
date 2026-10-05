#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
with open(file='V:/ProblemSet3/ProblemSet3/data/raw/transshipment_vessels_20180723.csv',mode='r') as file_obj:

    #Read the entire contents into a list object
    line_list = file_obj.readlines()

#Save the contents of the first line in the list of lines to the variable "headerLineString"
header_line = line_list[0]

#Print the contents of the headerLine
print(header_line)