#!/usr/bin/python
import csv,math,sys
LISTEst=[]
LISTtru=[]
finalDist=0
linesTru=[]
min=0
total = len(sys.argv)
if (total!=9):
	print "Please Enter eight arguments....!"
	exit()
inpfileEst=sys.argv[1]
inpfileTru=sys.argv[2]
outfileEst=sys.argv[3]
outfileTru=sys.argv[4]
flagUp=sys.argv[5]
SpotTime=sys.argv[6]
totoal_path_length=sys.argv[7]
UP_DOWNswap_file=sys.argv[8]

outfEst=open(outfileEst,'wb')
outfTru=open(outfileTru,'wb')
outlineEst=csv.writer(outfEst)
outlineTru=csv.writer(outfTru)

#calculating for each estimated value
listTemp=[]
#listTemp.append("Positions , NearestTruthDis, PosConf")
#outlineEst.writerow(listTemp)
##Swaping_start
if(int(flagUp)==1):
        linestru = csv.reader(open(inpfileTru,'rb'), delimiter=',')
        for row in linestru:
                originDist=row[4]
                timeExceed=int(SpotTime)-float(row[0])
                distExceed=timeExceed*14 #speed of train is 14 m/s
                
                finalDist=float(row[4])+distExceed
                if(float(finalDist)<=float(totoal_path_length)):
                        linesTru.append(row)
               
              
        linestru_swap = csv.reader(open(UP_DOWNswap_file,'rb'), delimiter=',')

        for row in linestru_swap:
                originDist=row[4]
                timeExceed=int(SpotTime)-float(row[0])
                distExceed=timeExceed*14 #speed of train is 14 m/s
                
                finalDist=float(row[4])-distExceed
                if(float(finalDist)<=0):
                        linesTru.append(row)
else:

        linestru = csv.reader(open(inpfileTru,'rb'), delimiter=',')
        for row in linestru:
                originDist=row[4]
                timeExceed=int(SpotTime)-float(row[0])
                distExceed=timeExceed*14 #speed of train is 14 m/s
                
                finalDist=float(row[4])-distExceed
                if(float(finalDist)>0):
                        linesTru.append(row)

               
              
        linestru_swap = csv.reader(open(UP_DOWNswap_file,'rb'), delimiter=',')

        for row in linestru_swap:
                originDist=row[4]
                timeExceed=int(SpotTime)-float(row[0])
                distExceed=timeExceed*14 #speed of train is 14 m/s
                
                finalDist=float(row[4])+distExceed
                if(float(finalDist)>float(totoal_path_length)):
                        linesTru.append(row)
               

##Swapping_end



linesEst = csv.reader(open(inpfileEst,'rb'), delimiter=',')

for row1 in linesEst:
    min=1000000
    listTemp=[]
    #linesTru = csv.reader(open(inpfileTru,'rb'), delimiter=',')
    for row2 in linesTru:
        originDist=row2[4]
        timeExceed=int(SpotTime)-float(row2[0])
        distExceed=timeExceed*14 #speed of train is 14 m/s
        if(int(flagUp)==1):
                finalDist=float(row2[4])+distExceed
                #print finalDist
                #print totoal_path_length
                if(float(finalDist)>float(totoal_path_length)):
                        finalDist=float(totoal_path_length)-finalDist+float(totoal_path_length)
               
               
        else:
                finalDist=float(row2[4])-distExceed
                if(float(finalDist)<0):
                        finalDist=0-finalDist
                if(float(finalDist)==0):
                        finalDist=finalDist

        #print finalDist
        #print abs(float(row1[0])-float(row2[4]))
        if(min>abs(float(row1[0])-float(finalDist))):
            min=abs(float(row1[0])-float(finalDist))
    listTemp.append(row1[0])
    listTemp.append(min)
    listTemp.append(row1[1])
    #print min
    LISTEst.append(listTemp)
for i, val in enumerate(LISTEst):
    outlineEst.writerow(val)

#calculating avg and max Positional Confidence

linesEst = csv.reader(open(inpfileEst,'rb'), delimiter=',')
maxPosConf=0
avgPosConf=0
s=0
i=0
for row in linesEst:
    s=s+float(row[1])
    i=i+1
    if(maxPosConf<row[1]):
        maxPosConf=row[1]
if(i==0):
        avgPosConf=0
else:
        avgPosConf=s/i
#print avgPosConf,maxPosConf

s1="AvgPosConf, "+str(avgPosConf)+","
s2="MaxPosConf,"+str(maxPosConf)+","
listTemp=[]
listTemp.append(s1)
#outlineEst.writerow(listTemp)
listTemp=[]
listTemp.append(s2)
#outlineEst.writerow(listTemp)


listTemp=[]
listTemp.append("Positions , NearestEstDis")
outlineTru.writerow(listTemp)

#calculating for each ground truth value
#linesTru = csv.reader(open(inpfileTru,'rb'), delimiter=',')

for row1 in linesTru:
    min=1000000
    listTemp=[]
    linesEst = csv.reader(open(inpfileEst,'rb'), delimiter=',')
    for row2 in linesEst:
        #print abs(float(row1[0])-float(row2[4]))
        originDist=row1[4]
        timeExceed=int(SpotTime)-float(row1[0])
        #print timeExceed
        distExceed=timeExceed*14 #speed of train is 14 m/s
	
        if(int(flagUp)==1):
                finalDist=float(row1[4])+distExceed
                if(float(finalDist)>float(totoal_path_length)):
                        finalDist=float(totoal_path_length)-finalDist+float(totoal_path_length)
               
                        #print "hello"
                #print flagUp
        else:
                finalDist=float(row1[4])-distExceed
		#print finalDist
                if(float(finalDist)<0):
                        finalDist=0-finalDist
                if(float(finalDist)==0):
                        finalDist=finalDist
                
        
        if(min>abs(float(finalDist)-float(row2[0]))):
            min=abs(float(finalDist)-float(row2[0]))
            #print finalDist
    listTemp.append(finalDist)
    listTemp.append(min)
    LISTtru.append(listTemp)
LISTtru.sort(key=lambda x:float(x[0]))
#print LISTtru
for i, val in enumerate(LISTtru):
    outlineTru.writerow(val)

