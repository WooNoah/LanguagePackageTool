#!/bin/bash
# my first shell script

A=$(ls *.txt)
# STR='hello wrold'
#echo $A 
for name in $A
do 
    filename=${name%.txt}
    #echo $filename
    `touch $filename.md`
done

