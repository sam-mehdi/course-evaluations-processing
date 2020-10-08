import pandas as pd
# import xlrd # This was for reading an Excel file for data files
import os
import constant_final as constant
import pandas.io.formats.excel
pandas.io.formats.excel.header_style = None # This if for formatting the header in the resulting Excels. Purely aesthetic.

# # # # # # # # # # # # # # # # Gather data # # # # # # # # # # # # # # # # 

print("Gathering General Data")

general_data = pd.read_csv(constant.GENERAL_DATA, index_col=False, na_values=(['D/A', 'NULL', 'NRP', 'N/A', '']), encoding='ISO-8859-2')
print("Number of rows read: {}".format(len(general_data)))
print("Gathering General Schools Data")
print("About to cause a warning! Don't worry!")
general_schools_data_values = [ pd.read_csv(constant.SCHOOLS_DATA[school], index_col=False, na_values=(['D/A', 'NULL', 'NRP', 'N/A', '']),encoding='ISO-8859-2') for school in constant.SCHOOLS ]
general_schools_data = { k:v for (k,v) in zip(constant.SCHOOLS, general_schools_data_values) }

print("Finished data gathering")
print("Schools read:")
print(constant.SCHOOLS)

print("Cleaning the data")

def clean_data(df):
    df.replace(constant.REPLACE_MAP, inplace=True)

general_data['User ID'] = general_data['User ID'].str.replace('Data4_', '')
general_data['Object ID'] = general_data['Object ID'].str.replace('Data3_', '')
clean_data(general_data)

for school in constant.SCHOOLS:
    general_schools_data[school]['User ID'] = general_schools_data[school]['User ID'].str.replace('Data4_', '') 
    general_schools_data[school]['Object ID'] = general_schools_data[school]['Object ID'].str.replace('Data3_', '')
    clean_data(general_schools_data[school])

# # # # # # # # # # # # # # # # Header data # # # # # # # # # # # # # # # # 

print("Gathering header data for General")

general_header = pd.read_csv(constant.HEADER_GENERAL)
general_header_rename = dict(zip(general_header['Original_Header'].to_list(), general_header['Working_Header'].to_list()))
general_header_dictionary = dict(zip(general_header['Working_Header'].tolist(), general_header['Final_Header'].tolist()))

print("Gathering header data for schools")
general_schools_header_values = [ pd.read_csv(constant.HEADER_SCHOOLS[school], encoding='ISO-8859-2') for school in constant.SCHOOLS ] 
general_schools_header = { k:v for (k,v) in zip(constant.SCHOOLS, general_schools_header_values)}
print("Creating dictionary")
general_schools_header_dictionary_values = [ dict(zip(general_schools_header[school]['Working_Header'].tolist(), general_schools_header[school]['Final_Header'].tolist())) for school in constant.SCHOOLS]
general_schools_header_dictionary = { k:v for (k,v) in zip(constant.SCHOOLS, general_schools_header_dictionary_values)}
print("Creating Rename")
general_schools_header_rename_values = [ dict(zip(general_schools_header[school]['Original_Header'].tolist(), general_schools_header[school]['Working_Header'].tolist())) for school in constant.SCHOOLS]
general_schools_header_rename = { k:v for (k,v) in zip(constant.SCHOOLS, general_schools_header_rename_values)}

# # # # # # # # # # # # # # # # Index lists # # # # # # # # # # # # # # # # 

print("Gathering index lists")

general_index_dictionary = dict()

for f in (os.listdir(constant.LECTURE_INDEX_RAW_DATA)):
    fname = f.split('.')
    iname = fname[0]
    with open(r'Index Lists/Raw Data/Lecture/{}'.format(f)) as fhand:
        index_list = (fhand.read().splitlines())
        general_index_dictionary[iname] = index_list

# # # # # # # # # # # # # # # # Generate column data # # # # # # # # # # # # # # # # 

print("Generating column data")

general_schools_lecture_cols = dict()

for school in constant.SCHOOLS:
    with open(constant.SCHOOLS_LECTURE_INDEX_RAW_DATA[school]) as fhand:
        general_schools_lecture_cols[school] = (fhand.read().splitlines())

