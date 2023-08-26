# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:35:45 2019

@author: suresh pokhrel
"""

import csv
import glob
import pandas as pd

Raw_FilePath = 'YourFolderName/*.dat' #put here the full folder path containing the raw (.dat) files of AE33
New_FilePath = 'YourPath/FinalFile.csv'# Put here the file path where you want store the converted csv file

""" 
This below line 19 is the optional one: - If you want to extract only few columns from full columns of the converted csv file 
then uncomment this line 19  and the last 6 lines with the required columns names in the second last line of the this code
"""
#Filtered_FilePath = 'YourPath/FilteredColumnsAE33.csv'



cols = [ ["Date(yyyy/MM/dd)", 
        'Time(hh:mm:ss)', 
        'Timebase',
        'RefCh1',
        'Sen1Ch1',
        'Sen2Ch1',
        'RefCh2',
        'Sen1Ch2',
        'Sen2Ch2',
        'RefCh3',
        'Sen1Ch3',
        'Sen2Ch3',
        'RefCh4',
        'Sen1Ch4',
        'Sen2Ch4',
        'RefCh5',
        'Sen1Ch5',
        'Sen2Ch5',
        'RefCh6',
        'Sen1Ch6',
        'Sen2Ch6',
        'RefCh7',
        'Sen1Ch7',
        'Sen2Ch7',
        'Flow1',
        'Flow2',
        'FlowC',
        'Pressure(Pa)',
        'Temperature(Â°C)',
        'BB (%)',
        'ContTemp',
        'SupplyTemp',
        'Status',
        'ContStatus',
        'DetectStatus',
        'LedStatus',
        'ValveStatus',
        'LedTemp',
        'BC11',
        'BC12',
        'BC1',
        'BC21',
        'BC22',
        'BC2',
        'BC31',
        'BC32',
        'BC3',
        'BC41',
        'BC42',
        'BC4',
        'BC51',
        'BC52',
        'BC5',
        'BC61',
        'BC62',
        'BC6',
        'BC71',
        'BC72',
        'BC7',
        'K1',
        'K2',
        'K3',
        'K4',
        'K5',
        'K6',
        'K7',
        'TapeAdvCount',
        'X1',
        'X2',
        'X3',
        'X4',
        'X5',
        'X6'
        ]
]

# read flash.dat to a list of lists
with open(New_FilePath, "w", newline='') as f:
    writer = csv.writer(f,dialect='excel')
    writer.writerows(cols)
  
AE_files = glob.glob(Raw_FilePath)
for files in AE_files :
    datContent = [i.strip().split() for i in open(files).readlines()]
    
    datContent=datContent[8:]
    
    
    #print(datContent)
    
    # write it as a new CSV file
    with open(New_FilePath, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(datContent)
        
# df = pd.read_csv(New_FilePath)  
# df.rename(columns={'Date(yyyy/MM/dd)': 'Date', 'Time(hh:mm:ss)': 'Time' }, inplace = True)
# df.Date= pd.to_datetime(df.Date)
# df['date_time'] = df.Date.astype(str) + ' ' + df.Time
# df = df[['date_time', 'BC1', 'BC2', 'BC3', 'BC4', 'BC5', 'BC6', 'BC7', 'BB (%)', 'Status']] #put here the names of columns you want to filter in
# df.to_csv(Filtered_FilePath, index=False)
      