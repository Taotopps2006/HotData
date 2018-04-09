import csv
import numpy as np
#this file sets up the data before machine learning takes place
#part a first counts the number of read/write requests on each FileObject
#part b ranks each file as hot or cold based on relation to 80th percentile
#part c appends the file with this information to be ready for machine learning

with open("sampledata/trace.csv", "r") as f:
    #part a

    reader = csv.reader(f)
    row = ['']
    while row != ['EndHeader']:
        row = reader.next()
    #row now points at EndHeader, will be at first element after 1 next

    #dictionary of all the file objects, key is the FileObject identifier, value is the count
    objTable = dict()

    #this loop counts the number of total requests associated with a file object
    #note: i manuaLly appended "end" as the last line of the file for the loop
    #the requests counted only include 'FileIoRead' and 'FileIoWrite'
    while row != ['end']:
        row = reader.next()
        if row[0] == "             FileIoRead" or row[0] == "            FileIoWrite": #the 0th index in the list is the request type
            fileObj = row[6] #the 6th index in the list is the file object
            if fileObj in objTable:
                objTable[fileObj] += 1;
            else:
                objTable[fileObj] = 1;

    #objTable is now filled with all data needed

    #part b
    #list of all the request values counted in the dictionary
    reqList = []
    for key in objTable:
        reqList.append(objTable[key])
    #reqList is a list of integers from the lowest request count to highest request count
    reqList.sort()
    npreqList = np.array(reqList)
    pcnt = np.percentile(npreqList, 80)
    #pcnt is the 80th percentile, numbers below this are cold and above are hot

    for key in objTable:
        if objTable[key] <= pcnt:
            objTable[key] = "cold"
        else:
            objTable[key] = "hot"
    #now objTable describes each file object as cold or hot

    #data in case needed later
    '''
    print(pcnt) #this prints the number of requests that defines hot/cold
    print(len(objTable)) #this prints the number of file objects being worked on
    totalReqs = 0
    for i in reqList:
        totalReqs += i
    print(totalReqs)
    print(objTable) #this prints each file object and if it is hot/cold
    '''

    #part c
with open("sampledata/trace.csv", "r") as f:
    with open("sampledata/traceApp.csv", "w") as g:
        reader = csv.reader(f)
        writer = csv.writer(g)
        #creates a new file called TraceApp.csv, except it appends 'hot' or 'cold' to each read or write request
        for row in reader:
            if row[0] == "             FileIoRead" or row[0] == "            FileIoWrite": #the 0th index in the list is the request type
                if row[6] != "         FileObject":
                    rowAppend = row
                    rowAppend.append(objTable[row[6]])
                    writer.writerow(row)
                else:
                    writer.writerow(row)
            else:
                writer.writerow(row)
