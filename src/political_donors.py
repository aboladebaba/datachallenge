#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 00:34:13 2017

@author: abolade
"""

import sys
import pandas as pd

filename = sys.argv[1]
ofile1 = sys.argv[2]
ofile2 = sys.argv[3]


clpos = [0, 10, 13, 14, 15]
clnames = ['CMTE_ID', 'ZIP_CODE', 'TRANSACTION_DT', 'TRANSACTION_AMT', \
           'OTHER_ID']

# Load the filename into a pandas DataFrame
data = pd.read_csv(filename, sep='|', usecols=clpos, names=clnames, \
                   parse_dates=[2], dtype={'ZIP_CODE': str})

# exclude rows with non-null value in column 'OTHER_ID'
data = data[data['OTHER_ID'].isnull()]

# Exclude rows with null values in 'CMTE_ID' or 'TRANSACTION_AMT' columns
data = data.dropna(subset=['CMTE_ID', 'TRANSACTION_AMT'])

# Trim the ZIP_CODE column to remain 5 characters
data['ZIP_CODE'] = data['ZIP_CODE'].str[:5]

# filter ZIP_CODE for len of 5 and not null
filtered = ( data['ZIP_CODE'].str.len()== 5) & (data['ZIP_CODE'].notnull())

d = {}
fl = open(ofile1, 'w')
for index, row in data[filtered].iterrows():
    lst = [row['CMTE_ID'], str(row['ZIP_CODE']), str(row['TRANSACTION_AMT'])]
    k = row['CMTE_ID'] + '_' + str(row['ZIP_CODE'])
    cnt = 1
    if k in d.keys():
        cnt += 1
    lst.append(str(cnt))
    d[k] = d.get(k, 0) + row['TRANSACTION_AMT']
    lst.append(str(d[k]))
    lst = '|'.join(lst)
    fl.write(lst + '\n')

fl.close()

# creating the second file

data2 = data[['CMTE_ID', 'TRANSACTION_DT', 'TRANSACTION_AMT']]
grp = data2['TRANSACTION_AMT'].groupby([data2['CMTE_ID'], data2['TRANSACTION_DT']])
cnt = pd.DataFrame(grp.agg('count'))
med = pd.DataFrame(round(grp.agg('median')))
sm = pd.DataFrame(grp.agg('sum'))
results = pd.merge(pd.merge(cnt, med, how='inner', left_index=True, \
        right_index=True), sm, how='inner', left_index=True, right_index=True)
results['TRANSACTION_AMT_y'] = results['TRANSACTION_AMT_y'].astype(int)
results.to_csv(ofile2, sep='|', header=None, columns=None, index=True, \
               index_label=None, mode='w', line_terminator='\n')



