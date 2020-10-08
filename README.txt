Each of the subfolders have more specific READMEs. This one will just guide you to each folder in order.

First, be sure you have the following libraries installed. To install them, use the command in the parentheses (from the command line):
- pandas (pip install pandas)
- xlsxwriter (pip install xlsxwriter)
- openpyxl (pip install openpyxl)
If this doesn't work, feel free to ask me! 

You may also need to delete the _pycache_ folders before running the scripts from the command line.

Input folders may have "Dummy" files. You should delete those. If there are none, don't worry about it. Sharepoint might have obliterated them already.

0. Clean the data with find and replace alls in Excel. Specifically, make the following replacemenets from ALL data files (general, BVC, BUS, etc.):
--- Replace ’ with '
--- Replace â€™ with '.
--- Replace \x27 with '.
These last two replacements may not come up with anything, and that's ok. They are just in case some encoding errors have already happened.

In addition, you MUST assign every evaluation to a school. In other words, every record must have a school.
--- Check for this by filtering the CSV in Excel on School, and filter for all Blank records, if there are any.
--- Replace all of these records with ERR, or any 'school name' that would indicate a lack of a school.

1. report_adapt_header changes the header from the base single column version to a multi-column version with a
'Working_Header' and a 'Final_Header'. Run this first. See the README in that folder for more details.

2. Next, report_processing. This takes the Raw and Aggregated course evaluations csvs, processes them, and distributes them to each school.

3. report_scheduling. This is independent from the previous two steps. It separates general course scheduling files per school.

4. report_placement distributes both the evaluations and the scheduling reports to professors' folders.

If anything goes wrong, please let me know! 