# Generic function to check for conditions
def getValidRows(data_struct, valid_condn, is_lecture=False):
    state = False

    # For each question in the Lecture Rows
    for condn in valid_condn:
        if not condn.startswith('Q1'): # We want to exempt Q1, as this question can result in empty evaluations
            state = state | data_struct[condn].notnull()
    
    # Keep the row if one of the lecture rows is properly filled out
    return data_struct[state]

# # # # # # # # # # # # # # # # Gather lecture data # # # # # # # # # # # # # # # # 

print("Gather Lecture, Discussion, and Lab data")

# First, rename the columns in general_data, swapping the long form questions for the Q1_1, etc.
general_data.rename(columns=general_header_rename, inplace=True)
#print(general_data.columns)

# General lecture data

general_lecture = general_data #[(general_data['Course Type'] == 'LECTURE')] This would be if we're separting Labs, discussions, and lectures, which we aren't doing
print("Length of lecture including non-submitted: {}".format(len(general_lecture)))
general_valid_lecture = getValidRows(general_lecture, constant.LECTURE_ROWS, True)
print("Length of valid lecture, excluding non-submitted: {}".format(len(general_valid_lecture)))

# Get a list of the valid schools and remove the 'nan' one
general_lecture_school_list = general_valid_lecture.School.unique()
print(general_lecture_school_list)

# Lecture data for individual schools
for school in general_schools_data:
    #print(general_schools_header_rename[school])
    general_schools_data[school].rename(columns=general_schools_header_rename[school], inplace=True)
    #print(school)
    #for item in general_schools_data[school].columns:
        #print(item)

general_schools_lecture_values = [ general_schools_data[school] for school in constant.SCHOOLS ] #[(general_schools_data[school]['Course Type'] == 'LECTURE')]
general_schools_lecture = { k:v for (k,v) in zip(constant.SCHOOLS, general_schools_lecture_values) }

general_schools_valid_lecture_values = [ getValidRows(general_schools_lecture[school], constant.GEN_SCHOOLS_LECTURE_ROWS[school]) for school in constant.SCHOOLS ]
general_schools_valid_lecture = { k:v for (k,v) in zip(constant.SCHOOLS, general_schools_valid_lecture_values) }

general_schools_lecture_department_list_values = [ list(set(general_schools_valid_lecture[school]['Course Department'])) for school in constant.SCHOOLS ]
general_schools_lecture_department_list = { k:v for (k,v) in zip(constant.SCHOOLS, general_schools_lecture_department_list_values) }

# # # # # # # # # # # # # # # # Generate reports # # # # # # # # # # # # # # # # 

print("Generating reports")

def generateDepartmentReport(file_name_to_be_saved, school_name, department_list, valid_lecture, path):
    os.chdir(constant.ROOT_PATH)
    for f in os.listdir(constant.LECTURE_INDEX_RAW_DATA):
        fname = f.split('.')
        dept_name = fname[0]
        if(f in department_list):
            with open(r'Index Lists/Raw Data/Lecture/{}'.format(f)) as dhand:
                dept_columns = (dhand.read().splitlines())
                # print("School name ", school_name)
                # print("Deparment name ", f)
                # print("Department columns ",dept_columns)
                df_department_cols = pd.DataFrame(valid_lecture, columns=dept_columns)
                # print("Data frame columns are", list(df_department_cols))
                generateDepartmentOutput(constant.DEPARTMENT_RAW_DATA_FILE_NAME, df_department_cols, school_name, dept_name)

def generateDepartmentOutput(dept_name_to_be_saved, df, school_name, department_name):
    grouped_df_school = df.groupby(df['School']).get_group(school_name)
    group_df_department = grouped_df_school.groupby(grouped_df_school['Course Department']).get_group(department_name)
    group_df_department = group_df_department.sort_values(by=['Course Department', 'Section', 'Last Name'])
    group_df_department = group_df_department.rename(columns=general_header_dictionary)

    os.chdir(constant.RAW_DATA_PATH)

    if not os.path.exists(school_name):
        os.makedirs(school_name)
    os.chdir(school_name)
    group_df_department.to_csv(dept_name_to_be_saved.format(school_name, department_name), index=False)
    os.chdir(constant.ROOT_PATH)

