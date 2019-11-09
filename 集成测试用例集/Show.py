import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import datetime
import threading
import base64
from 集成测试用例集.icon import img
import os
from tkinter import ttk
from 集成测试用例集.Deal import *

class Show:
    ischoose=False
    def __init__(self):
        self.nowyear=datetime.datetime.now().strftime('%Y') #当前年
        self.nowmonth=datetime.datetime.now().strftime('%m') #当前月
        self.nowday=datetime.datetime.now().strftime('%d') #当前日
        self.UIInit()# 界面初始化

    def UIInit(self):
        tmp = open("tmp.ico","wb+")
        tmp.write(base64.b64decode(img))
        tmp.close()
        self.root=tkinter.Tk()
        self.root.title('集成测试用例集-Script')
        self.root.geometry('300x380+100+200')
        self.root.resizable(0,0)
        self.root.iconbitmap('tmp.ico')
        os.remove("tmp.ico")

        # 项目名称
        self.txtprojectname=tkinter.StringVar()
        self.txtprojectname.set('xxxxxxxxxxxxxxxxxx')
        self.labprojectname=tkinter.Label(self.root,text='项目名称  :')
        self.labprojectname.place(x=10,y=10,width=100,height=20)
        self.entprojectname=tkinter.Entry(self.root,textvariable=self.txtprojectname)
        self.entprojectname.place(x=120,y=10,width=150,height=20)

        # 测试人
        self.txttestpeople=tkinter.StringVar()
        self.txttestpeople.set('XXX')
        self.labtestpeople=tkinter.Label(self.root,text='测试人  :')
        self.labtestpeople.place(x=10,y=40,width=100,height=20)
        self.enttestpeople=tkinter.Entry(self.root,textvariable=self.txttestpeople)
        self.enttestpeople.place(x=120,y=40,width=150,height=20)

        # 年、月、日
        self.cmbyear=ttk.Combobox(self.root)
        self.cmbyear['value']=[int(self.nowyear)]+[int(self.nowyear)+n for n in range(-10,11)]
        self.cmbyear.current(0)
        self.cmbyear.place(x=30,y=70,width=55,height=20)
        self.labyear=tkinter.Label(self.root,text='年')
        self.labyear.place(x=85,y=70,height=20)

        self.cmbmonth=ttk.Combobox(self.root)
        self.cmbmonth['value']=[int(self.nowmonth)]+[n for n in range(1,13)]
        self.cmbmonth.current(0)
        self.cmbmonth.place(x=120,y=70,width=45,height=20)
        self.labmonth=tkinter.Label(self.root,text='月')
        self.labmonth.place(x=170,y=70,height=20)

        self.cmbday=ttk.Combobox(self.root)
        self.cmbday['value']=[int(self.nowday)]+[n for n in range(1,32)]
        self.cmbday.current(0)
        self.cmbday.place(x=200,y=70,width=45,height=20)
        self.labday=tkinter.Label(self.root,text='日')
        self.labday.place(x=250,y=70,width=30,height=20)

        # 消息提示区
        self.txtmessshow=tkinter.Text(self.root, bg="#ffffff")
        self.txtmessshow.place(x=30, y=200, width=250, height=150)
        self.scroll = tkinter.Scrollbar(self.txtmessshow)
        self.scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.txtmessshow.config(yscrollcommand=self.scroll.set)

        # 文件/文件夹模式选择
        self.int_val=tkinter.IntVar()
        self.int_val.set('11')
        self.rbtnChooseFile=tkinter.Radiobutton(self.root,text='选择文件',variable=self.int_val,value="11")
        self.rbtnChooseFile.place(x=20,y=120,height=20)
        self.rbtnChooseFiles=tkinter.Radiobutton(self.root,text='选择文件夹',variable=self.int_val,value="22")
        self.rbtnChooseFiles.place(x=20,y=150,height=20)

        # 添加按钮
        self.btnAdd=tkinter.Button(self.root,text='添加',command=self.clickAdd)
        self.btnAdd.place(x=140,y=118,width=90,height=30)

        # 导出按钮
        self.btnExport=tkinter.Button(self.root,text='生成',command=self.clickMaker)
        self.btnExport.place(x=140,y=150,width=90,height=30)


        self.root.mainloop()

        # 添加按钮点击事件
    def clickAdd(self):
        self.txtmessshow.delete('1.0','end')
        if(self.int_val.get()==11):
            self.filelist=tkinter.filedialog.askopenfilenames(title='请选择.tcf序列',filetypes=(("TCF files", "*.tcf;"),))
            self.txtmessshow.insert(tkinter.END, '选择了' + str(len(self.filelist)) + '个文件\n--------------------------------\n')
            self.txtmessshow.see(tkinter.END)
            if(len(self.filelist)>0):
                self.ischoose=True
            else:
                self.ischoose=False
        elif(self.int_val.get()==22):
            self.path=tkinter.filedialog.askdirectory(title='请选择文件夹')  #可遍历整个文件夹中所有的.mht文件
            if(self.path):
                self.filelist=self.selectFile(self.path)
                self.txtmessshow.insert(tkinter.END, '选择了' + str(len(self.filelist)) + '个文件\n--------------------------------\n')
                self.txtmessshow.see(tkinter.END)
                if(len(self.filelist)>0):
                    self.ischoose=True
                else:
                    self.ischoose=False
            else:
                self.txtmessshow.insert(tkinter.END, '未选择文件夹\n--------------------------------\n')
                self.txtmessshow.see(tkinter.END)

        else:
            self.txtmessshow.insert(tkinter.END, 'error\n')
            self.txtmessshow.see(tkinter.END)

    # 生成按钮点击事件
    def clickMaker(self):
        if(self.ischoose):
            self.savepath=tkinter.filedialog.askdirectory(title='请选择保存路径')
            if(self.savepath):
                def thread1(filelist):
                    self.errs=""
                    try:
                        self.txtmessshow.insert(tkinter.END, '正在生成.\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        deal=Deal(self.txtprojectname.get(),self.txttestpeople.get(),self.cmbyear.get(),self.cmbmonth.get(),self.cmbday.get())
                        list=[]
                        ii=1
                        for file in filelist:
                            self.errs=file
                            text1=deal.getText(file)
                            caselist1=deal.getCaseList(text1)
                            self.txtmessshow.insert(tkinter.END, '----解析文本'+str(ii)+'\n--------------------------------\n')
                            self.txtmessshow.see(tkinter.END)
                            list.append(caselist1)
                            ii+=1
                        self.txtmessshow.insert(tkinter.END,'----开始生成。。。\n--------------------------------\n')
                        deal.dealCase(list,self.savepath)
                        self.txtmessshow.insert(tkinter.END,'----导出完成\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        self.txtmessshow.insert(tkinter.END,'任务结束.\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        tkinter.messagebox.showinfo("Finish","任务结束.")
                        # self.ischoose=False #可以一次导入多次生成
                    except Exception as exc:
                        tkinter.messagebox.showerror("Finish",exc+"\n请检查"+self.errs)
                        print(exc)
                th=threading.Thread(target=thread1,args=(self.filelist,))
                th.setDaemon(True)
                th.start()
            else:
                self.txtmessshow.insert(tkinter.END, '未选择保存路径\n--------------------------------\n')
                self.txtmessshow.see(tkinter.END)
        else:
            self.txtmessshow.insert(tkinter.END, '没有可操作的文件\n--------------------------------\n')
            self.txtmessshow.see(tkinter.END)

    #递归遍历筛选文件
    def selectFile(self,dirpath):
        filelist=[]
        for root, dirs, files in os.walk(dirpath):
            #print(root) #当前目录路径
            #print(dirs) #当前路径下所有子目录
            #print(files) #当前路径下所有非目录子文件
            for file in files:
                if os.path.splitext(file)[1] == '.tcf':
                    filelist.append(os.path.join(root, file))
        return filelist





if __name__ == '__main__':
    Show()