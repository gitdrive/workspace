#!/usr/bin/python
import csv,math,sys
LIST=[]
train=[]
rowIndex=[]
up_down=[]
count=0
i=0
n=0
k=0
last_peak=0
total = len(sys.argv)
if (total!=4):
	print "Please Enter three arguments....!"
	exit()
inpfile=sys.argv[1]
outfileUp=sys.argv[2]
outfileDown=sys.argv[3]

#outfile='Peak.csv'
outfUp=open(outfileUp,'wb')
outfDown=open(outfileDown,'wb')
lines = csv.reader(open(inpfile,'rb'), delimiter='\t')
outlineUp=csv.writer(outfUp)
outlineDown=csv.writer(outfDown)
for row in lines:
    if row:
            if((row[2]=="Stopped_Western")):
                if(int(row[0])>int(9800)):
                        n+=1
                        LIST.append(row)
                        #print row[0],row[1],row[2],row[3],row[4]


for i, val in enumerate(LIST):
        if(val[1] not in rowIndex):
                rowIndex.append(val[1])
                train.append(i)
                #print i,val[1]
        
                

for i, val in enumerate(LIST):
        if(i in train):
                up_down.append(val)
for i, val in enumerate(up_down):
        if(val[5]=="up"):
                outlineUp.writerow(val)
        else:
                outlineDown.writerow(val)
        print val[5]


#   outline.writerow(val)    
            
