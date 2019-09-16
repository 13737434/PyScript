import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import datetime
import threading
import base64
import os
from tkinter import ttk


class Show:
    def __init__(self):
        self.nowyear=datetime.datetime.now().strftime('%Y') #当前年
        self.nowmonth=datetime.datetime.now().strftime('%m') #当前月
        self.nowday=datetime.datetime.now().strftime('%d') #当前日
        self.UIInit()  # 界面初始化
    def UIInit(self):
        # tmp = open("tmp.ico","wb+")
        # tmp.write(base64.b64decode(img))
        # tmp.close()
        self.root=tkinter.Tk()
        self.root.title('单元测试用例集-Script')
        self.root.geometry('300x380+100+200')
        self.root.resizable(0,0)
        # self.root.iconbitmap('tmp.ico')
        # os.remove("tmp.ico")

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
        self.cmbmonth=tkinter.Label(self.root,text='月')
        self.cmbmonth.place(x=170,y=70,height=20)

        self.cmbday=ttk.Combobox(self.root)
        self.cmbday['value']=[int(self.nowday)]+[n for n in range(1,32)]
        self.cmbday.current(0)
        self.cmbday.place(x=200,y=70,width=45,height=20)
        self.cmbday=tkinter.Label(self.root,text='日')
        self.cmbday.place(x=250,y=70,width=30,height=20)

        # 消息提示区
        self.txtmessshow=tkinter.Text(self.root, bg="#ffffff")
        self.txtmessshow.place(x=30, y=200, width=250, height=150)
        self.scroll = tkinter.Scrollbar(self.txtmessshow)
        self.scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.txtmessshow.config(yscrollcommand=self.scroll.set)









        self.root.mainloop()


if __name__ == '__main__':
    Show()