def generateOutput(file_name_to_be_saved, df, school, header_dictionary, final_header_name, path):
    os.chdir(path)
    grouped_df = df.groupby(df['School']).get_group(school)
    grouped_df = grouped_df.sort_values(by=['Course Department', 'Section', 'Last Name'])
    grouped_df = grouped_df.rename(columns=final_header_name)
    if not os.path.exists(school):
        os.makedirs(school)
    os.chdir(school)
    writer = pd.ExcelWriter(file_name_to_be_saved.format(school), engine='xlsxwriter')
    print('Creating {}'.format(file_name_to_be_saved.format(school)))
    grouped_df.to_excel(writer, sheet_name=school, index=False)
    writer.save()
    os.chdir(path)

def handleData(file_name_to_be_saved, school_list, index_dictionary, final_header_names, valid_lecture, path, isLecture, shouldProcessDept, df=None):
    if len(school_list) > 0:
        #print("School list: ")
        #print(school_list)
        for school in school_list:
            # If data frame is not sent, which is the case for lectures. Generate them at every iteration
            os.chdir(path)
            if isLecture == True:
                df = pd.DataFrame(valid_lecture, columns=index_dictionary[school])
            generateOutput(file_name_to_be_saved, df, school, index_dictionary, final_header_names, path)
    
def create_schools_workbook(data, ctype, dtype, name_list, header, path, school):
    if not os.path.exists(school):
        os.makedirs(school)
    os.chdir(school)
    file = r'{}_{}_{}_{}.xlsx'.format(school, ctype, dtype, constant.term)
    print('Creating', file)
    writer = pd.ExcelWriter(file, engine='xlsxwriter')
    for department_name in sorted(name_list):
        # Group lecture data by school and select school in list
        # print("Ctype is ",ctype)
        # print("Dtype ",dtype)
        # print("department name is ",department_name)
        # grouped_data = data.groupby(data['Department']).get_group(department_name)
        grouped_data = data.groupby(data['Course Department'])
        # TODO : Need to verify this update with Robyn
        # Addding this check in case a department name is missing in the grouped data
        # if department_name in grouped_data.groups.keys():
        grouped_data = grouped_data.get_group(department_name)
        # Create the csv file
        grouped_data = grouped_data.sort_values(by=['Course Department', 'Section', 'Last Name'])
        grouped_data = grouped_data.rename(columns=header)
        grouped_data.to_excel(writer, sheet_name=department_name, index=False)
    data = data.rename(columns=header)
    data.to_excel(writer, sheet_name='ALL_' + school, index=False)
    writer.save()
    print("Workbook created")
    os.chdir(path)

def generateGeneralReport():
    # Generating data frames for the discussion and the labes
    path = constant.RAW_DATA_PATH
    os.chdir(path)
    #general_df_lecture_ta = pd.DataFrame(general_valid_lecture_ta, columns=general_lecture_ta_cols)
    # pass 1) name of the file to be saved
    #      2) which list to use (lecture, discussion lab or lecture_ta)
    #      3) send the path
    #      4) send the appropriate data format
    handleData(constant.LECTURE_RAW_DATA_FILE_NAME, general_lecture_school_list, general_index_dictionary, general_header_dictionary, general_valid_lecture, path, True, True)

def generateSchoolsGeneralReport():
    print("Generating Schools General Report")
    path = constant.RAW_DATA_PATH
    os.chdir(path)

    general_schools_df_lecture_values = [ pd.DataFrame(general_schools_valid_lecture[school], columns=general_schools_lecture_cols[school]) for school in constant.SCHOOLS ]
    general_schools_df_lecture = { k:v for (k,v) in zip(constant.SCHOOLS, general_schools_df_lecture_values) }

    for school in constant.SCHOOLS:
        create_schools_workbook(general_schools_df_lecture[school], "Lecture", "Raw_Data", general_schools_lecture_department_list[school], general_schools_header_dictionary[school], path, school) 

print("Generating General Data")
generateGeneralReport()
print("General report completed")

print("Generating General Schools Data")
generateSchoolsGeneralReport()
print("General Schools Generated")

print("Done!")