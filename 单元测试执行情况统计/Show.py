import tkinter
import tkinter.filedialog
import tkinter.messagebox
import threading
import base64
import os
from 单元测试执行情况统计.Deal import Deal
from 单元测试执行情况统计.icon import img

class Show:
    ischoose=False

    def __init__(self):
        self.UIInit()# 界面初始化

    def UIInit(self):
        tmp = open("tmp.ico","wb+")
        tmp.write(base64.b64decode(img))
        tmp.close()
        self.root=tkinter.Tk()
        self.root.title('单元测试执行情况统计-Script')
        self.root.geometry('380x330+100+200')
        self.root.resizable(0,0)
        self.root.iconbitmap('tmp.ico')
        os.remove("tmp.ico")

        # 注意事项
        self.lab1=tkinter.Label(self.root,text='注意事项  :1.确保LDRA Dynamic Coverage Analysis和LDRA\nTBrun Regression Report两中报告一 一对应\n2.只有文件夹导入模式(切记，只能是单元)\n3.备注部分需要自己补充')
        self.lab1.place(x=10,y=10)

        # 消息提示区
        self.txtmessshow=tkinter.Text(self.root, bg="#ffffff")
        self.txtmessshow.place(x=60, y=150, width=250, height=150)
        self.scroll = tkinter.Scrollbar(self.txtmessshow)
        self.scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.txtmessshow.config(yscrollcommand=self.scroll.set)

        # 添加按钮
        self.btnAdd=tkinter.Button(self.root,text='导入文件夹',command=self.clickAdd)
        self.btnAdd.place(x=80,y=100,width=90,height=30)

        # 导出按钮
        self.btnExport=tkinter.Button(self.root,text='生成',command=self.clickMaker)
        self.btnExport.place(x=190,y=100,width=90,height=30)

        self.root.mainloop()
    # 添加按钮点击事件
    def clickAdd(self):
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

    #递归遍历筛选文件
    def selectFile(self,dirpath):
        filelist=[]
        for root, dirs, files in os.walk(dirpath):
            #print(root) #当前目录路径
            #print(dirs) #当前路径下所有子目录
            #print(files) #当前路径下所有非目录子文件
            for file in files:
                if os.path.splitext(file)[1] == '.mht':
                    filelist.append(os.path.join(root, file))
        return filelist

    # 生成按钮点击事件
    def clickMaker(self):
        if(self.ischoose):
            self.savepath=tkinter.filedialog.askdirectory(title='请选择保存路径')
            if(self.savepath):
                def thread1(filelist):
                    try:
                        self.txtmessshow.insert(tkinter.END, '正在生成.\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        run=Deal()
                        ii=0
                        for li in filelist:
                            ii+=1
                            self.txtmessshow.insert(tkinter.END, '----解析文本'+str(ii)+'\n--------------------------------\n')
                            self.txtmessshow.see(tkinter.END)
                            text=run.getText(li)
                            run.dealText(text)
                        run.makeExcel(run.resultlist,run.casenumlist,self.savepath)
                        self.txtmessshow.insert(tkinter.END,'----导出完成\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        self.txtmessshow.insert(tkinter.END,'任务结束.\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        tkinter.messagebox.showinfo("Finish","任务结束.")
                        # self.ischoose=False #可以一次导入多次生成
                    except Exception as exc:
                        tkinter.messagebox.showerror("Finish",exc)
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





if __name__ == '__main__':
    Show()