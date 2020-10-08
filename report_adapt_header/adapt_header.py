import pandas as pd
import os
from pathlib import Path

cwd = os.getcwd()

# The directory that provides the base header files
HEADER_INPUT = cwd + '\\headers_input\\'

# The directory that will contain the processed headers
HEADER_OUTPUT = cwd + '\\headers_output\\'

# Make the output folder if it doesn't exist
if not os.path.exists(HEADER_OUTPUT):
    os.makedirs(HEADER_OUTPUT)

# The headings for the new header files:
headings = [ 'Original_Header', 'Working_Header', 'Final_Header']

# Get all the headers
files = os.listdir(HEADER_INPUT)

for file in files:    
    print('Adapting {}'.format(file))
    # The input file
    input = pd.read_csv(HEADER_INPUT + file, encoding='latin1', header=None)
    #print(input)

    # The base output
    data = pd.DataFrame(columns=headings)

    #first, copy everything into 'Original Header'
    for i in range (0, input.shape[0]):
        data = data.append( { 'Original_Header': input.loc[i,0], 'Working_Header':'', 'Final_Header':'' }, ignore_index=True )

    # Variables to track Q1_1, Q1_2, and so on
    question = 1
    sub_question = 1

    # Go through all the questions/headers/rows
    for i in range(0, len(data)):
        # If the first letter in that item in Q
        if data.iloc[i,0][0] == 'Q':
            # Get the # question this is
            q = ""
            index = 1
            char = data.iloc[i, 0][index]
            while char != '_':
                q += char
                index += 1
                char = data.iloc[i,0][index]

            # Sometimes need to advance to next question
            if not int(q) == question:
                sub_question = 1
                question = int(q)
            # Create a working header
            original_header = data.iloc[i,0].split('_')
            working_header = original_header[0] + '_' + str(sub_question)
            data.iloc[i,1] = working_header

            # Set the final header. It combines the working header with the end of the original header
            data.iloc[i,2] = working_header + '_' + original_header[1]

            sub_question = sub_question + 1
        else:
            # Otherwise, just copy the original header into the other two
            data.iloc[i, 1] = data.iloc[i, 0]
            data.iloc[i, 2] = data.iloc[i, 0]
    
    # Make an index column
    data.insert(0, 'Index', data.index)
    # Write data to a new csv
    data.to_csv(HEADER_OUTPUT + Path(file).stem + '_adapted.csv', encoding='latin1', index=False)

print('Success!')