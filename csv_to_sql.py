

##############################################################################
# specific cleaning functions.
##############################################################################

def string_to_sql_varchar(list_obj, list_varchar_indices):
    """takes a list of strings, and passes another list of indices 
    representing the elements in that list of strings that you want formatted 
    as SQL VARCHAR elements. This is achieved  by wrapping single quotes around
    the existing string value for PLSQL compliance. 
    """
    values_as_varchar = ["".join(["'", val, "'"]) for i, val in enumerate(list_obj) 
                        if i in list_varchar_indices]
    
    for i in range(len(list_obj)):
        if i in list_varchar_indices:
            list_obj[i] = values_as_varchar.pop(0)
    
    return list_obj


def string_to_sql_date(list_obj, list_date_indices, date_as):
    """takes a list of strings, and pass another list of indices r
    representing the elements that you want transformed to a date from a string 
    to a PLSQL compliant TO_DATE string to date format.
    """
    
    values_as_date = ["".join(["TO_DATE('", val, "', ", "'{}')".format(date_as)])
                     for i, val in enumerate(list_obj) 
                     if i in list_date_indices]
    
    for i in range(len(list_obj)):
        if i in list_date_indices:
            list_obj[i] = values_as_date.pop(0)
    
    return list_obj



###############################################################################
# Main function  
###############################################################################

def convert_to_sql(read_path, out_path, varchar_indices, date_indices,
                   date_format):
    """
    From the filepath to a .CSV (read_path), reads one row at a time, 
    cleans/transforms the row into a PLSQL SELECT FROM dual UNION ALL stmt, 
    then writes (appends) the transformed row to out_path. 
        
    PARAMETER DEFINITIONS:
    read_path: path ending in .CSV file name you want to read lines from.
    
    out_path: new path and .txt file you want translated output stored in. 
    
    Func expects a list of 0 based varchar_indices representing columns in the 
    .CSV that need to be transformed by wrapping them in single-quotes.
    
    Func expects a list of 0 based date_indices representing columns in the 
    .CSV that need to be translated into a TO_DATE SQL SELECT statement format.
    
    A single quoted date_format should be passed to specify  SQL SELECT 
    statement date format based on how dates are stored in the .CSV.    
    
    IMPORTANT NOTE: 
    The last output row will have UNION ALL appended to it. This should be 
    manually deleted after copy/paste into SQL engine since it is not unioning 
    to any other rows or subqueries. 
    
    EXAMPLE:
    >>> input = '/Users/bhoeft/Desktop/data.csv'
    >>> output = ''/Users/bhoeft/Desktop/final_output.txt'
    >>> varchar_locs = [0,1,2,3,6,9,10,12]
    >>> date_locs = [13,14,15]
    >>> convert_to_sql(input, output, varchar_locs, date_locs, 'yyyy-mm-dd')
    
    Complete: read, translated, and wrote row 1
    Complete: read, translated, and wrote row 2
    ...
    Complete: read, translated, and wrote row 1000
    >>>
    """
    
    with open(read_path) as infile:
        with open(out_path, 'a') as outfile:
    
            
            # iterates over infile object, assigning each line to a var 
            # called line. using enumerate enables iteration over indices too. 
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
                    values = string_to_sql_date(values, date_indices, date_format)
                    # join each cleaned val with corresponding SQL field header
                    sql_select_list = [val + ' AS ' + header 
                                       for val, header in zip(values, headers)]
                    # write initial FROM dual query. has headers.
                    outfile.write('SELECT ' + 
                                  ', '.join(sql_select_list) + 
                                  ' FROM DUAL UNION ALL \n')
    
                elif i > 1:
                    # repeat above except but no need for HEADERS like initial query.  
                    values = line.rstrip('\n').split(',')
                    values = string_to_sql_varchar(values, varchar_indices)
                    values = string_to_sql_date(values, date_indices, date_format)
                    outfile.write('SELECT ' + 
                                  ', '.join(values) + 
                                  ' FROM DUAL UNION ALL \n')
    
                else:
                    print('something unexpected happened. Investigate!')
                
                print('Complete: read, translated, and wrote row {}'.format(i))




#!/usr/bin/env python3
# -*- coding: utf-8 -*-