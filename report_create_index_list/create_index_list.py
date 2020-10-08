import pandas as pd
import os
import openpyxl

cwd = os.getcwd()

output_folder = "\\copies\\"

LAS_file = "LAS.txt"

schools = "schools.xlsx"

if not os.path.exists(cwd + output_folder):
    os.makedirs(cwd + output_folder)

# First, get the list of schools

schools_list = list(set(pd.read_excel(schools, engine='openpyxl')['School']))
print("Read Schools:")
print(schools_list)

# Next, get the LAS file's data
with open(LAS_file, 'r') as f:
    data = f.read()
    # For each school, create a txt file named after it with LAS_file data
    os.chdir(cwd + output_folder)
    for school in schools_list:
        print("Creating {}.txt".format(school))
        new_file = open("{}.txt".format(school), 'x')
        new_file.write(data)
    os.chdir(cwd)
print("Done!")