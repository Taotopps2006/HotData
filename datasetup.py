import csv

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
    while row != ['end']:
        row = reader.next()
        if row[0] == "             FileIoRead" or row[0] == "            FileIoWrite":
            fileObj = row[6] #the 6th in the list is the file object
            if fileObj in objTable:
                objTable[fileObj] += 1;
            else:
                objTable[fileObj] = 1;

    #objTable is now filled with all data needed
    print(objTable)

    #part b
    #list of all the request values counted in the dictionary
    reqList = []
    for key in objTable:
        reqList.append(objTable[key])
    #reqList is a list of integers from the lowest request count to highest request count
    print(reqList)
