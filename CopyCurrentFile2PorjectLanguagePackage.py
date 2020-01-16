import os

Project_LanguagePackage_Dir=r'../wikifx/ZJNews/Sources/LocalibSource/'
Current_Direct=r'./'


def projectLanguagePackageDirectories():
	file_array = []
	dir_array = []
	for root, dirs, files in os.walk(Project_LanguagePackage_Dir):
		for dir in dirs:
			# print(dir)
			dir_array.append(dir)
	return dir_array

def fetch_file_name(dir_path):
    array = []
    for root, dirs, files in os.walk(dir_path):
    	# print(root, dirs, files)
        for file in files:
			# print(file)
            if os.path.splitext(file)[1] == '.md':
            	array.append(os.path.splitext(file)[0])
    return array

def matchDirWithFileName(file_name, dir_name):
	fileNameShort = file_name.split('_')[-1]
	dirNameShort = dir_name.split('.')[0]
	if fileNameShort == dirNameShort:
		# print(file_name + " and " + dir_name + " is Ture")
		return True
	elif mapNameForShort(fileNameShort) == dirNameShort:
		# print(file_name + " and " + dir_name + " is Ture")
		return True
	else:
		return False
	pass

def mapNameForShort(fileNameShort):
	if fileNameShort == 'pt':
		return 'pt-PT'
	if fileNameShort == 'zh-CN':
		return 'zh-Hans'
	if fileNameShort == 'zh-HK':
		return 'zh-Hant'
	if fileNameShort == 'zh-TW':
		return 'zh-HK'


def getSpecificWriteFileName(dir_name):
	# print(os.path.abspath(dir_name))
	fp = Project_LanguagePackage_Dir + dir_name + "/Localizable.strings"
	# print(os.path.abspath(fp))
	return fp


def transactionReadWrite(readFilePath, writeFilePath):
	newFile = open(writeFilePath, 'w')
	with open(readFilePath, 'r') as originFile:
		line_list = originFile.readlines()
		for line in line_list:
			newFile.write(line)




txtArr = fetch_file_name(Current_Direct)
# print(txtArr)
ppDirArr = projectLanguagePackageDirectories()
# print(ppDirArr)

for txt_file_name in txtArr:
	for dir_name in ppDirArr:
		# print(matchDirWithFileName(txt_file_name, dir_name))
		if matchDirWithFileName(txt_file_name, dir_name):
			transactionReadWrite(txt_file_name+".md", getSpecificWriteFileName(dir_name))
