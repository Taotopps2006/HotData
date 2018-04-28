import csv
import numpy as np
import math
import binascii

#This file creates a csv from traceApp that includes only the
#   FileIo requests that we're concerned with

#Other formatting changes are made to make data compatible with tensorflow's data types
# In particular everything is integerized

#Note: Python 3 syntax used


#Characters to strip from some of the data fields (columns)
chars_to_strip = dict.fromkeys(map(ord, 'p ()|Disk\/":\n\rxabcdef'), None)



with open("sampledata/traceApp.csv", "r") as f:
    with open("sampledata/dataFull.csv", "w", newline = '') as g:
        #part a

        reader = csv.reader(f)
        writer = csv.writer(g)
        row = ['']
        while row != ['EndHeader']:
            row = next(reader)

        #This loop looks through traceApp.csv row by row and writes those
        # rows corresponding to a file io request to trainingSet.csv
        while row != ['end']:
            row = next(reader)
            if row[0] == "             FileIoRead" or row[0] == "            FileIoWrite": #the 0th index in the list is the request type

                if "Read" in row[0]:    #Read requests are given value 0, write requests given 1
                    row[0] = 0
                else:
                    row[0] = 1
                row[1] = int(row[1])
                row[2] = int(row[2].translate(chars_to_strip))  #Characters stripped to leave integer corresponding to value
                row[3] = int(row[3])
                row[4] = int(row[4])
                row[5] = int(row[5].translate(chars_to_strip))
                row[6] = int(row[6].translate(chars_to_strip))
                row[7] = int(row[7].translate(chars_to_strip))
                #######################################################
                #These columns, consisting of mixed strings and hexadecimal, are ommitted
                row[8] = 0
                row[9] = 0
               #########################################################
                
                if "Normal" in row[10]: #Normal priority is given value 0, NotSet is given value 1
                    row[10] = 0
                else:
                    row[10] = 1
                    
                #######################################################
                #This data is ommitted
                    
                #row[11] = int(row[11].translate(chars_to_strip))
                row[11] = 0
                #######################################################

                if len(row[12]) > 1:
                    row[12] = int(row[12].translate(chars_to_strip)) #strip characters to leave integer representing value
                else:
                    row[12] = 0   #blank entries are given value 0
                    
                if "hot" in row[13]:   #For labeling purposes, 'hot' requests are given value 0, 'cold' given value 1
                    row[13] = 0
                else:
                    row[13] = 1
                writer.writerow(row)
