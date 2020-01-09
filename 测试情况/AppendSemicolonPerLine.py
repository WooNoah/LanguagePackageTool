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
    string = matchObj.group()
    resultString = string.replace('\\ \"', '\\\"')
    # print(resultString)
    return resultString
    pass

def reStep2Function(matchObj):
    # print(matchObj.group())
    string = matchObj.group()
    print(matchObj.group())
    resultString = string.replace('\"','\\\"')
    # print(resultString)
    return resultString
    pass

def reStep3Function(matchObj):
    string = matchObj.group()
    resultString = string.replace('\"','\\\"')
    return resultString
    pass

def reStep4Function(matchObj):
    string = matchObj.group()
    str_list = list(string)
    str_list.insert(1, '\\')
    resultString = ''.join(str_list)
    return resultString
    pass

def reStep5Function(matchObj):
    string = matchObj.group()
    resultString = string.replace(' ','')
    return resultString
    pass

def reStep6Function(matchObj):
    string = matchObj.group()
    string1 = string.replace('\"','\\\"')
    resultString = string1[:-1]
    return resultString
    pass

def regularExpressionReplacementPhase(originFileName, tempFileName):
    # 匹配auf "Registrieren"这种格式的字符串，然后改为auf \"Registrieren\"
    #reString1 = r"(\w\s+\"+[\w\s]+\")|(\\+\s+\"+[\w]+\s+\\+\”)|([\w\"]\"[A-Za-z0-9_\\\s]+\")" 

#2. \w\s+\"+[\w\s]+\"           筛选 click "Solved" or the "Service Agreement"这种情况
#3. [\w\"]+\"[A-Za-z_]+\"       筛选 "HB_000066"=",click"Setting" to enter the page";这个
#4. [\"]+\"\w+\"                筛选 "_001015"=""पंजीकरण" पर क्लिक करने这种情况
#5. \\\s+\"                     筛选 \ "这种情况
#6. \w+\"\\                     删选 đặt"\这种情况

    

    # 匹配sur \ "Paramètres \" - \ "Accès这种格式的字符串，然后改为sur \"Paramètres \" - \"Accès
    reString1 = r"([\s]+\\[\s]+\"[A-Za-z0-9_\s]+?)"
    # reString2 = r"(\w\s+\"+[\w\s]+\")"
    # reString2 = r"([\uAA80-\uAADF\u20000-\u2FFFD\w]\s+\"+[\w\s]+\")" 
    reString2 = r"([^]+?\s+\"[^\\]+?\")"
    # reString3 = r"([\w\"]+\"[A-Za-z_]+\")"
    reString4 = r"(\"+\"\w+\")"
    reString5 = r"(\\\s+\")"
    reString6 = r"(\w+\"\\)"


    ff = open(tempFileName, mode="w")
    with open(originFileName, 'r') as f:
        line = f.readlines()
        for line_list in line:
            # print(line_list)
            # tempString1 = re.sub(reString1, reStep1Function, line_list)  # 移除\ "中间的空格
            tempString2 = re.sub(reString2, reStep2Function, line_list)    # 添加反斜杠
            # tempString3 = re.sub(reString3, reStep3Function, tempString2)
            # tempString4 = re.sub(reString4, reStep4Function, tempString2)
            # tempString5 = re.sub(reString5, reStep5Function, tempString4)
            # tempString6 = re.sub(reString6, reStep6Function, tempString5)
            # line_new = line_remove_middle_space.replace('\\ n', '\\n')
            # print(tempString2)
            ff.write(tempString2)
        pass


def removeGarbageFile(deleteFileName):
    #判断文件是否存在
    if (os.path.exists(deleteFileName)):
       os.remove(deleteFileName)
       pass

def test():
    pass

file_name_arrays = fetch_file_name(directory_path)
for file_name in file_name_arrays:
    markdown_file_name = file_name.replace('.txt', '.md')
    markdown_temp_file_name = file_name.replace('.txt', '') + "_temp.md"
#     # print(markdown_temp_file_name)
    # createSameNameMarkDownFile(markdown_file_name)
    regularExpressionReplacementPhase(file_name, markdown_temp_file_name)
    # appendSymbolToNewFile(markdown_temp_file_name, markdown_file_name)
    pass

# for file_name in file_name_arrays:
#     markdown_temp_file_name = file_name.replace('.txt', '') + "_temp.md"
#     removeGarbageFile(markdown_temp_file_name)
# #    removeGarbageFile(file_name)
#     pass




