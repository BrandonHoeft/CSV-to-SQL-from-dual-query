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
            # 1. need to format the anticipated SQL varchar elements.
            # IN-PROGRESS BELOW
            # 2. need to clean the anticipated SQL date type elements
            # IN-PROGRESS BELOW
            # 3. need to update the values list with cleaned varchar, date type vals
            # TO DO
            # 4. join the value with the header as query string
            # IN-PROGRESS BELOW
            # 5. format a select statement for the first FROM dual query.
            # TO DO
        elif i > 1:
            None
        else:
            print(line)
    

    print(headers)
            

headers
values
for i, val in enumerate(values):
    print(i, val)
values[0]


# identify values indices that need special formatting for a SQL statement. 
varchar_indices = (0,1,2,3,6,9,10,12)
date_indices = (13,14,15)

# 1. need to format the anticipated SQL varchar elements. GOOD!
values_as_varchar = ["".join(["'", val, "'"]) for i, val in enumerate(values) if i in varchar_indices]
# Check output
for i, char in enumerate(values_as_varchar):
    print(i, char)


# 2. need to clean the anticipated SQL date type elements. GOOD!
values_as_date = ["".join(["TO_DATE('", val, "', ", "'mm/dd/yyyy')"]) for i, val in enumerate(values) if i in date_indices]
for i, date in enumerate(values_as_date):
    print(i, date)




# 3. need to update the values list with cleaned varchar, date type vals
values_copy = list(values)
values_as_varchar_copy = list(values_as_varchar)

# VARCHAR list comprehension
# if index of original values list  was ID'd as needing VARCHAR format for SQL,
# then pop off from formatted list and update corresponding elements in original list.
values_copy = [values_as_varchar_copy.pop(0) if i in varchar_indices 
               else values_copy[i] 
               for i in range(len(values_copy))]

# DATE type list comprehension
values_as_date_copy = list(values_as_date)
values_copy = [values_as_date_copy.pop(0) if i in date_indices 
               else values_copy[i] 
               for i in range(len(values_copy))]



# 4. join the value with the header as query string. GOOD!
# zip iterates over multiple objects in parallel. 
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