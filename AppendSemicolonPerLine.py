# coding: UTF-8  #设置编码
import os

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

file_name_arrays = fetch_file_name(directory_path)
for file_name in file_name_arrays:
    markdown_file_name = file_name.replace('.txt', '.md')
    # print(markdown_file_name)
    createSameNameMarkDownFile(markdown_file_name)
    appendSymbolToNewFile(file_name, markdown_file_name)
