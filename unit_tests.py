import os
current_path = os.getcwd()
print('Current working directory: {}'.format(current_path))
os.chdir("{}/Desktop/CSV-to-SQL-from-dual-query".format(current_path))


from csv_to_sql import string_to_sql_varchar, string_to_sql_date

# Testing string_to_varchar output
strings_list = ['dog', 'cat', 0, 5, '12/10/2017', '1/6/2006']

str_formatted = string_to_sql_varchar(strings_list, [0,1])
print(str_formatted)

# Testing sql_string_to_date output
dates_formatted = string_to_sql_date(str_formatted, [4,5])
print(dates_formatted)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-


