import pandas as pd
import numpy as np
import csv
import sqlite3

def calculate(data):
    
    columns = []
    useful = data[['BPsystolic', 'BPdiastolic', 'Gender','1RelWD','active','Age','hypertension','BMI']].copy()
    
    useful = pd.DataFrame(useful)

    for i in range(0,len(useful['BPsystolic'])):
        useful['BPsystolic'][i] = float(useful['BPsystolic'][i])

    for i in range(0,len(useful['BPdiastolic'])):
        useful['BPdiastolic'][i] = float(useful['BPdiastolic'][i])

    for i in range(0,len(useful['Gender'])):
        useful['Gender'][i] = str(useful['Gender'][i])

    for i in range(0,len(useful['1RelWD'])):
        useful['1RelWD'][i] = str(useful['1RelWD'][i])

    for i in range(0,len(useful['active'])):
        useful['active'][i] = str(useful['active'][i])

    for i in range(0,len(useful['Age'])):
        useful['Age'][i] = float(useful['Age'][i])

    for i in range(0,len(useful['hypertension'])):
        useful['hypertension'][i] = str(useful['hypertension'][i])

    for i in range(0,len(useful['BMI'])):
        useful['BMI'][i] = float(useful['BMI'][i])

    print(useful)

    def diabetes(data):

        df = data

        points = []
             
        p = 0
                   
        r1 = df['BPsystolic']
        r2 = df['BPdiastolic']
        r3 = df['Gender']
        r4 = df['1RelWD']
        r5 = df['active']
        r6 = df['Age']
        r7 = df['hypertension']
        r8 = df['BMI']
        
        for i in range(0,len(r1)):
            p=0
            if r1[i] > 140:
                p += 1
            else:
                p += 0

            if r2[i] > 90:
                p += 1
            else:
                p += 0

            if r3[i] == 'Male':
                p += 1
            else:
                p += 0
                         
            if r4[i] == 'Yes':
                p += 1
            else:
                p += 0
                           
            if r5[i] == 'No':
                p += 1
            else:
                p += 0
                           
            if r6[i] < 40:
                p += 0
            elif r6[i] > 40 < 50:
                p += 1

            elif r6[i] > 50 < 60:
                p += 2
            else:
                p += 3

            if r7[i] == 'Yes':
                p += 1
            else:
                p += 0
                           
            if r8[i] < 25:
                p += 0
                points.append(p)
            elif r8[i] > 25 < 30:
                p += 1
                points.append(p)
            elif r8[i] > 30 < 40:
                p += 2
                points.append(p)
            else:
                p += 3
                points.append(p)
                
        global percentages
        percentages = []
        for i in points:
            x = ((i/12)*100)
            percentages.append(x)
            

    diabetes(useful)
    return percentages
