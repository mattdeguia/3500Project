# course: cmps3500
# CLASS Project
# PYTHON IMPLEMENTATION OF A CUSTOM STATISTICS SUMMARY CALCULATOR
# date: 11/14/21
# Student: Matthew Deguia 
# Student: Nathaly Leon
# Student: ...
# description: Implementation of a statistics summary Calculator

"""
    Program Overview:
    1. Data Loading - Read from csv files
    2. Data Cleaning - Must have these cleaning tasks
       - Remove rows with non-numerical data on any column
       - Remove rows with empty values on any column
       - Remove all rows with empty values on any column
       - Remove all rows with duplicated values
       - Remove all fully empty rows
    3. Functions - All functions must be made ourselves
    4. Searching Capability - Must be able to search any element in any column

Dataset:
"DataSet[0]"        Column 1 [0]     Column 2 [1]    Column # [#]
"DataSet[1]"        val      [0]     val      [1]    val      [#]
"DataSet[2]"        val      [0]     val      [1]    val      [#]
"DataSet[3]"        val      [0]     val      [1]    val      [#]
 etc...

"""

import sys

# ==================================================================
# 1. reading from csv file and storing the whole data set
with open("InputDataSample.csv") as file:
#with open("Boston_Lyft_Uber_Data.csv") as file:
    DataSet = file.readlines()

# - store the whole data set as an array
DataSet = [elem.strip().split(',') for elem in DataSet]

# ==================================================================
# 2. data cleaning functions
# ------------------------------------------------------------------
# eliminating columns with non-numeric values
def delCol():
    num_data = []
    num_data_list = []
    index_list = []
    row_len = rowLen(DataSet)

    while row_len > 0:
        # find the indexes in which there is numeric data
        # check if the value is an int or a float
        if DataSet[1][row_len-1].isdigit() or DataSet[1][row_len-1].replace('.', '', 1).isdigit():
            index_list.append(row_len-1)
        row_len-=1

    for row in DataSet:
        for index,ele in enumerate(row):
            if index in index_list:
                num_data.append(ele)
        num_data_list.append(num_data) # to keep the structure of rows
        num_data = []
    return num_data_list

def rowLen(DataSet):
    for row in DataSet:
        return len(row)

# ------------------------------------------------------------------
# eliminating empty rows
def emptyRow():
    no_empty_row = []
    for x in DataSet:
        if x != emptied():
            no_empty_row.append(x)
    return no_empty_row

def emptied(): # gets an empty row for comparison
    emp_list = []
    for row in DataSet:
        for ele in row:
            emp_list.append('')
        return emp_list

# -----------------------------------------------------------------
# eliminating rows with empty values
def emptyVal():
    for row in DataSet:
        if '' in row:
            DataSet.remove(row)

# ------------------------------------------------------------------
# eliminating duplicate rows
def duplicates():
    no_dup = []
    for row in DataSet:
        if row not in no_dup:
            no_dup.append(row)
    return no_dup

# ------------------------------------------------------------------
# eliminating rows with missing values
def missingVal():
    for row in DataSet:
        if 'NA' in row:
            DataSet.remove(row)

# 3. statistical operations
# finished already:
# - count
# - unique
# - mean
# - median
# - mode
# - min
# - max

# still need:
# - standard deviation
# - variance
# - 20 percentile
# - 40 percentile
# - 50 percentile
# - 60 percentile
# - 80 percentile


# ==================================================================
# 4. search function - search for anything in any or all rows
# - this function should work for any data set, regardless of rows and columns
def Search(value, matrix):
   
    # -------------------------------------------------------------
    # 4A. All data in the matrix is stored as strings
    # - if needed, must convert the given value into a string to compare values correctly
    value = str(value)
    
    # -------------------------------------------------------------
    # 4B. Searching through the whole data set
    if matrix == "DataSet":
        # - variable to keep track of how many times the values is present in the data set
        # - variable to keep track of each row we're in
        value_presence = 0
        row_index = -1
        # - formatting of details
        print ()
        print ("Details:")
        print ("*********************************")

        # - go thru each row
        for row in DataSet:
            # - increment to keep track of each row currently searching in
            row_index += 1
            # - variable to keep track of columns we're searching thru
            # - initialized here because needs to reset for each iteration of the rows
            col_index = -1

            # - go thru each column in each row
            for element in row:
                # - increment to keep track of each column currently searching in
                col_index += 1
                # - if the value is found in the column...
                if value == element:
                    value_presence += 1
                    print (value, "is present in Column", col_index+1, "row", row_index)

        # - formatting of details
        print ("*********************************")
        print ()
        print (value, "is present", value_presence, "times in the data set.")
        print ()

    
    # -------------------------------------------------------------
    # 4C. Searching through a specific column in the data set
    else:
        # - variables to keep track values
        value_presence = 0
        row_index = -1
        col_index = -1

        # - Try block to see if the column the user inputted is actual in data set
        # - if it's not, the if statement compares an index that's out of bounds
        try:
            while (col_index < len(DataSet[0])):
                col_index += 1
                if matrix == DataSet[0][col_index]:
                    break
        except IndexError:
            print ("    Error: '", matrix, "' was not found in data set")
            print ("    Choose what to search through from the list below:")
            print ("    - DataSet")
            for row in DataSet[0]:
                print ("    -", row)
            print ()
            sys.exit(1)     # - stop the program here

        # - if column found, continue...
        # - formatting of details
        print ()
        print ("Details:")
        print ("*********************************")
        # - now go thru each row
        for row in DataSet:
            row_index += 1
            # - go thru each column in each row...
            for element in row:
                # - if the value is found in the column...
                if value == element:
                    value_presence += 1
                    print (value, "is present in Column", col_index+1, "row", row_index)
        # - formatting of details
        print ("*********************************")
        print ()
        print (value, "is present", value_presence, "times in Column:", DataSet[0][col_index])
        print ()


# ==================================================================
# 4. Testing the Search function:

# InputDataSample.csv:
# - 320141, Column A
# - 320141, DataSet

# Boston.csv
# - 40.61, temperatureHigh
# - 40.61, DataSet

DataSet = delCol()
DataSet = emptyRow()
DataSet = duplicates()
missingVal()
emptyVal()

#for i in DataSet:
#    print(i)

matrix = input("Enter 'DataSet' to search thru whole data set, or a specific column to search through: ")
matrix = str(matrix)
value = input("Enter a value to search for: ")
value = str(value)
Search(value, matrix)

# ==================================================================

"""
Tasks:
    1. must be able to pass the dataset as an argument to the file
    2. NA
    3. NA
    4. try and catch block.
       - if the user inputs a column to search thru but the column doesn't exist,
         tell the user that the column inputted was not found, and to input a correct column.
         maybe display all the columns from the csv file using a for loop. tell user to 
         choose one of those column names
       - if the user inputs a value that's not found

Final Thoughts:
    - brute force way, looking thru each index and finding matches
    - did not sort the data before searching
    - but it all works like it should
"""












