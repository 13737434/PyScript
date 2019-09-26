import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import threading
import base64
import os
from 函数调用关系.Deal import Deal

class Show:
    isaddtxt=False #判断是否导入文本
    getFundict={} #调用level1：【调用level2，，，，，】
    getFundict_1={} #调用level1：【入口函数名称，，，，，，】
    deal=Deal()
    funlist=[]  #要操作的函数列表

    def __init__(self):
        self.UIInit()  # 界面初始化

    def UIInit(self):
        # tmp = open("tmp.ico","wb+")
        # tmp.write(base64.b64decode(img))
        # tmp.close()
        self.root=tkinter.Tk()
        self.root.title('函数调用关系')
        self.root.geometry('270x560+100+200')
        self.root.resizable(0,0)
        # self.root.iconbitmap('tmp.ico')
        # os.remove("tmp.ico")



        # 消息提示区
        self.labmesstitle=tkinter.Label(self.root,text='消息提示')
        self.labmesstitle.place(x=100,y=10,height=20)
        self.txtmessshow=tkinter.Text(self.root, bg="#ffffff")
        self.txtmessshow.place(x=10, y=30, width=250, height=150)
        self.scroll = tkinter.Scrollbar(self.txtmessshow)
        self.scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.txtmessshow.config(yscrollcommand=self.scroll.set)

        # 导入文本文件按钮
        self.labaddtxt=tkinter.Label(self.root,text='导入文本文件进行解析')
        self.labaddtxt.place(x=10, y=200)
        self.btnaddtxt=tkinter.Button(self.root,text='导入',command=self.clickAddTxt)#
        self.btnaddtxt.place(x=165,y=200,width=80,height=25)

        # 添加要操作的函数名
        self.txtaddfun=tkinter.StringVar()
        self.labaddfun=tkinter.Label(self.root,text='添加要操作的函数名（区分大小写及下划线）')
        self.labaddfun.place(x=10, y=240)
        self.entaddfun=tkinter.Entry(self.root,textvariable=self.txtaddfun)
        self.entaddfun.place(x=20,y=265,width=170,height=30)
        self.btnaddfun=tkinter.Button(self.root,text='+',font = ('宋体', 20,"bold"),command=self.clickAddFun)#
        self.btnaddfun.place(x=200,y=265,width=30,height=30)
        self.labremove=tkinter.Label(self.root,text='双击列表中函数名可将其移除')
        self.labremove.place(x=50,y=320)

        # 生成报告单
        self.btnexport=tkinter.Button(self.root,text='导出列表中函数',command=self.clickMakeReport)#
        self.btnexport.place(x=20,y=520,width=100,height=25)
        self.btnexport=tkinter.Button(self.root,text='导出所有函数',command=self.clickMakeReport_all)#
        self.btnexport.place(x=140,y=520,width=100,height=25)

        # 解析完文本生成的表格
        columns = ("funname")
        self.treeview=tkinter.ttk.Treeview(self.root,height=100,show='headings',columns=columns)
        self.treeview.column("funname", width=100, anchor='center') # 设置首列 不显示
        self.treeview.heading("funname", text="函数名") # 设置表头
        self.treeview.place(x=10,y=350,width=250,height=160)
        self.treeview.bind('<Double-1>', self.doubleClick) # 双击左键移除该函数

        self.root.mainloop()

     #导入文本文件事件
    def clickAddTxt(self):
        self.txtmessshow.delete('1.0','end')
        self.filepath=tkinter.filedialog.askopenfilename(title='请选择Understand生成的文本文件',filetypes=(("text files", "*.txt;"),))
        if(self.filepath):#判断是否导入成功
            '''初始化'''
            self.isaddtxt=False
            self.getFundict={}
            self.getFundict_1={}
            self.funlist=[]
            ''''''
            def thread1(filepath):
                try:
                    self.txtmessshow.insert(tkinter.END, '正在解析文本...\n--------------------------------\n')
                    self.txtmessshow.see(tkinter.END)
                    text=self.deal.getString(filepath)#解析文本
                    if(self.deal.isTrue(text)):#判断文本是否符合要求
                        self.getFundict=self.deal.getFunDict(text)#获得字典 函数名--.c文件名
                        self.getFundict_1=self.deal.getFunDict_1(self.getFundict)#获得字典 函数名--圈复杂度
                        self.isaddtxt=True
                        self.funlist=[]
                        self.txtmessshow.insert(tkinter.END, '文本解析成功,继续下一步\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                    else:
                        self.txtmessshow.insert(tkinter.END, '文本不符合要求，请重新导入\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                except Exception as exc:
                    self.isaddtxt=False
                    tkinter.messagebox.showerror("Finish",exc)
                    print(exc)
            th=threading.Thread(target=thread1,args=(self.filepath,))
            th.setDaemon(True)
            th.start()
        else:
            self.txtmessshow.insert(tkinter.END, '导入文本失败\n--------------------------------\n')
            self.txtmessshow.see(tkinter.END)

    # 添加函数
    def clickAddFun(self):
        if(self.isaddtxt): #操作1完成，执行操作2
            tmpfun=self.txtaddfun.get()
            if(tmpfun in self.getFundict):
                if(tmpfun not in self.funlist):
                    self.funlist.append(tmpfun)
                    self.treeview.insert('','end', values=(tmpfun))
                    self.txtmessshow.insert(tkinter.END, tmpfun+'添加成功\n--------------------------------\n')
                    self.txtmessshow.see(tkinter.END)
                    self.txtaddfun.set('')
                else:
                    self.txtmessshow.insert(tkinter.END, '重复添加\n--------------------------------\n')
                    self.txtmessshow.see(tkinter.END)
            else:
                self.txtmessshow.insert(tkinter.END, '输入的函数名错误或不存在\n--------------------------------\n')
                self.txtmessshow.see(tkinter.END)
        else:
            self.txtmessshow.insert(tkinter.END, '还未导入文本\n--------------------------------\n')
            self.txtmessshow.see(tkinter.END)

    # 双击某一项可以删除
    def doubleClick(self,event):
        if(len(self.funlist)>0):
            row = self.treeview.identify_row(event.y)  # 行  从1开始
            if(self.treeview.item(row)['values']):
                tmpfun=self.treeview.item(row)['values'][0]
                self.funlist.remove(tmpfun)
                self.treeview.delete(row)
                self.txtmessshow.insert(tkinter.END,tmpfun+ '删除成功\n--------------------------------\n')
                self.txtmessshow.see(tkinter.END)
            else:
                print('Click Null!')
        else:
            print('Click Null!')

    # 生成按钮点击事件 部分
    def clickMakeReport(self):
        if(self.funlist):
            self.savepath=tkinter.filedialog.askdirectory(title='请选择保存路径')
            if(self.savepath):
                def thread2(funlists):
                    try:
                        self.txtmessshow.insert(tkinter.END,'正在生成\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        self.deal.makeExcel(funlists,self.getFundict,self.getFundict_1,self.savepath)
                        self.txtmessshow.insert(tkinter.END,'任务结束\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        tkinter.messagebox.showinfo("Finish","任务结束.")
                    except Exception as exc:
                        tkinter.messagebox.showerror("Finish",exc)
                        print(exc)
                th=threading.Thread(target=thread2,args=(self.funlist,))
                th.setDaemon(True)
                th.start()
            else:
                self.txtmessshow.insert(tkinter.END, '未选择保存路径\n--------------------------------\n')
                self.txtmessshow.see(tkinter.END)

        else:
            self.txtmessshow.insert(tkinter.END, '没有可生成的对象\n--------------------------------\n')
            self.txtmessshow.see(tkinter.END)

        # 生成按钮点击事件 全部
    def clickMakeReport_all(self):
        if(self.isaddtxt):
            self.savepath=tkinter.filedialog.askdirectory(title='请选择保存路径')
            if(self.savepath):
                def thread2(funlists):
                    try:
                        self.txtmessshow.insert(tkinter.END,'正在生成\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        self.deal.makeExcel_all(self.getFundict,self.getFundict_1,self.savepath)
                        self.txtmessshow.insert(tkinter.END,'任务结束\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        tkinter.messagebox.showinfo("Finish","任务结束.")
                    except Exception as exc:
                        tkinter.messagebox.showerror("Finish",exc)
                        print(exc)
                th=threading.Thread(target=thread2,args=(self.funlist,))
                th.setDaemon(True)
                th.start()
            else:
                self.txtmessshow.insert(tkinter.END, '未选择保存路径\n--------------------------------\n')
                self.txtmessshow.see(tkinter.END)

        else:
            self.txtmessshow.insert(tkinter.END, '没有可生成的对象\n--------------------------------\n')
            self.txtmessshow.see(tkinter.END)

if __name__ == '__main__':
    Show()