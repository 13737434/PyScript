import re
from bs4 import BeautifulSoup
class Deal:
    #获取 XXXXX.mht 中的文本
    def getString(self, url):
        try:
            with open(url, 'r',errors="ignore",encoding="") as f:
                self.text=f.read()
        except:
            with open(url, 'r',encoding="utf-8",errors="ignore") as f:
                self.text=f.read()


    #通过bs4解析库解析
    def getBS(self):
        bs=BeautifulSoup(self.text,'html.parser')
        self.bs=bs

    #解析出标题是否符合要求
    def txtIsTrue(self):
        if(self.bs.title.text=='LDRA Testbed Dataflow Report'):
            return True
        else:
            return False

    #解析出UR DU DD 标题（结点h4）                                  ，然后解析对应下一个结点(center)为表格
    def getAllTable(self):
        h4list=self.bs.find_all('h4')
        tmpURTable=[]
        tmpDUTable=[]
        tmpDDTable=[]
        for li in h4list:
            txt=str(li.text).replace("=20","").replace("=","").replace("\n","").replace(" ","")
            if("TypeURAnomalies" in txt): #查找UR
                tmpURTable=self.getTable(li)
            if("TypeDUAnomalies" in txt): #查找DU
                tmpDUTable=self.getTable(li)
            if("TypeDDAnomalies" in txt): #查找DD
                tmpDDTable=self.getTable(li)
        return [tmpURTable,tmpDUTable,tmpDDTable]


    #解析 UR DU DD
    def getTable(self,node):
        center=node.find_next('center')
        trs=center.find_all('tr')
        if(len(trs)>2):  #有数据的情况
            tmptd=[]
            for tr in trs:
                tds=tr.find_all('td')
                for td in tds:
                    tmptd.append(td.text.replace("=\n","").replace("=3D","="))
            return [tmptd[i:i+4] for i in range(0,len(tmptd),5)]
        else:#无数据情况
            return []

    #获取c文件名字
    def getCName(self):
        try:
            patternfilename=re.compile(r'\((\w+\.c)\)',re.S)
            file_name=re.findall(patternfilename,self.text)[0]
            return file_name
        except:
            return "unknow"


if __name__ == '__main__':
    dd=Deal()
    dd.getString("C:/Users/v5682/Desktop/新建文件夹/02.mht")
    dd.getBS()
    if(dd.txtIsTrue()):
        print(dd.getCName())
        for tt in dd.getAllTable()[2]:
            print(tt)
    else:
        print("不正确的报告格式")


