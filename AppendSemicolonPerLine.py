# coding: UTF-8  #设置编码
import os
import re

directory_path = './'

def fetch_file_name(dir_path):
    array = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                array.append(os.path.join(file))
    return array

def appendSymbolToNewFile(originFileName, newFileName):
    ff = open(newFileName, 'w')
    with open(originFileName, 'r') as f:
        line = f.readlines()
        for line_list in line:
            line_new = line_list.replace('\r\n','')
            line_new = line_new + ';' + '\r\n'
            # print(line_new)
            ff.write(line_new)

def createSameNameMarkDownFile(filename):
        """
        创建日志文件夹和日志文件
        :param filename:
        :return:
        """
        # path = filename[0:filename.rfind("/")]
        # if not os.path.isdir(path):  # 无文件夹时创建
        #     os.makedirs(path)
        if not os.path.isfile(filename):  # 无文件时创建
            fd = open(filename, mode="w+")
            fd.close()
        else:
            pass


def reStep1Function(matchObj):
    # print(matchObj.group())
    string = matchObj.group()
    resultString = string.replace('\"','\\\"')
    return resultString
    pass

def reStep2Function(matchObj):
    string = matchObj.group()
    return string.replace('\\ \"', '\\\"')
    pass

def regularExpressionReplacementStep1(originFileName, tempFileName):
    # 匹配auf "Registrieren"这种格式的字符串，然后改为auf \"Registrieren\"
#    reString1 = r"(\w\s+\"+[\w\s]+\")|(\\+\s+\"+[\w]+\s+\\+\”)|([\w\"]\"[A-Za-z0-9_\\\s]+\")"
    # 匹配sur \ "Paramètres \" - \ "Accès这种格式的字符串，然后改为sur \"Paramètres \" - \"Accès
    reString2 = r"([\s]+\\[\s]+\"[A-Za-z0-9_\s]+?)"
    ff = open(tempFileName, mode="w")
    with open(originFileName, 'r') as f:
        line = f.readlines()
        for line_list in line:
#            line_add_backslash = re.sub(reString1, reStep1Function, line_list)    # 添加反斜杠
            line_remove_middle_space = re.sub(reString2, reStep2Function, line_list)  # 移除\ "中间的空格
            # line_new = line_remove_middle_space.replace('\\ n', '\\n')
            # print(line_new)
            ff.write(line_remove_middle_space)
        pass


def removeGarbageFile(deleteFileName):
    #判断文件是否存在
    if (os.path.exists(deleteFileName)):
       os.remove(deleteFileName)
       pass


file_name_arrays = fetch_file_name(directory_path)
for file_name in file_name_arrays:
    markdown_file_name = file_name.replace('.txt', '.md')
    markdown_temp_file_name = file_name.replace('.txt', '') + "_temp.md"
#     # print(markdown_temp_file_name)
    createSameNameMarkDownFile(markdown_file_name)
    regularExpressionReplacementStep1(file_name, markdown_temp_file_name)
    appendSymbolToNewFile(markdown_temp_file_name, markdown_file_name)
    pass

for file_name in file_name_arrays:
    markdown_temp_file_name = file_name.replace('.txt', '') + "_temp.md"
    removeGarbageFile(markdown_temp_file_name)
#    removeGarbageFile(file_name)
    pass

# for file_name in file_name_arrays:
#     # markdown_file_name = file_name.replace('.txt', '.md')
#     markdown_file_name = file_name.replace('.txt', '') + "_temp.md"
# #     # print(markdown_temp_file_name)
#     createSameNameMarkDownFile(markdown_file_name)
#     appendSymbolToNewFile(file_name, markdown_file_name)
#     pass

# for file_name in file_name_arrays:
#     markdown_file_name = file_name.replace('.txt', '.md')
#     markdown_temp_file_name = file_name.replace('.txt', '') + "_temp.md"
#     createSameNameMarkDownFile(markdown_file_name)
#     regularExpressionReplacementStep1(markdown_temp_file_name, markdown_file_name)
#     pass



