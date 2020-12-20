import pandas as pd
import numpy as np
import csv

def calculate(filename):
    
    with open("filename") as sensitive_data:
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

        for i in range(0,len(pddf[0])):
            pddf[0][i] = float(pddf[0][i])
            
        for i in range(0,len(pddf[1])):
            pddf[1][i] = float(pddf[1][i])

        for i in range(0,len(pddf[5])):
            pddf[5][i] = float(pddf[5][i])

        for i in range(0,len(pddf[7])):
            pddf[7][i] = float(pddf[7][i])

        print(pddf)

    def treeclassdiabetes(DATA):

        df = DATA
        points = []
         
        p = 0
           
        r1 = df[0]
        r2 = df[1]
        r3 = df[2]
        r4 = df[3]
        r5 = df[4]
        r6 = df[5]
        r7 = df[6]
        r8 = df[7]
        
        if r1 > 140:
            p += 1
        else:
            p += 0

        if r2 > 90:
            p += 1
        else:
            p += 0

        if r3 == 'Male':
            p += 1
        else:
            p += 0
             
        if r4 == 'Yes':
            p += 1
        else:
            p += 0
               
        if r5 == 'No':
            p += 1
        else:
            p += 0
               
        if r6 < 40:
            p += 0
        elif r6 > 40 < 50:
            p += 1

        elif r6 > 50 < 60:
            p += 2
        else:
            p += 3

        if r7 == 'Yes':
            p += 1
        else:
            p += 0
               
        if r8 < 25:
            p += 0
            points.append(p)
        elif r8 > 25 < 30:
            p += 1
            points.append(p)
        elif r8 > 30 < 40:
            p += 2
            points.append(p)
        else:
            p += 3
            points.append(p)
                
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None

        print('Chance for diabetes:',((points[0]/12)*100))

    for row in range(0,pddf.shape[0]):
        inprow = pddf.loc[row].values.tolist()
        treeclassdiabetes(inprow)
        


