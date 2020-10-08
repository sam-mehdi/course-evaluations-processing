import pandas as pd
import constant_c as constant
import os

# This file will combine the outputted Excel files into a single file with multiple worksheets.

# Combines individual Excel files into one file with a number of worksheets
def combine_excels(school_list, wd):
    # For every school
    for school in school_list:

        print("Combining {}".format(school))

        # Navigate to that school's folder. If it doesn't exist, go next.
        if not os.path.exists(school):
            continue # should rarely trigger
        path = os.chdir(school)

        # Create an Excel file that will contain all the worksheets
        output_file = "{}_scheduling_" + constant.term + ".xlsx".format(school)
        writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

        # For each file in the school's folder
        for file in os.listdir(path):
            # Unless it's the output file
            if file == output_file:
                continue

            # Create a new worksheet for that file (without the .xlsx ending)
            worksheet_name = file.split('.')[0]
            new_data = pd.read_excel(file) # get that Excel's data
            new_data.to_excel(writer, index=False, sheet_name=worksheet_name) # put it in a new worksheet

            # Delete the Excel file
            os.remove(file)

        # Save the new Excel file
        writer.save()

        # Change the path back up
        path = os.chdir(wd)

# Get the list of schools from the Scheduled_Courses file
data = pd.read_csv('Scheduled_Courses_' + constant.term + '.csv', infer_datetime_format=True)
school_list = list(set(data['School']))

cwd = os.getcwd()
os.chdir(constant.output_path)
# Go to the output folder
combine_excels(school_list, constant.output_path)
os.chdir(cwd)