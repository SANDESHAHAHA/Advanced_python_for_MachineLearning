# 4. Write a generator to read a CSV file line by line.

import csv
def readFile(file):
    with open(file,mode="r") as f:
        content=csv.reader(f)
        for item in content:
            yield(item)
        
result =readFile("new.csv")
for row in result:
    print(row)