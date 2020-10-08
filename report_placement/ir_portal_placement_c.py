import constant_c as constant
import os
import pandas as pd
import shutil
import re

# READ BEFORE USE:
# This file is for placing the course reports within this script's folder.
# For automated placement (if you have access to the S: drive), use ir_portal_placement.py
# The _c at the end of the file name (i.e. this file) indicates that this script will 
# place the course reports on this computer's C: drive.

USER_DISTRIBUTION_FILE = r'scheduling_distribution_list_' + constant.term + '.csv'

user_file = pd.read_csv(USER_DISTRIBUTION_FILE)

school = list()

# First, get all the schools that will be distributed to
cwd = os.getcwd()
if constant.SCHEDULING:
    os.chdir(constant.SCHEDULE_DATA_PATH + '\\')
elif constant.RAW:
    os.chdir(constant.RAW_DATA_PATH + '\\')
elif constant.AGG:
    os.chdir(constant.AGG_DATA_PATH + '\\')
else:
    print('No data was inputted! Check constant_c.py and the README!')
for file in os.listdir():
    school.append(file.split('_'[0])[0])
print(school)
os.chdir(cwd)

create_file_dict = {'NSCI': 'LAS', 'PM': 'MED', 'MEDS': 'MED', 'MPTX': 'PHAR', 'PSCI': 'PHAR'}

########################################################################################
# 
def special_report(new_school_name, old_school_name, path, prof_folder):
    '''
    @precondition: os is currently at folder containing the script.
    @parameters:
    new_school_name: the key in the above dictionary (NSCI, ACAD)
    old_school_name: the value in the above dictionary (LAS, FA)
    path - either RAW_DATA or AGG_DATA
    prof_folder - _pvt_prof
    '''
    print("Generating special report for " + new_school_name)

    base_path = os.getcwd()

    # Go to either aggregate or raw data path
    os.chdir(path)
    files = os.listdir(old_school_name)
    os.chdir(old_school_name)

    # Having a list of file names which need to be processed further
    original_file_names = [constant.LECTURE_RAW_DATA_FILE_NAME.format(old_school_name),
                           constant.DISCUSSION_RAW_DATA_FILE_NAME.format(old_school_name),
                           constant.LAB_RAW_DATA_FILE_NAME.format(old_school_name),
                           constant.LECTURE_TA_RAW_DATA_FILE_NAME.format(old_school_name),
                           constant.LECTURE_AGG_DATA_FILE_NAME.format(old_school_name),
                           constant.DISCUSSION_AGG_DATA_FILE_NAME.format(old_school_name),
                           constant.LAB_AGG_DATA_FILE_NAME.format(old_school_name),
                           constant.LECTURE_TA_AGG_DATA_FILE_NAME.format(old_school_name)
                           ]

    final_destination = base_path + '\\Reports\\' + old_school_name + '\\' + prof_folder + '\\'
    #print(final_destination)
 
    for file in files:
        if file in original_file_names:

            file_data_frame = pd.read_csv(file, encoding='ISO-8859-1')
            file_data_frame = file_data_frame.loc[file_data_frame['Department'] == new_school_name]
            #print("File name ",new_school_name, "Length ", len(file_data_frame))
            if(len(file_data_frame) > 0):
                file.replace(old_school_name, new_school_name)
                new_file_name = re.sub(old_school_name, new_school_name, file)
                file_data_frame.to_csv(new_file_name, index=False)

                if not os.path.exists(final_destination):
                    os.makedirs(final_destination)
                shutil.copy(new_file_name, final_destination)


    os.chdir(base_path)
########################################################################################

########################################################################################
def move_to_folder(school, prof_folder, path):
    '''
    @precondition: os is currently at folder containing the script.
    Note: outputted file structure has a general reports folder, and then it is distinguished by school. Ex:
    reports/ENGR/_pvt_prof
    @parameters:
    school - ENGR, MED, etc.
    prof_folder - _pvt_prof
    path - either RAW_DATA or AGG_DATA

    '''
    if school in create_file_dict:
        school = create_file_dict[school]

    # 0th, get the base path and the destination path:
    base_path = os.getcwd()
    destination_path = base_path + '\\Reports\\' + school + '\\' + prof_folder + '\\'
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # First, get the right spreadsheet for that school
    school_data_path = path + '\\' + school
    
    # Next, copy all files from the school report folder to the professor's folder
    files = os.listdir(school_data_path)
    for file in files:
        # Ensure it's the right file
        if (file.__contains__(school)):
            # Copy the .xlsx to the professor's folder
            full_file_name = school_data_path + '\\' + file
            shutil.copy(full_file_name, destination_path)
########################################################################################

# First, create and navigate to general reports folder
if not os.path.exists('Reports'):
    os.makedirs('Reports')

for sch in school:
    print("Generating report for {}".format(sch))

    # Each row from report distribution list is a professor who needs to receive this report
    rows = user_file.loc[user_file['School'] == sch]

    # Each professor in this school has their own folder for the reports
    for row in rows['Folder'].values:
        # Dealing with Raw data files:
        if constant.RAW:
            if sch in create_file_dict:
                special_report(sch, create_file_dict[sch], constant.RAW_DATA_PATH, row)
            else:
                move_to_folder(sch, row, constant.RAW_DATA_PATH)

        # Aggregate data files:
        if constant.AGG:
            if sch in create_file_dict:
                special_report(sch, create_file_dict[sch], constant.AGG_DATA_PATH, row)
            else:
                move_to_folder(sch, row, constant.AGG_DATA_PATH)
        
        # Schedules
        if constant.SCHEDULING:
            move_to_folder(sch, row, constant.SCHEDULE_DATA_PATH)