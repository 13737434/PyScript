import os
from 静态不符合项列表脚本.ProductOne import ProductOne
class ProductSome:
    #遍历某文件夹下的所有.mht文件
    def selectFile(self,file_dir):
        lists=[]
        for root, dirs, files in os.walk(file_dir):
            #print(root) #当前目录路径
            #print(dirs) #当前路径下所有子目录
            #print(files) #当前路径下所有非目录子文件
            for file in files:
                if os.path.splitext(file)[1] == '.mht':
                    lists.append(os.path.join(root, file))
        return lists

    #生成该目录下所有的.mht文件的报告
    def getAllReport(self,lists):
        productone=ProductOne()
        for list in lists:
            productone.getOneReport(list)


if __name__ == '__main__':
    a=ProductSome()
    lists=a.selectFile("C:\\Users\\v5682\\Desktop\\新建文件夹")
    a.getAllReport(lists)
    print("finish")

