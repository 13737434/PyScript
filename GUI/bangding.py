import tkinter
root=tkinter.Tk()
root.minsize(300,200)

# 单行文本
entry=tkinter.Entry(root)
entry.pack()


def changerd1(eventobj):
    eventobj.widget['bg']='red'
def changerd2(eventobj):
    eventobj.widget['bg']='green'


entry.bind('<FocusIn>',changerd1)# entry获取焦点组件 改变颜色
entry.bind('<FocusOut>',changerd2)# entry获取焦点组件 改变颜色


entry2=tkinter.Entry(root)
entry2.pack()

btn1=tkinter.Button(root,text='232323')
btn1.place(x=10,y=10,width=50,height=50)
btn2=tkinter.Button(root,text='2323')
btn2.place(x=70,y=70,width=50,height=50)
def changebg(e):
    e.widget['bg']='red'
btn1.bind_class('Button','<Enter>',changebg)


def change1(e):
    print(e.widget)
btn1.bind_all('<Button-1>',change1)

root.mainloop()