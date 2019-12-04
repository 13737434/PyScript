import tkinter
import tkinter.filedialog
import tkinter.messagebox
import threading
import base64
import os
from 函数来源.Deal import Deal
from 函数来源.icon import img

class Show:
    isaddtxt=False #判断是否导入文本
    dd=Deal()
    fundic={}

    def __init__(self):
        self.UIInit()# 界面初始化

    def UIInit(self):
        tmp = open("tmp.ico","wb+")
        tmp.write(base64.b64decode(img))
        tmp.close()
        self.root=tkinter.Tk()
        self.root.title('函数来源-Script')
        self.root.geometry('380x250+100+200')
        self.root.resizable(0,0)
        self.root.iconbitmap('tmp.ico')
        os.remove("tmp.ico")

        # 消息提示区
        self.txtmessshow=tkinter.Text(self.root, bg="#ffffff")
        self.txtmessshow.place(x=60, y=70, width=250, height=150)
        self.scroll = tkinter.Scrollbar(self.txtmessshow)
        self.scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.txtmessshow.config(yscrollcommand=self.scroll.set)

        # 添加按钮
        self.btnAdd=tkinter.Button(self.root,text='导入文本',command=self.clickAdd)
        self.btnAdd.place(x=80,y=20,width=90,height=30)

        # 导出按钮
        self.btnExport=tkinter.Button(self.root,text='生成',command=self.clickMaker)
        self.btnExport.place(x=190,y=20,width=90,height=30)

        self.root.mainloop()
    # 添加按钮点击事件
    def clickAdd(self):
        self.filepath=tkinter.filedialog.askopenfilename(title='请选择Understand生成的文本文件',filetypes=(("text files", "*.txt;"),))
        if(self.filepath):#判断是否导入成功
            '''初始化'''
            self.isaddtxt=False
            ''''''
            def thread1(filepath):
                try:

                    self.txtmessshow.insert(tkinter.END, '正在解析文本...\n--------------------------------\n')
                    self.txtmessshow.see(tkinter.END)
                    text=self.dd.getString(filepath)#解析文本
                    if(self.dd.isTrue(text)):#判断文本是否符合要求
                        self.fundic=self.dd.getCFileDict(text)
                        self.isaddtxt=True
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


    # 生成按钮点击事件
    def clickMaker(self):
            self.savepath=tkinter.filedialog.askdirectory(title='请选择保存路径')
            if(self.savepath and len(self.fundic)>0):
                self.errs=""
                def thread1():
                    try:
                        self.txtmessshow.insert(tkinter.END, '正在生成.\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        self.dd.makeExcel_all(self.fundic,self.savepath)
                        self.txtmessshow.insert(tkinter.END,'----导出完成\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        self.txtmessshow.insert(tkinter.END,'任务结束.\n--------------------------------\n')
                        self.txtmessshow.see(tkinter.END)
                        tkinter.messagebox.showinfo("Finish","任务结束.")
                    except Exception as exc:
                        tkinter.messagebox.showerror("Finish","请检查"+str(self.errs))
                th=threading.Thread(target=thread1)
                th.setDaemon(True)
                th.start()
            else:
                self.txtmessshow.insert(tkinter.END, '未选择保存路径或无内容\n--------------------------------\n')
                self.txtmessshow.see(tkinter.END)





if __name__ == '__main__':
    Show()