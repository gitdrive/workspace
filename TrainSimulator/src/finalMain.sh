#!/bin/bash
numUsr=$1
maxNumUsr=$2
rm Avg.csv
rm Avg1.csv
rm allUsr.csv
rm allUsr1.csv
echo NumUsr,AvgError,SD>allUsr.csv
echo NumUsr,AvgError,SD>allUsr1.csv
while [  $numUsr -lt $maxNumUsr ]; do
         
SpotTime=864000
end_sim_time=2592000
         while [  $SpotTime -lt $end_sim_time ]; do
echo -e "\n"
echo "num user="$numUsr
echo "Spot Time="$SpotTime
echo -e "\n"

             bash main.sh $end_sim_time $SpotTime $numUsr
	     python CalAvg.py $4 Avg.csv	
	     python CalAvg.py $5 Avg1.csv
	     let SpotTime=SpotTime+864000
         done

python avg.py Avg.csv $numUsr allUsr.csv
python avg.py Avg1.csv $numUsr allUsr1.csv
rm Avg.csv
rm Avg1.csv
   
     let numUsr=numUsr+$3
     
done
python error_bar.py $4 allUsr.csv allUsrGraphEst.pdf </dev/null>/dev/null 2>&1
python error_bar.py $5 allUsr1.csv allUsrGraphTru.pdf </dev/null>/dev/null 2>&1
