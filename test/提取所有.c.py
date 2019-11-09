import os
import shutil
for root, dirs, files in os.walk('C:/Users/v5682/Desktop/新建文件夹'):
    #print(root) #当前目录路径
    #print(dirs) #当前路径下所有子目录
    #print(files) #当前路径下所有非目录子文件
    for file in files:
        if(os.path.splitext(file)[1] == '.c'):
            shutil.copy(os.path.join(root, file),'C:/Users/v5682/Desktop/新建文件夹1')