import re
from openpyxl import load_workbook
class Deal:
    def __init__(self,Model):
        self.model=Model

    #获取 XXXXX.mht 中的文本
    def getString(self, url):
        with open(url, 'r') as f:
            text=f.read()
        return text

    #获取文件名
    def getFileName(self,str):
        pattern=re.compile(r'<H1>File.*\\(.*?)\.c.*?</H1>',re.S)
        file_name=re.findall(pattern,str)[0].replace("\n", "").replace("=", "")
        return file_name

    #解析红色部分
    def parseRedString(self,str):
        pattern=re.compile('<TR>.*?bgColor=3D#ff8181.*?\.htm">(.*?)</A>.*?color=3Dblue>(.*?)</FONT>.*?\.write\(\'(.*?)\'\).*?</FONT></TD></TR>',re.S)
        items=re.findall(pattern,str)
        return items
    #解析蓝色部分
    def parseYellowString(self,str):
        pattern=re.compile('<TR>.*?bgColor=3Dyellow.*?<CENTER>(.*?)</CENTER>.*?3Dblue>(.*?)</FONT>.*?write\(\'(.*?)\'\).*?</FONT></TD></TR>',re.S)
        items=re.findall(pattern,str)
        return items

    #写入 Excel 文档
    def dataWrite(self,items,savepath):
        #wb=Workbook() #创建Excel文件对象
        wb=load_workbook('Demo.xlsx')  #获取Excel文件对象
        ws=wb.active #获取第一个sheet
        i=2
        for item in items:
            ws["A"+str(i)]=i-1
            ws["B"+str(i)]= self.model.filename+ ".c"
            ws["C"+str(i)]=self.model.testskill
            ws["D"+str(i)]=item[1].replace("\n", "").replace("=", "")+':'+item[2].replace("\n", "").replace("=", "")
            ws["E"+str(i)]=item[0].replace("\n", "").replace("=", "")
            ws["F"+str(i)]=self.model.disqualificationlv
            ws["G"+str(i)]=self.model.verifytime
            ws["H"+str(i)]=self.model.dealway
            ws["I"+str(i)]=self.model.explanation
            ws["J"+str(i)]=self.model.confirmperson
            ws["K"+str(i)]=self.model.testperson
            ws["L"+str(i)]=self.model.stated
            i+=1
        wb.save(savepath+'\\'+ self.model.filename + "-静态不符合项列表.xlsx")  #保存

    #生成一份报告
    def getOneReport(self,filepath,savepath):
        text=self.getString(filepath)
        self.model.filename=self.getFileName(text)
        redItems=self.parseRedString(text)
        yellowItems=self.parseYellowString(text)
        self.dataWrite(redItems+yellowItems,savepath)
        return self.model.filename

    #生成所有的.mht文件的报告
    # def getAllReport(self,filelist):
    #     for file in filelist:
    #         self.getOneReport(file)



