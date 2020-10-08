0. Ensure that there are no rows with empty schools. This script creates folders based on school names, and a folder cannot have an empty name.
--- To resolve this: Go through the files and sort the School column A-Z. Below Z, there would be courses without Schools. Fill these in with something
that indicates an error, such as "A."

In addition, you must ensure the encodings of all files are correct. 
--- Go CSV by CSV and open them in Notepad++. 
--- At the top menu bar, go to "Encoding." If the encoding is not already UTF-8 or UTF-8-BOM, convert it to UTF-8-BOM.

1. Ensure all libraries for running the script are installed. These include:
- pandas (pip install pandas)
- xlsxwriter (pip install xlsxwriter)
There may be a couple of more, but these are the ones I am certain about.

2. Configuring the script: 
Be sure to change the terms in these filenames. Otherwise, following their naming convention exactly.
- Default_Scheduling_20202.csv
- Scheduled_Courses_20202.csv
- no_instructor_20202.csv
- Excluded_Courses_20202.csv
You will still need to configure the term of the files as well:
--- Open constant_c.py
--- On line 3 is the term. Change it to the correct one.

3. Running the script:
To run the script, open up a command prompt or terminal in the directory. An easy way to do this on Windows is to type 'cmd' in the file address bar from Windows Explorer,
and press enter.
In a cmd or terminal, run the script with:
py schedule_report_processing_with_school_folders.py

Don't worry about all the warnings.
This outputs separate Excel workbooks. If this is the desired output, then you're done! To combine these workbooks into a single one with multiple worksheets, run:
py combine_school_excels.py

4. Done!

POTENTIAL ERRORS:
- SyntaxError: print(EXTERNSHEET B7) (something like this)
--- This is caused by a corrupted xlrd.
--- You will need to delete xlrd. Find it in the following path (in your Python directory, the following is default):
----- C:\Users\<USERNAME>\AppData\Local\Programs\Python\Python36\Lib\site-packages
--- From there, scroll to the bottom and delete both the xlrd folder and the xlrd egg file.
--- Now, run a command prompt and install xlrd again (pip install xlrd).
--- You should be able to run it now!

- TypeError: stat: path should be string, bytes, os.PathLike or integer, not float
--- This error indicates that, in one of the files, the school is missing.
--- At the top of the error (below Traceback), you should be able to find the line at which the error is caused. This line will indicates
which file is being problematic.
--- Open that file, filter the School column, and filter for Blanks. Replace those blanks with "A" or whatever you named your error school.

- UnicodeDecodeError: 'utf-8' codec can't decode byte 0xfd in position 7209: invalid start byte
--- This is a problem with the encoding.
--- You can once again go to the top of the error to find the problematic file.
--- Open that file in Notepad++, go to encoding, and the encoding probably isn't UTF-8 or UTF-8-BOM. Convert it to UTF-8-BOM.
--- Save the file and run again.

- ValueError: time data '25-Nov-20' does not match format '%m/%d/%Y'
--- This is a problem with the time formatting in the file.
--- Once again, figure out which file is causing problems. You can figure this out by the top of the error.
--- Go to the corresponding line in schedule_report_processing_with_school_folders.py where that datetime is parsed:
----- no_instructor: 52
----- Default_Scheduling: 56
--- Once you're there, try to change the datetime format to correspond.
----- for example, in the above error, you'd have to change it to '%d/%b/%y'
----- Here is an excellent guide on the datetimes, detailing all of the abbreviations: https://www.programiz.com/python-programming/datetime/strptime

- KeyError: 'Evaluation_Start'
--- This is caused by a bad reference to a column by the program.
--- For example, the program might be trying to access the column 'Evaluation_Start,' but the column is actually 'Eval_Start.'
--- Find the file that is causing this error. Instead of going into that file, go to where it is processed in the code:
----- no_instructor: 52
----- Default_Scheduling: 56
----- Scheduled_Courses: 60
--- Open the corresponding file and find the column in question. Replace the code reference to it.
--- Note: this error may be caused with other columns. For example, it might be KeyError: 'Course_Department'. Feel free to change all of these references in the code.