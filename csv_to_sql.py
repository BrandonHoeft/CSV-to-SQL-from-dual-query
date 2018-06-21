read_path = '/Users/bhoeft/Desktop/temp/fake_simulated_data.csv'
out_path = '/Users/bhoeft/Desktop/temp/output.txt'
###############################################################################
# Explore: captures headers row as a list, then prints each row line by line. 
###############################################################################

with open(read_path) as file:
    
    for i, line in enumerate(file): # file is an iterable.
        if i == 0:
            headers = line.rstrip('\n').split(',')
        elif i == 1:
            values = line.rstrip('\n').split(',')
            
        else:
            print(line)
    
    print(headers)
            

headers
values
for i, val in enumerate(values):
    print(i, val)
values[0]
"".join(("'", values[0], "'"))
# zip iterates over multiple objects in parallel. 
varchar_indices = (0,1,2,3,6,9,10,12)
date_indices = (13,14,15)

# good! need to convert string value columns to varchar plsql format.
values_as_varchar = ["".join(["'", val, "'"]) for i, val in enumerate(values) if i in varchar_indices]
# Check output
for i, char in enumerate(values_as_varchar):
    print(i, char)


# good! need to convert string value columns to varchar plsql format.
values_as_date = ["".join(["TO_DATE('", val, "', ", "'mm/dd/yyyy')"]) for i, val in enumerate(values) if i in date_indices]
for i, date in enumerate(values_as_date):
    print(i, date)


# good! need to combine value with header in a string. 
[val + ' AS ' + header for val, header in zip(values, headers)]










###############################################################################
# Development of query output.  
###############################################################################

with open(read_path) as file:
    
    for i, line in enumerate(file): # file is an iterable.
        if i == 0:
            headers = line.rstrip('\n').split(',')
        elif i == 1:
            values = line.rstrip('\n').split(',')
            value_header_list = [val + ' AS ' + header 
                                 for val, header in zip(values, headers)]
            
            'SELECT FROM dual UNION ALL'.format()
        else:
            print(line)
    
    print(headers)







###############################################################################
# Template structure for reading line by line and writing line by line.
###############################################################################

with open(read_path) as file:
    with open(out_path, 'a') as file_out: 
        for line in file:
            print(line)



datestr = '1956-01-31'
year, month, day = datestr.split('-')



'"Python"'

"'Python'"






#!/usr/bin/env python3
# -*- coding: utf-8 -*-