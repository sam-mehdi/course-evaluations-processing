This script distributes the processed course evaluations and scheduling to the professors' _pvt_ folders.

Note: you may want to use this script for either scheduling or report processing or both. In order to choose which, go to lines 5 - 7
of constant_c.py. Set True/False accordingly. REPLACE <term> WITH THE TERM TOO! (like 20202 or 20203)

0. Depending on what you want to process, you can set the lines in constant_c.py (RAW, AGG, and SCHEDULING) to True/False.

1. Ensure you have the right term. In constant_c.py, change the term on line 3.

2. (if applicable) Put Raw_Data and Aggregated_Data into their respective folders (just copy and paste all the output from report_processing_<term>)

3. (if applicable) Put output from report_scheduling_<term> into Scheduling folders

4. Ensure you have a distribution list named in this exact fashion: scheduling_distribution_list_<term>.csv

5. run the script: py ir_portal_placement.py

Output folder should now have all your results! These are the end product. You are all done!
