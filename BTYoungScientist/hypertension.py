import pandas as pd
import numpy as np
import csv
import sqlite3

def calculate(data):
    
    columns = []
    useful = data[['Age', 'Gender', 'Height','MAP']].copy()
    
    useful = pd.DataFrame(useful)

    for i in range(0,len(useful['Age'])):
        useful['Age'][i] = int(useful['Age'][i])

    for i in range(0,len(useful['Gender'])):
        useful['Gender'][i] = str(useful['Gender'][i])

    for i in range(0,len(useful['Height'])):
        useful['Height'][i] = float(useful['Height'][i])

    for i in range(0,len(useful['MAP'])):
        useful['MAP'][i] = float(useful['MAP'][i])
 
    print(useful)

    def hypertension(DATA):

        df = DATA
        points = []        
        p = 0
                   
        r1 = df['Age']
        r2 = df['Gender']
        r3 = df['Height']
        r4 = df['MAP']

        for i in range(0,len(r1)):
            p=0
            if r1[i] > 60:
                p += 1
            else:
                p += 0

            if r2[i] == 'Male':
                p += 1.5
            else:
                p += 0

            if r3[i] > 170:
                p += 2.5
            else:
                p += 0

            if r4[i] > 120:
                p += 3
                points.append(p)
            elif 120 > r4[i] > 100:
                p += 2
                points.append(p)
            elif 100 > r4[i] > 80:
                p += 1
                points.append(p)
            else:
                p += 0
                points.append(p)
                
        global percentages
        percentages = []
        
        for i in points:
            x = ((i/8))
            percentages.append(x)
            

    hypertension(useful)
    return percentages
