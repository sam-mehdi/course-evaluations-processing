import os

term = '20203'

RAW = False
AGG = False
SCHEDULING = True

cwd = os.getcwd()
RAW_DATA_PATH = cwd + '\\Raw_Test'
AGG_DATA_PATH = cwd + '\\Aggregated_Test'
SCHEDULE_DATA_PATH = cwd + '\\Scheduling'

# Raw file names
LECTURE_RAW_DATA_FILE_NAME = '{}_Lecture_Raw_Data_' + term + '.csv'
DISCUSSION_RAW_DATA_FILE_NAME = '{}_Discussion_Raw_Data_' + term + '.csv'
LAB_RAW_DATA_FILE_NAME = '{}_Lab_Raw_Data_' + term + '.csv'
LECTURE_TA_RAW_DATA_FILE_NAME = '{}_Lecture_TA_Raw_Data_' + term + '.csv'

# Aggregate file names
LECTURE_AGG_DATA_FILE_NAME = '{}_Lecture_Aggregated_Data_' + term + '.csv'
DISCUSSION_AGG_DATA_FILE_NAME = '{}_Discussion_Aggregated_Data_' + term + '.csv'
LAB_AGG_DATA_FILE_NAME = '{}_Lab_Aggregated_Data_' + term + '.csv'
LECTURE_TA_AGG_DATA_FILE_NAME = '{}_Lecture_TA_Aggregated_Data_' + term + '.csv'