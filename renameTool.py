import os
import shutil
#使用步骤：1.将第一个文件改成xxx(0) 2.改文件夹地址 3.改nameList & selectList 文件分两个文件夹

#中文合规地址，使用前改动
CHrootdir = 'C:/Users/Administrator/Desktop/xxx'
#英文合规地址，使用前改动
PYrootdir = 'C:/Users/Administrator/Desktop/xxx'

#输出地址，不改会自动生成
combineDir = 'C:/Users/Administrator/Desktop/combine'
rootDirs = [CHrootdir,PYrootdir]
for rootdir in rootDirs:
    nameList = [
        '王涛',
    ]
    selectList = [
        '刘洋',
        '王涛',
    ]
    dirs = os.listdir(rootdir)
    for i in range(len(dirs)):
        oldname = rootdir + '/' + dirs[i]
        nameIndex = int(dirs[i].split(' (')[1].split(')')[0])
        nameName = nameList[nameIndex]
        if rootdir == PYrootdir:
            newname = rootdir + '/' + dirs[i].split(' (')[0] + nameList[nameIndex] + 'py' + dirs[i].split(' (')[1].split(')')[1]
        else:
            newname = rootdir + '/' + dirs[i].split(' (')[0] + nameList[nameIndex] + dirs[i].split(' (')[1].split(')')[1]
        os.rename(oldname,newname)
        print(oldname, '==>', newname)
        if nameName in selectList:
            if not os.path.exists(combineDir):
                os.makedirs(combineDir)
            dsFilePath = combineDir + '/' + newname.split(')')[1]
            shutil.copyfile(newname,dsFilePath)
            print('moving',newname,'==>',dsFilePath)

