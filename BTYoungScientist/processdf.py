import pandas as pd
import csv

with open("ExampleDiabetesCalc.txt") as sensitive_data:
    lines = sensitive_data.readlines()
    alllines = []
    for i in lines:
        alllines.append(i)
    attribscount = len(alllines[0].split(',')) #14 attributes
    #split attributes up as columns
    
    attributes = []
    for i in range(0, attribscount):
        attributes.append(str(i))
        
    add = []
    for i in range(0, len(alllines)):
        add.append(alllines[i].split(','))
     
    pddf = pd.DataFrame(add)



print(pddf)


