"""
@author: MortezaYosefy
Using Spyder (Python 3.8)
"""
import json

# json file and this file should be located at the same directory.
# Otherwise, you need to give the exact location of json file.
fileObj = open("problem1.json", "r")

# To read this json file in python, first open the file in read mode,
# and then parse it using json.loads() function.
jsonContent = fileObj.read()
aList = json.loads(jsonContent)

# Here we'll have two nested for loop to discover the empty strings
for m in aList:
    
    for key,value in m.items():
        # Empty strings "" are going to be replaced with None.
        if value == "":
            m[key] = None

# The json.dumps() takes a list as an argument and returns the JSON data type.                
newJsonContent = json.dumps(aList)