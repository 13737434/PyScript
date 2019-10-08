import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import datetime
import threading
import base64
import os
from 圈复杂度脚本.icon import img
from 圈复杂度脚本.Model import Model
from 圈复杂度脚本.Deal import Deal

class Show:
    isaddtxt=False #判断是否导入文本
    getallcyclomatic={}  #所有函数的Cyclomatic exp:{'app_inf_get_sdpbtm_par', '4'}
    getallfun={} #所有函数所在的.c文件 exp:{'abs_value': 'utilities.c'}
    funlist=[]  #要操作的函数列表
    deal=Deal()


    def __init__(self):
        self.nowtime=datetime.datetime.now().strftime('%Y%m%d') #当前时间
        self.UIInit()  # 界面初始化


    def UIInit(self):
        tmp = open("tmp.ico","wb+")
        tmp.write(base64.b64decode(img))
        tmp.close()
        self.root=tkinter.Tk()
        self.root.title('静态度量问题报告单-Script')
        self.root.geometry('500x560+100+200')
        self.root.resizable(0,0)
        self.root.iconbitmap('tmp.ico')
        os.remove("tmp.ico")

        # 严重程度
        self.txtseriouslv=tkinter.StringVar()
        self.txtseriouslv.set('一般')
        self.labseriouslv=tkinter.Label(self.root,text='严重程度  :')
        self.labseriouslv.place(x=10,y=10,width=100,height=20)
        self.entseriouslv=tkinter.Entry(self.root,textvariable=self.txtseriouslv)
        self.entseriouslv.place(x=120,y=10,width=100,height=20)

        # 发现方式
        self.txtfindsub=tkinter.StringVar()
        self.txtfindsub.set('质量度量')
        self.labfindsub=tkinter.Label(self.root,text='发现方式  :')
        self.labfindsub.place(x=10,y=40,width=100,height=20)
        self.entfindsub=tkinter.Entry(self.root,textvariable=self.txtfindsub)
        self.entfindsub.place(x=120,y=40,width=100,height=20)

        # NCR分类
        self.txtNCRclass=tkinter.StringVar()
        self.txtNCRclass.set('编码缺陷')
        self.labNCRclass=tkinter.Label(self.root,text='NCR分类  :')
        self.labNCRclass.place(x=10,y=70,width=100,height=20)
        self.entNCRclass=tkinter.Entry(self.root,textvariable=self.txtNCRclass)
        self.entNCRclass.place(x=120,y=70,width=100,height=20)

        # 发现时间
        self.txtfindtime=tkinter.StringVar()
        self.txtfindtime.set(self.nowtime)
        self.labfindtime=tkinter.Label(self.root,text='发现时间  :')
        self.labfindtime.place(x=10,y=100,width=100,height=20)
        self.entfindtime=tkinter.Entry(self.root,textvariable=self.txtfindtime)
        self.entfindtime.place(x=120,y=100,width=100,height=20)

        # 发现人
        self.txtfindperson=tkinter.StringVar()
        self.txtfindperson.set('XXX')
        self.labfindperson=tkinter.Label(self.root,text='发现人  :')
        self.labfindperson.place(x=10,y=130,width=100,height=20)
        self.entfindperson=tkinter.Entry(self.root,textvariable=self.txtfindperson)
        self.entfindperson.place(x=120,y=130,width=100,height=20)

        # 问题个数
        self.txtquestionnum=tkinter.StringVar()
        self.txtquestionnum.set('1')
        self.labquestionnum=tkinter.Label(self.root,text='问题个数  :')
        self.labquestionnum.place(x=10,y=160,width=100,height=20)
        self.entquestionnum=tkinter.Entry(self.root,textvariable=self.txtquestionnum)
        self.entquestionnum.place(x=120,y=160,width=100,height=20)

        # 处理意见
        self.txtdealopinion=tkinter.StringVar()
        self.txtdealopinion.set('说明')
        self.labdealopinion=tkinter.Label(self.root,text='处理意见  :')
        self.labdealopinion.place(x=10,y=190,width=100,height=20)
        self.entdealopinion=tkinter.Entry(self.root,textvariable=self.txtdealopinion)
        self.entdealopinion.place(x=120,y=190,width=100,height=20)

        # 解决措施
        self.txtsolution=tkinter.StringVar()
        self.txtsolution.set('代码经多轮测试验证，逻辑正确，符合设计')
        self.labsolution=tkinter.Label(self.root,text='解决措施  :')
        self.labsolution.place(x=10,y=220,width=100,height=20)
        self.entsolution=tkinter.Entry(self.root,textvariable=self.txtsolution)
        self.entsolution.place(x=120,y=220,width=100,height=20)

        # 研发确认
        self.txtconfirmperson=tkinter.StringVar()
        self.txtconfirmperson.set('XXX')
        self.labconfirmperson=tkinter.Label(self.root,text='研发确认  :')
        self.labconfirmperson.place(x=10,y=250,width=100,height=20)
        self.entconfirmperson=tkinter.Entry(self.root,textvariable=self.txtconfirmperson)
        self.entconfirmperson.place(x=120,y=250,width=100,height=20)

        # 验证时间
        self.txtverifytime=tkinter.StringVar()
        self.txtverifytime.set(self.nowtime)
        self.labverifytime=tkinter.Label(self.root,text='验证时间  :')
        self.labverifytime.place(x=10,y=280,width=100,height=20)
        self.entverifytime=tkinter.Entry(self.root,textvariable=self.txtverifytime)
        self.entverifytime.place(x=120,y=280,width=100,height=20)

        # 状态
        self.txtstated=tkinter.StringVar()
        self.txtstated.set('closed')
        self.labstated=tkinter.Label(self.root,text='状态  :')
        self.labstated.place(x=10,y=310,width=100,height=20)
        self.entstated=tkinter.Entry(self.root,textvariable=self.txtstated)
        self.entstated.place(x=120,y=310,width=100,height=20)

        # 消息提示区
        self.labmesstitle=tkinter.Label(self.root,text='消息提示')
        self.labmesstitle.place(x=330,y=10,height=20)
        self.txtmessshow=tkinter.Text(self.root, bg="#ffffff")
        self.txtmessshow.place(x=240, y=30, width=250, height=150)
        self.scroll = tkinter.Scrollbar(self.txtmessshow)
        self.scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.txtmessshow.config(yscrollcommand=self.scroll.set)

        # 导入文本文件按钮
        self.labaddtxt=tkinter.Label(self.root,text='1.导入文本文件进行解析')
        self.labaddtxt.place(x=240, y=200)
        self.btnaddtxt=tkinter.Button(self.root,text='导入',command=self.clickAddTxt)
        self.btnaddtxt.place(x=395,y=200,width=80,height=25)

        # 添加要操作的函数名
        self.txtaddfun=tkinter.StringVar()
        self.labaddfun=tkinter.Label(self.root,text='2.添加要操作的函数名（区分大小写及下划线）')
        self.labaddfun.place(x=240, y=240)
        self.entaddfun=tkinter.Entry(self.root,textvariable=self.txtaddfun)
        self.entaddfun.place(x=250,y=265,width=170,height=30)
        self.btnaddfun=tkinter.Button(self.root,text='+',font = ('宋体', 20,"bold"),command=self.clickAddFun)
        self.btnaddfun.place(x=430,y=265,width=30,height=30)
        self.labremove=tkinter.Label(self.root,text='双击列表中函数名可将其移除')
        self.labremove.place(x=250,y=320)

        # 生成报告单
        self.labcyc=tkinter.Label(self.root,text="3.生成报告单(圈复杂度大于20)")
        self.labcyc.place(x=20,y=520)
        self.btnexport=tkinter.Button(self.root,text='生成列表中函数',command=self.clickMakeReport)
        self.btnexport.place(x=200,y=520,width=100,height=25)
        self.btnexport=tkinter.Button(self.root,text='生成所有函数',command=self.clickMakeReport1)
        self.btnexport.place(x=320,y=520,width=90,height=25)

        # 帮助
        self.labhelp=tkinter.Label(self.root,text='帮助',font = ('宋体', 10),fg='#0000ff')
        self.labhelp.place(x=420,y=520,width=90,height=30)
        self.labhelp.bind('<Button-1>',self.clickHelp)

        # 解析完文本生成的表格
        columns = ("funname", "cyclomatic","filename")
        self.treeview=tkinter.ttk.Treeview(self.root,height=100,show='headings',columns=columns)
        self.treeview.column("funname", width=100, anchor='center') # 设置首列 不显示
        self.treeview.column("cyclomatic", width=100, anchor='center')
        self.treeview.column("filename", width=100, anchor='center')
        self.treeview.heading("funname", text="函数名") # 设置表头
        self.treeview.heading("cyclomatic", text="圈复杂度")
        self.treeview.heading("filename", text="文件名")
        self.treeview.place(x=20,y=350,width=450,height=160)
        self.treeview.bind('<Double-1>', self.doubleClick) # 双击左键移除该函数




        self.root.mainloop()




     #导入文本文件事件
    def clickAddTxt(self):
        self.txtmessshow.delete('1.0','end')
        self.filepath=tkinter.filedialog.askopenfilename(title='请选择Understand生成的文本文件',filetypes=(("text files", "*.txt;"),))
        if(self.filepath):#判断是否导入成功
            '''初始化'''
            self.isaddtxt=False
            self.getallcyclomatic={}
            self.getallfun={}
            self.funlist=[]
            ''''''
            def thread1(filepath):
                try:
                    self.txtmessshow.insert(tkinter.END, '正在解析文本...\n--------------------------------\n')
                    self.txtmessshow.see(tkinter.END)
                    text=self.deal.getString(filepath)#解析文本
                    if(self.deal.isTrue(text)):#判断文本是否符合要求
                        self.getallcyclomatic=self.deal.getAllCyclomatic(text)#获得字典 函数名--.c文件名
                        self.getallfun=self.deal.getAllFunDict(text)#获得字典 函数名--圈复杂度
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
            if(tmpfun in self.getallcyclomatic):
                if(tmpfun not in self.funlist):
                    self.funlist.append(tmpfun)
                    if(tmpfun in self.getallfun):
                        self.treeview.insert('','end', values=(tmpfun, self.getallcyclomatic[tmpfun], self.getallfun[tmpfun]))
                    else:
                        self.treeview.insert('','end', values=(tmpfun, self.getallcyclomatic[tmpfun], 'null'))
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
            # column= self.treeview.identify_column(event.x)# 列  从1开始
            row = self.treeview.identify_row(event.y)  # 行  从1开始
            # cn = int(str(column).replace('#',''))
            # rn = int(str(row).replace('I',''))
            # sels=event.widget.selection()
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

    # 生成按钮点击事件
    def clickMakeReport(self):
        if(self.funlist):
            self.savepath=tkinter.filedialog.askdirectory(title='请选择保存路径')
            if(self.savepath):
                model=Model(self.txtseriouslv.get(),self.txtfindsub.get(),self.txtNCRclass.get(),self.txtfindtime.get(),self.txtfindperson.get(),self.txtquestionnum.get(),self.txtdealopinion.get(),self.txtsolution.get(),self.txtconfirmperson.get(),self.txtverifytime.get(),self.txtstated.get())
                def thread2(funlists):
                    try:
                        self.txtmessshow.insert(tkinter.END,'正在生成\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        newlists=[]
                        for tmpfun in funlists:
                            if int(self.getallcyclomatic[tmpfun])>20:
                                if(tmpfun in self.getallfun):
                                    newlists.append([tmpfun,self.getallcyclomatic[tmpfun],self.getallfun[tmpfun]])
                                else:
                                    newlists.append([tmpfun,self.getallcyclomatic[tmpfun],'需进入Excel手动添加'])
                        if(len(newlists)>0):
                            self.deal.makeExcel(model,newlists,self.savepath)
                        else:
                            self.txtmessshow.insert(tkinter.END,'没有不符合项\n--------------------------------\n')
                            self.txtmessshow.see(tkinter.END)
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

    # 生成所有 按钮点击事件
    def clickMakeReport1(self):
        if(self.isaddtxt):
            self.savepath=tkinter.filedialog.askdirectory(title='请选择保存路径')
            if(self.savepath):
                model=Model(self.txtseriouslv.get(),self.txtfindsub.get(),self.txtNCRclass.get(),self.txtfindtime.get(),self.txtfindperson.get(),self.txtquestionnum.get(),self.txtdealopinion.get(),self.txtsolution.get(),self.txtconfirmperson.get(),self.txtverifytime.get(),self.txtstated.get())
                def thread2(funlists):
                    try:
                        self.txtmessshow.insert(tkinter.END,'正在生成\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        newlists=[]
                        for tmpfun in funlists:
                            if int(self.getallcyclomatic[tmpfun])>20:
                                if(tmpfun in self.getallfun):
                                    newlists.append([tmpfun,self.getallcyclomatic[tmpfun],self.getallfun[tmpfun]])
                                else:
                                    newlists.append([tmpfun,self.getallcyclomatic[tmpfun],'需进入Excel手动添加'])
                        if(len(newlists)>0):
                            self.deal.makeExcel(model,newlists,self.savepath)
                        else:
                            self.txtmessshow.insert(tkinter.END,'没有不符合项\n--------------------------------\n')
                            self.txtmessshow.see(tkinter.END)
                        self.txtmessshow.insert(tkinter.END,'任务结束\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        tkinter.messagebox.showinfo("Finish","任务结束.")
                    except Exception as exc:
                        tkinter.messagebox.showerror("Finish",exc)
                        print(exc)
                th=threading.Thread(target=thread2,args=(self.getallcyclomatic,))
                th.setDaemon(True)
                th.start()
            else:
                self.txtmessshow.insert(tkinter.END, '未选择保存路径\n--------------------------------\n')
                self.txtmessshow.see(tkinter.END)

        else:
            self.txtmessshow.insert(tkinter.END, '没有可生成的对象\n--------------------------------\n')
            self.txtmessshow.see(tkinter.END)



    # 帮助按钮点击事件
    def clickHelp(self,e):
        self.txtmessshow.insert(tkinter.END, '错误反馈及建议 379221379@qq.com\n--------------------------------\n')
        self.txtmessshow.see(tkinter.END)



if __name__ == '__main__':
    Show()