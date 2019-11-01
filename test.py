# coding: UTF-8  #设置编码
ff = open('./TXT_de.md', 'w')
with open('./1.txt', 'r') as f:
    line = f.readlines()
    for line_list in line:
        line_new = line_list.replace('\r\n','')
        line_new = line_new + ';' + '\r\n'
        print(line_new)
        ff.write(line_new)
