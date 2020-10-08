import os

# Change term here
term = '20202'

cwd = os.getcwd()
ROOT_PATH = cwd

# Paths for destination folders
RAW_DATA_PATH = cwd + '\\Raw_Test'
SCHEDULE_DATA_PATH = cwd + '\\Scheduling'

# General Data path
# name general data general_<term>.csv, and so on for the rest of the files
GENERAL_DATA = cwd + '\\Data Files\\general_' + term + '.csv'              # general_20202.csv
HEADER_GENERAL = cwd + '\\Header Files\\header_general_' + term + '.csv'   # header_general_20202.csv

# School data files
SCHOOLS = ['BVC' ]
SCHOOLS_DATA = dict( (school, cwd + '\\Data Files\\' + school + '_' + term + '.csv') for school in SCHOOLS )
HEADER_SCHOOLS = dict( (school,  cwd + '\\Header Files\\header_' + school + '_' + term + '.csv' ) for school in SCHOOLS )

# Replace map for cleaning the data:
REPLACE_MAP = {
    '\r\n': '',
    '\r': '',
    '\n': '',
    '&#x27': '',
    '&#x2F': '',
    '&quot;': '',
    '&ndash': '',
    '=': '',
    'â€™': '\'',
    '\\x27': '\''
}
### Look through the following index file names to ensure the structure is correct ###
# Raw General Index Files
LECTURE_INDEX_RAW_DATA =  cwd + '\\Index Lists\\Raw Data\\Lecture'

# Raw file names ( the brackets indicate it can be formatted. to use properly, do something like LECTURE_RAW_DATA_FILE.format('ENGR') )
LECTURE_RAW_DATA_FILE_NAME = '{}_Lecture_Raw_Data_' + term + '.xlsx'
DEPARTMENT_RAW_DATA_FILE_NAME = '{}_{}_Lecture_Raw_Data_' + term + '.csv'

# Raw Schools Index Files
SCHOOLS_LECTURE_INDEX_RAW_DATA = dict( (school,  cwd + '\\Index Lists\\Raw Data\\Lecture\\' + school + '.txt') for school in SCHOOLS )

# Skeleton for Department Reports
RAW_INDEX_LIST_SKELETON = cwd + '\\Index Lists\\Raw Data\\Lecture\\{}'

#General conditon for Valid Rows
LECTURE_ROWS = [ 'Q1_1', 'Q2_1', 'Q2_2', 'Q2_3', 'Q3_1', 'Q3_2', 'Q3_3', 'Q3_4', 'Q3_5', 'Q3_6', 'Q3_7', 'Q4_1', 'Q4_2',
                 'Q4_3', 'Q4_4', 'Q5_1', 'Q5_2', 'Q5_3', 'Q6_1', 'Q7_1', 'Q8_1', 'Q9_1', 'Q10_1', 'Q10_2', 'Q10_3', 'Q10_4',
                 'Q10_5', 'Q10_6', 'Q10_7', 'Q11_1', 'Q11_2', 'Q11_3', 'Q11_4', 'Q12_1', 'Q12_2', 'Q13_1', 'Q14_1', 'Q15_1',
                 'Q15_2', 'Q16_1', 'Q17_1', 'Q18_1', 'Q19_1', 'Q20_1', 'Q21_1', 'Q22_1', 'Q23_1', 'Q23_2', 'Q23_3', 'Q23_4', 
                 'Q23_5', 'Q23_6', 'Q23_7', 'Q23_8', 'Q24_1']

#General Schools conditon for Valid Rows (\ just tells the compiler to 'look at the next line, the expression is not yet complete')
GEN_SCHOOLS_LECTURE_ROWS = \ 
{'BUS': ['Q1_1', 'Q2_1', 'Q2_2', 'Q2_3', 'Q2_4', 'Q2_5', 'Q2_6', 'Q2_7', 'Q2_8', 'Q2_9', 'Q2_10', 'Q6_1', 'Q8_1', 'Q15_1'],
         \
 'BVC': ['Q1_1', 'Q2_1', 'Q2_2', 'Q2_3', 'Q3_1', 'Q3_2', 'Q3_3', 'Q3_4', 'Q3_5', 'Q3_6', 'Q3_7', 'Q4_1', 'Q4_2', 'Q4_3',
         'Q4_4', 'Q5_1', 'Q5_2', 'Q5_3', 'Q7_1', 'Q8_1', 'Q9_1', 'Q15_1', 'Q15_2', 'Q16_1', 'Q17_1', 'Q18_1', ]   
         }

#Constants for report verification
SCHOOL_NAMES = ['ACAD', 'ALI', 'ANSC', 'ARCH', 'BUS', 'BVC', 'CNTV', 'DANC', 'DENT', 'EDUC', 'ENGR', 'ERR', 'FA', 'GERO', 'LAS', 'LAW', 'MED', 'MUS', 'OT', 'PHAR', 'PPD', 'PT', 'SOWK', 'THTR']