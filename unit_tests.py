import os
current_path = os.getcwd()
print('Current working directory: {}'.format(current_path))
os.chdir("{}/Desktop/CSV-to-SQL-from-dual-query".format(current_path))


from csv_to_sql import string_to_sql_varchar, string_to_sql_date, convert_to_sql

# Testing string_to_varchar output
strings_list = ['dog', 'cat', 0, 5, '12/10/2017', '1/6/2006']

str_formatted = string_to_sql_varchar(strings_list, [0,1])
print(str_formatted)

# Testing sql_string_to_date output
dates_formatted = string_to_sql_date(str_formatted, [4,5], 'mm/dd/yyyy')
print(dates_formatted)



# Testing if convert_to_sql() works
read_in = '/Users/bhoeft/Desktop/CSV-to-SQL-from-dual-query/test_data.csv'
write_to = '/Users/bhoeft/Desktop/CSV-to-SQL-from-dual-query/translated_output.txt'
varchars = [1, 2, 5, 6, 7, 8]
dates = [0]

convert_to_sql(read_in, write_to, varchars, dates, 'yyyy-mm-dd')






#!/usr/bin/env python3
# -*- coding: utf-8 -*-


