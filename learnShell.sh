#!/bin/sh

#NAME="De Woo"
#echo "Hello,$NAME"
#echo $0

echo "File Name: $0"
echo "First Parameter : $1"
echo "First Parameter : $2"
echo "Quoted Values: $@"
echo "Quoted Values: $*"
echo "Total Number of Parameters : $#"

#for TOKEN in $*
#do	
#	echo $TOKEN	
#done

ARRAY[0]="Zara"
ARRAY[1]="Qadir"
ARRAY[2]="Mahnaz"
ARRAY[3]="Ayan"
ARRAY[4]="Daisy"
#echo "First Index:${ARRAY[0]}"
#echo "Second Index:${ARRAY[1]}"
#echo "All array is ${ARRAY[*]}"


#val=`expr 2 + 2`
a=10
b=8
c=`expr $a + $b`
d=[$a==$b]
e=`[-z$a]`
echo $e
