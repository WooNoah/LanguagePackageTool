#!/bin/bash
# 复制.txt文件内容到.md文件内容中,并在每一行最后添加”;“

#echo "please enter the number of insert line:"
#read numberLine


#A=$(ls *.txt)
##x=`sed 's//&;/g' 1.txt`
#for name in $A
#do
#	x=`sed -e 's/\(.*\)"\(.*\)/\1";\2/g' ${A}`
#	filename=${name%.md}
#	#echo ${filename} > TXT_de.md
#	echo ${x} > $filename
#done

#content=`sed -e 's/$/;/g' 1.txt`
content=`sed -e 's/\(.*\)"\(.*\)/\1";\2/g' 1.txt`
echo ${content} > TXT_de.md
#c=`sed -e 's/^[ ]*//g' TXT_de.md`
#echo ${c} > TXT_de.md

A=$(ls *.txt)
for name in $A
do
    content=`sed -e 's/\(.*\)"\(.*\)/\1";\2/g' ${name}`
    prefix=${name%.txt*}
    suffix='.md'
    new_filename=${prefix}${suffix}
    echo ${content} > ${new_filename}
#    echo ${content} > TXT_de.md

done
