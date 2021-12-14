# course: cmps3500
# CLASS Project
# PYTHON IMPLEMENTATION OF A CUSTOM STATISTICS SUMMARY CALCULATOR
# date: 11/14/21
# Student: Matthew Deguia 
# Student: Nathaly Leon
# Student: Mike Cha
# description: Implementation of a statistics summary Calculator

"""
    Program Overview:
    1. Data Loading
    2. Data Cleaning
    3. Statistical Operations
    4. Searching Capability

Dataset:
"DataSet[0]"        Column 1 [0]     Column 2 [1]    Column # [#]
"DataSet[1]"        val      [0]     val      [1]    val      [#]
"DataSet[2]"        val      [0]     val      [1]    val      [#]
"DataSet[3]"        val      [0]     val      [1]    val      [#]
 etc...
"""

import sys
import math

# ==========================================================================
# 1. reading from csv file and storing the whole data set
try:
    with open("InputDataSample.csv") as file:
    #with open("Boston_Lyft_Uber_Data.csv") as file:
        DataSet = file.readlines()

    # - store the whole data set as an array
    DataSet = [elem.strip().split(',') for elem in DataSet]
except:
    print("Something went wrong when reading the file.")


# ==========================================================================
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
    no_empty_val = []
    for row in DataSet:
        if all(row):
            no_empty_val.append(row)
    return no_empty_val

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
    no_missing_val = []
    for row in DataSet:
        if 'NA' not in row:
            no_missing_val.append(row)
    return no_missing_val



# ==========================================================================
# 3. Statistical Operations
columnA = []
columnB = []
count = 0 #Amount in Rows
columnA.sort()
columnB.sort()

# Reads the file
f = open("InputDataSample.csv")
with open("InputDataSample.csv","r") as read:
    i = 0
    for line in read:
        for index, line in enumerate(read):
            count += 1
            word = line.split(",")
            #appends numbers into columnA and columnB
            columnA.append(int(word[0]))
            columnB.append(int(word[1]))
f.close()

def calcMean (column):
    mean = 0 

    for i in column:
        mean = mean + int(i)

    return mean/count

def calcMedian(column):
    median = 0

    copyArray = column

    n = len(copyArray)
    k = n/2
    copyArray.sort()
    
    if k % 2 == 0:
        median = (copyArray[int(k)] + copyArray[int(k+1)]) / 2
        return median
    else:
        return copyArray[int(k)]

def calcMode(column):
    modeArray = {} #Number of most repeated numbers
    finalArray = [] #Has the actual Number Inputs
    
    for i in column:
        modeArray.setdefault(i,0)
        #increments 1 when it sees a repeatable number
        modeArray[i] += 1     
    
    maximum = max(modeArray.values())

    for j, item in modeArray.items():
        if item == maximum:
            finalArray.append(j)
    return max(finalArray)

    
def calcUnique(column):
    unique = []
    solution = []
    counter = 0
    l = len(column)
    index = 0
    for i in range(l): 
        for x in range(i+1,l):
            if column[x] == column[i]:
                index += 1
            else:
                index += 0
        unique.append(index)
        index = 0
    for j in range(l):
        if unique[j] == 0:
            solution.append(column[j])
    return len(solution)



def calcVariance(column):
    variance = 0
    sum = 0

    mean = calcMean(column)

    for j in column:
        calc = j - mean
        calc = calc * calc
        variance = variance + calc
        
    variance = (variance / (count-1))

    return variance


# Divided Variance to find Stdv
#---------------------------------------
def stanDev(column):
    return math.sqrt(calcVariance(column))
#---------------------------------------


# Calculates Percentiles of a Column
#---------------------------------------
def find20(column):
    twenty = int(.2 * (count + 1))
    return column[twenty]

def find40(column):
    fourty = int(.4 * (count + 1))
    return column[fourty]

def find50(column):
    fifty = int(.5 * (count + 1))
    return column[fifty]

def find60(column):
    sixty = int(.6 * (count + 1))
    return column[sixty]

def find80(column):
    eighty = int(.8 * (count + 1))
    return column[eighty]
#---------------------------------------

