#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import csv, sys, re, random, os, time
font = {'family' : 'normal',
        
        'size'   : 10}

plt.rc('font', **font)
datfile="repuTrue.csv"
Mcsv = csv.reader(open(datfile, 'rb'), delimiter=',', quotechar='"')

# Mapping from column name to column index
I = {}

# Matrix of all the rows
M = []

rowNum = 0
for row in Mcsv:
    rowNum += 1
    if (rowNum == 1):
        for i in range(len(row)):
            I[row[i]] = i
        continue
    else:
        M.append(row)

simtime = map(lambda r: float(r[I['SimTime']]), M)
repu = map(lambda r:float( r[I['reputation']]), M)



ind = np.arange(len(simtime))
width = 0.20
plt.plot(simtime,repu, label='Avg reputation with time', ls='-', color='blue', marker='+', markersize=1, mew=1, linewidth=1)
#plt.plot(ind+1.5*width, repu, linestyle='_',color='b',marker='*')

plt.axis(ymin=0)
plt.axis(ymax=1)
#plt.axis(xmax=1000000)


plt.xlabel('Time')
plt.ylabel('Reputation of user')
plt.grid(b='on')
#plt.xticks(ind+1.5*width, Usr)
plt.legend(loc=0)
plt.suptitle('Graph for reputation of user with time')
plt.savefig("RepuGraphAvg.pdf", bbox_inches='tight')
#plt.show()
