#!/bin/bash

INTERVAL=0.5 #Interval of Capture Screen(seconds)
read folder
DIRNAME="${HOME}/Desktop/capture/${folder}/"
tmp1=0
tmp2=`echo 0`

if [ ! -e ${DIRNAME} ]
then
    mkdir ${DIRNAME}
fi

while true
do 
    DATE=`date +%H%M%S`
    FILENAME0="${DIRNAME}${DATE}_${tmp2}.png"
    screencapture ${FILENAME0}
    echo "capture at ${DATE}_${tmp2}"
    tmp2=$((${tmp1} + 1))
    tmp2=$((${tmp2} % 2))
    tmp1=${tmp2}
    tmp2=`echo ${tmp2}`
    sleep $INTERVAL
done
