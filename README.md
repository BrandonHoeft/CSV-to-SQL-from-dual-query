# Programming flat file rows into a SQL ... SELECT FROM DUAL ... query

## Problem Definition

[**DUAL** is a table automatically created by Oracle Database. Selecting from a DUAL
table is useful for computing a constant expression with the SELECT statement.](https://en.wikipedia.org/wiki/DUAL_table)

My constraint is having no write access to an Oracle corporate database (plsql)
for which I have partially complete data from a SQL query. The other relevant data exists currently
in a flat file (.CSV). I need to UNION these 2 sources of data into one dataset.
To do this my goal is a programmatic approach where I can convert each row of
the flat file into a Oracle compliant SQL query string which can then be inserted
into my SQL query without any manual labor other than a copy and paste.

## Project goal

So the goal of this project is to be able to write a program that:

* Reads a flat file row by row
* converts the row values from the flat file into a valid **SELECT … FROM DUAL** SQL statement
* The N rows from the flat file are converted and written to a .txt file as
  N unioned SQL queries FROM DUAL table.
* The contents of the .txt file can then be added into a valid SQL statement
  for unioning these data with a similarly formatted query from a database.

## Sample Solution Data

A sample .CSV is included in this repo from [Kaggle Datasets](https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017)
of the results from all international football matches from 1872 to 2018. The
dataset was subsampled to contain matches from 1998 through June 20, 2018.

The sample dataset can be used to demonstrate the use of the main function
**convert_to_sql**. The translated output, stored in **translated_output.txt**,
can be copied and pasted into a query front-end to generate a temporary table of
data in lieu of being able to write data or create tables in your SQL environment.

*Note in the final output, the final UNION ALL needs to manually be chopped off.*
