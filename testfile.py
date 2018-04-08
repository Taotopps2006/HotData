import csv

with open("sampledata/trace.csv", "r") as f:
    reader = csv.reader(f)
    row = ['']
    while row != ['EndHeader']:
        row = reader.next()
    #row now points at EndHeader, will be at first element after 1 next
    #while True:
    row = reader.next()
    print(row[0])
    print('hello')
