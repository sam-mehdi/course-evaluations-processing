import pandas as pd
import os
import pandas.io.formats.excel as pde
from datetime import datetime
import shutil
import constant_c as constant

pde.header_style = None

def get_col_widths(dataframe):
    # First we find the maximum length of the index column
    idx_max = max([len(str(s)) for s in dataframe.index.values] + [len(str(dataframe.index.name))])
    # Then, we concatenate this to the max of the lengths of column name and its values for each column, left to right
    return [idx_max] + [max([len(str(s)) for s in dataframe[col].values] + [len(col)]) for col in dataframe.columns]

# Create function that will parse evaluation scheduling data from access. File is the name of the file to be processed,
# filename_skeleton will be the frame of how you want the output file to be formatted, and the wd is the working
# directory you want to do this in (currently set to just do it in the working directory of this file.
def scheduling_report_generation(file, filename_skeleton, wd, output_path):
    term = constant.term
    # Read CSV file, ANSII coding is default from excel, mbcs is python's encoding for ANSII
    os.chdir(wd)
    
    data = pd.read_csv(file, encoding='utf-8-sig', infer_datetime_format=True) #encoding should be utf-8-sig
    print(file)
    os.chdir(output_path)

    print(data.dtypes)
    # Sort these files
    data = data.sort_values(by=['School'])
    # Get a unique list of all the schools present in the file. You will return this at the end of the function.
    school_list = list(set(data['School']))
    # Iterate through each school type in the data frame
    for school in school_list:
        
        # Check to see if a folder currently exists in the working directory for the school, and if it doesn't exist
        # create it and change the working directory to be within this school folder
        if not os.path.exists(school):
            os.makedirs(school)
        os.chdir(school)
        # Group the dataframe by school and grab only the subset of rows for the school that is currently being
        # processed
        school_report = data.groupby(data['School']).get_group(school)
        # Populate the filename using the skeleton provided at the function's input and the name of the school being
        # processed
        filename = filename_skeleton.format(school)
        # Indicates to user which file is being created
        print('Creating', filename)
        # Sort file by evaluation start date only for files who have it included and write the data frame to the output
        # file
        if file == 'no_instructor_' + term + '.csv':
            school_report['sort'] = [datetime.strptime(x, '%d-%b-%y') for x in school_report['Eval_Start']]
            school_report = school_report.sort_values(by=['sort'])
            school_report = school_report.drop(labels='sort', axis=1)
        elif file == 'Default_Scheduling_' + term + '.csv': #i.e. Default_Scheduling
            school_report['sort'] = [datetime.strptime(x, '%m/%d/%Y') for x in school_report['Evaluation_start']]
            school_report = school_report.sort_values(by=['sort'])
            school_report = school_report.drop(labels='sort', axis=1)
        elif file == 'Scheduled_Courses_' + term + '.csv': #i.e. this handles Scheduled_Courses
            school_report['sort'] = [x for x in school_report['Eval_Start']]
            school_report = school_report.sort_values(by=['sort'])
            school_report = school_report.drop(labels='sort', axis=1)
        else: # this handles excluded_courses
            school_report = school_report.sort_values(by=['Course_Department', 'Section_ID'])
        
        # Write to Excel
        writer = pd.ExcelWriter(filename.split('.')[0] + '.xlsx', engine='xlsxwriter')
        school_report.to_excel(writer, index=False, sheet_name=school)

        # Formatting
        workbook = writer.book
        worksheet = writer.sheets[school]
        header_format = workbook.add_format({'bold': True})
        worksheet.set_row(0, 15, header_format)
        for i, width in enumerate(get_col_widths(school_report)):
            i = i - 1
            width = width + 1
            worksheet.set_column(i, i, width)
        writer.save()
        # Change working directory back to output folder
        os.chdir(output_path)
    # Return the school list at end of processing
    return school_list


###############################################################################################################################
#################                                       Main Execution                                  #######################
###############################################################################################################################

term = constant.term 

# Get current working directory, and make the output folder if it doesn't already exist
path = constant.cwd
output_path = constant.output_path
if not os.path.exists(output_path):
    os.makedirs(output_path)
# Process scheduled courses data. Note that this file extension is different because of certain inputs.
scheduled_school_list = scheduling_report_generation('Scheduled_Courses_' + term + '.csv', '{}_Scheduled_Courses_' + term + '.xlsx', path, output_path)
# Process excluded courses data
excluded_school_list = scheduling_report_generation('Excluded_Courses_'+ term + '.csv', '{}_Excluded_Courses_' + term + '.xlsx', path, output_path)
# Process default scheduling data
default_school_list = scheduling_report_generation('Default_Scheduling_' + term + '.csv', '{}_Default_Scheduling_' + term + '.xlsx', path, output_path)
# Process valid course but no instructor data
valid_course_no_instructor_school_list = scheduling_report_generation('no_instructor_' + term + '.csv', '{}_no_instructor_' + term + '.xlsx', path, output_path)