read_path = '/Users/bhoeft/Desktop/CSV-to-SQL-from-dual-query/fake_simulated_data.csv'
out_path = '/Users/bhoeft/Desktop/CSV-to-SQL-from-dual-query/output.txt'

##############################################################################
# specific cleaning functions.
##############################################################################

def string_to_sql_varchar(list_obj, list_varchar_indices):
    """takes a list of strings, and passes another list of indices representing 
    the elements in that list of strings that you want formatted as SQL VARCHAR 
    elements. This is achieved  by wrapping single quotes around the existing 
    string value for PLSQL compliance. 
    """
    values_as_varchar = ["".join(["'", val, "'"]) for i, val in enumerate(list_obj) 
                        if i in list_varchar_indices]
    
    for i in range(len(list_obj)):
        if i in list_varchar_indices:
            list_obj[i] = values_as_varchar.pop(0)
    
    return list_obj


def string_to_sql_date(list_obj, list_date_indices):
    """takes a list of strings, and pass another list of indices representing 
    the elements that you want transformed to a date from a string to a PLSQL 
    compliant TO_DATE string to date format.
    """
    
    values_as_date = ["".join(["TO_DATE('", val, "', ", "'mm/dd/yyyy')"])
                     for i, val in enumerate(list_obj) 
                     if i in list_date_indices]
    
    for i in range(len(list_obj)):
        if i in list_date_indices:
            list_obj[i] = values_as_date.pop(0)
    
    return list_obj


###############################################################################
# Development of CSV to SQL FROM dual temp table .txt file output.  
###############################################################################


with open(read_path) as infile:
    with open(out_path, 'a') as outfile:

        varchar_indices = (0,1,2,3,6,9,10,12) 
        date_indices = (13,14,15)
        
        # file is an iterable. can loop over indices and rows
        for i, line in enumerate(infile): 

            if i == 0:
                # clean header values and unpack into list.
                headers = line.rstrip('\n').lower().split(',')
            elif i == 1:
                # clean, unpack line into list of strings, splitting on delimiter
                values = line.rstrip('\n').split(',')
                # clean, format desired SQL VARCHAR elements
                values = string_to_sql_varchar(values, varchar_indices)
                # clean, format the SQL DATE elements to convert string to date in SQL.
                values = string_to_sql_date(values, date_indices)
                # join each cleaned val with corresponding SQL field header
                sql_select_list = [val + ' AS ' + header for val, header in zip(values, headers)]
                # write initial FROM dual query. has headers.
                outfile.write('SELECT ' + ', '.join(sql_select_list) + ' FROM DUAL UNION ALL \n')

            elif i > 1:
                # repeat above except but no need for HEADERS like initial query.  
                values = line.rstrip('\n').split(',')
                values = string_to_sql_varchar(values, varchar_indices)
                values = string_to_sql_date(values, date_indices)
                outfile.write('SELECT ' + ', '.join(values) + ' FROM DUAL UNION ALL \n')

            else:
                print('something unexpected happened. Investigate!')
            
            print('completed row ', i)




##############################################################################
# miscellaneous.
##############################################################################
headers
values
for i, val in enumerate(values):
    print(i, val)
values[0]





#!/usr/bin/env python3
# -*- coding: utf-8 -*-