# ==========================================================================
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

# ==========================================================================
# Switch Statement Menu:
def menu(option):
    # the DataSet array must be global for each case to access it properly
    global DataSet
    match option:
        case 'a':
            DataSet = delCol()
            print("    ***Option executed succussfully...")
            print()
        case 'b':
            DataSet = emptyRow()
            print("    ***Option executed succussfully...")
            print()
        case 'c':
            DataSet = duplicates()
            print("    ***Option executed succussfully...")
            print()
        case 'd':
            DataSet = emptyVal()
            print("    ***Option executed succussfully...")
            print()
        case 'e':
            DataSet = missingVal()
            print("    ***Option executed succussfully...")
            print()
        case 'f':
            print("                                                  ")
            print("                     Calculator                   ")
            print("                     ----------                   ")
            print("Descriptor            Column A                 Column B")
            print("**********            ********                 ********")
            print('Count                ','{:,}'.format(count), "                  "'{:,}'.format(count))
            print('Unique               ','{:,}'.format(calcUnique(columnA)), "                   "'{:,}'.format(calcUnique(columnB))) 
            print('Mean                 ','{:,}'.format(calcMean(columnA)), "            "'{:,}'.format(calcMean(columnB)))
            print('Median               ','{:,}'.format(calcMedian(columnA)), "               "'{:,}'.format(calcMedian(columnB)))
            print('Mode                 ','{:,}'.format(calcMode(columnA)), "                 "'{:,}'.format(calcMode(columnB)))     
            print('SD                   ','{:,}'.format(stanDev(columnA)), "       "'{:,}'.format(stanDev(columnB)))
            print('Variance             ','{:,}'.format(calcVariance(columnA)), "    "'{:,}'.format(calcVariance(columnB)))
            print('Minimum              ','{:,}'.format(min(columnA)), "                      "'{:,}'.format(min(columnB)))
            print('20 Percentile        ','{:,}'.format(find20(columnA)), "                 "'{:,}'.format(find20(columnB)))
            print('40 Percentile        ','{:,}'.format(find40(columnA)), "                 "'{:,}'.format(find40(columnB)))
            print('50 Percentile        ','{:,}'.format(find50(columnA)), "                 "'{:,}'.format(find50(columnB)))
            print('60 Percentile        ','{:,}'.format(find60(columnA)), "                 "'{:,}'.format(find60(columnB)))
            print('80 Percentile        ','{:,}'.format(find80(columnA)), "                 "'{:,}'.format(find80(columnB)))
            print('Maximum              ','{:,}'.format(max(columnA)), "                 "'{:,}'.format(max(columnB)))
            print("                                                  ")
        case 'g':
            matrix = input("Enter 'DataSet' to search thru whole data set, or a specific column to search through: ")
            matrix = str(matrix)
            value = input("Enter a value to search for: ")
            value = str(value)
            Search(value, matrix)
        case 'y':
            print('\n'.join([', '.join(['{:4}'.format(item) for item in row]) for row in DataSet]))
        case 'z':
            print("    -- Thank you for using our calculator! --")
            print()
            sys.exit(1)     # - stop the program here

# Main Function:
# - switch statement that displays menu of all options
def main():
    while True:
        print()
        print("=======================================================================")
        print("    -- CMPS 3500 Class Projct - Statistics Summary Calculator --")
        print()
        print("    Data Cleaning:")
        print("    a. Eliminate columns with non-numerical values") #delCol()
        print("    b. Eliminate empty rows") #emptyRow()
        print("    c. Eliminate duplicate rows") #duplicates()
        print("    d. Eliminate rows with empty values") #emptyVal()
        print("    e. Eliminate rows with missing values") #missingVal()
        print()
        print("    Statisical Operations:")
        print("    f. View all statistical operations")
        print()
        print("    Search Functionality:")
        print("    g. Search for a value in the data set")
        print()
        print("    General:")
        print("    y. View data set")
        print("    z. Exit program")
        print()
        option = input("    Choose an option from the menu above: ")
        print()
        menu(option)

# Calling Main Function:
if __name__ == "__main__":
    main()
    print()


# ==========================================================================




