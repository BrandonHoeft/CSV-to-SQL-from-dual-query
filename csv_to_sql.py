read_path = '/Users/bhoeft/Desktop/temp/fake_simulated_data.csv'
out_path = '/Users/bhoeft/Desktop/temp/output.txt'


###############################################################################
# Development of query output.  
###############################################################################

with open(read_path) as infile:
    
    varchar_indices = (0,1,2,3,6,9,10,12) 
    date_indices = (13,14,15)
    
    # file is an iterable. loop over indices and rows
    for i, line in enumerate(infile): 

        if i == 0:
            headers = line.rstrip('\n').lower().split(',')
        elif i == 1:
            # parsed list of original values from the CSV row.
            values = line.rstrip('\n').split(',')
            # 1. need to format the anticipated SQL varchar elements.
            values_as_varchar = ["".join(["'", val, "'"]) 
                                 for i, val in enumerate(values) 
                                 if i in varchar_indices]
            # 2. need to clean the anticipated SQL date type elements
            values_as_date = ["".join(["TO_DATE('", val, "', ", "'mm/dd/yyyy')"]) 
                              for i, val in enumerate(values) 
                              if i in date_indices]
            # 3. need to update the values list with cleaned varchar, date type vals
            # VARCHAR 
            for i in range(len(values)):
                if i in varchar_indices:
                    values[i] = values_as_varchar.pop(0)
            # DATE type 
            for i in range(len(values)):
                if i in date_indices:
                    values[i] = values_as_date.pop(0)
            # 4. join each val in values with corresponding  header as a query string
            sql_select_list = [val + ' AS ' + header for val, header in zip(values, headers)]
            # 5. format a select statement for initial SQL FROM dual query. NEEDS HEADERS!
# START HERE. 
            print('SELECT' + ',\n'.join(sql_select_list) + '\nFROM DUAL\nUNION ALL\n')
        
        elif i > 1:
            # repeat above except no need for HEADERS when unioning rows.  
            values = line.rstrip('\n').split(',')
            values_as_varchar = ["".join(["'", val, "'"]) 
                                 for i, val in enumerate(values) 
                                 if i in varchar_indices]
            values_as_date = ["".join(["TO_DATE('", val, "', ", "'mm/dd/yyyy')"]) 
                              for i, val in enumerate(values) 
                              if i in date_indices]
            # need to update the values list with cleaned varchar, date type vals
            for i in range(len(values)):
                if i in varchar_indices:
                    values[i] = values_as_varchar.pop(0)

            for i in range(len(values)):
                if i in date_indices:
                    values[i] = values_as_date.pop(0)
            
# START HERE. 
            print('SELECT' + ',\n'.join(values) + '\nFROM DUAL\nUNION ALL\n')
        
        else:
            print('something else happened. Investigate!')
        

##############################################################################
# Testing Code, then moving above.
##############################################################################
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

# VARCHAR
# if index of original values list  was ID'd as needing VARCHAR format for SQL,
# then pop off from formatted list and update corresponding elements in original list.
for i in range(len(values_copy)):
    if i in varchar_indices:
        values_copy[i] = values_as_varchar_copy.pop(0)


# DATE type 
values_as_date_copy = list(values_as_date)

for i in range(len(values_copy)):
    if i in date_indices:
        values_copy[i] = values_as_date_copy.pop(0)


# 4. join the value with the header as query string. GOOD!
# zip iterates over multiple objects in parallel. 
sql_select_list_copy = [val + ' AS ' + header for val, header in zip(values_copy, headers)]

'SELECT' + ', '.join(sql_select_list_copy) + ' FROM DUAL UNION ALL' 
print('SELECT' + ',\n'.join(sql_select_list_copy) + '\nFROM DUAL\nUNION ALL' )








###############################################################################
# Template structure for reading line by line and writing line by line.
###############################################################################

with open(read_path) as infile:
    with open(out_path, 'a') as outfile: 
        for line in infile:
            print(line)






#!/usr/bin/env python3
# -*- coding: utf-8 -*-