read_path = '/Users/bhoeft/Desktop/temp/fake_simulated_data.csv'
out_path = '/Users/bhoeft/Desktop/temp/output.txt'

# Explore: captures headers row as a list, then prints each row line by line. 
with open(read_path) as file:
    
    for i, line in enumerate(file): # file is an iterable.
        if i == 0:
            headers = line.rstrip('\n').split(',')
        else:
            print(i, line)
    
    print(headers)
            

    





# Template structure for reading line by line and writing line by line.
with open(read_path) as file:
    with open(out_path, 'a') as file_out: 
        for line in file:
            print(line)















#!/usr/bin/env python3
# -*- coding: utf-8 -*-