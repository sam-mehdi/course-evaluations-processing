This is the most involved step. Most of the complexity lies in the very exact naming procedures and other small details.

0. Check Preprocessing.txt for necessary details on how to clean the data!

1. Open constant_c_schools.py. Here's what you need to change:
--- Line 4: Change the term (20202, 20171, etc.)
--- Line 19: Change schools array. Ex: [ 'BUS', 'BVC' ]. These are the schools that require separate processing from the general input data.
--- Lines 51 - 63: These are essentially the "Working_Header" from the header file, or the questions in the index list. You need to make different ones for each school.
--- Line 66: You may need to change the schools. Note that you do need to add the ERR school for blank schools, added in preprocessing.
After this, you can close out of constant_final.py. You won't need to change anything else.

2. In your file explorer, open Example Inputs. Note that they have to be named exactly as specified, with the term (20202, e.g.) as the only thing that may need to change in the naming.
They all need to be csv. You would need to refactor the code if you have .xlsx as inputs (mainly the lines that read_csv in final_report_processing_20202.py).
Note: if there are any inconsistencies between the naming in the README and the Example Input folder, always assume the Example Input folder is correct.
--- You will need to get the right files for: Data Files, Index Lists, and Header Files.
--- Data Files: there should be 1 general file (general_20202.csv, or change the corresponding term) --- NOTE: This file needs to be here. Otherwise, the script will fail.
--- Data Files: there should be 1 file per individual school (BUS_20202.csv, BVC_20202.csv)
--- Header Files: 1 general file (header_general_20202.csv)
You should use the adapted header files from the first part in this process and put those here (they need 'Working_Header' and 'Final_Header' columns, in addition to the 'Original_Header').
--- Header Files: 1 file per school (header_BUS_20202.csv and header_BVC_20202.csv)
--- Index Lists: These are the questions that each schools 'cares about,' which will appear in the final report. These are created in report_create_index_list.
Put the index lists in a Lecture folder within Raw_Test.

3. Run the script. In the command prompt: py report_processing_20202.py. This outputs files to Raw_Test.
Use these outputs to proceed to the next step: distributing these outputs to each professor in report_placement.