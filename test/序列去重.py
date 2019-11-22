import os
filelist=[]
ss=set()
dd={}
tt=[]
def getText(url):
    with open(url, 'r',encoding="GBK") as f:
        text=f.read()
        return text
for root, dirs, files in os.walk('C:/Users/v5682/Desktop/2019-11-11'):
    #print(root) #当前目录路径
    #print(dirs) #当前路径下所有子目录
    #print(files) #当前路径下所有非目录子文件
    for file in files:
        if(os.path.splitext(file)[1] == '.tcf'):
            filelist.append(os.path.join(root, file))
            text=getText(os.path.join(root, file))
            dd[text]=os.path.join(root, file)

for d1 in dd:
    tmp=0
    for fi in filelist:
        text=getText(fi)
        if(text==d1):
            if(tmp==0):
                tmp=tmp+1
            else:
                os.remove(fi)
                print("删"+fi)





#for li in filelist:
    #text=getText(li)





