In order to create the index lists for report processing, you will need the header files.

From the header file, determine which questions have non-empty results and responses that professors would potentially like to see.
A general rule for filtering questions would be that, if the question has ANY non-null data in it, retain it in the created LAS.txt index list.
You can check for this by opening the general export from Blue in Excel, adding a filter to the whole document, and going question by question
to ensure it has some non-null result. 

This process, detailed above, will result in LAS.txt, which is your index list for the general course evaluations document. You will have to manually
make the index lists for other schools that had separate evaluations csvs. In 20202, these were BVC and BUS.

This project, given a LAS.txt index list, copies the questions for all of the schools in a given schools file.

For example, given LAS.txt and schools.xlsx (the creation of which will be detailed soon), it will generate ACAD.txt, ALI.txt, ..., THTR.txt in the 
designated output folder. Note that to run the script, the original index list must be named LAS.txt and the xlsx is schools.xlsx.

To create the schools.xlsx file:
- Open the export result from Blue
- Copy the 'School' column (which INCLUDES the ERR school added to blank schools)
--- This column can include the 'School' header (label). However, it is not necessary.
- Paste it into a new xlsx file that, as column A, has a long list of schools
--- Do not worry about duplicates, the script takes care of that

Now, open the cmd and run py create_index_list.py. The results will be in the output folder. 

Note: you will need to manually create some schools that have specified questions, such as MUS, ENGR, and PHAR (in 20202, at least). You can add to the index lists copied from LAS here.