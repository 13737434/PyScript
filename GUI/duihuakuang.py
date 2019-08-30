#messagebox消息对话框
import tkinter
# 导入消息对话框子模块
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.filedialog
import tkinter.colorchooser
# 创建主窗口
root=tkinter.Tk()
root.minsize(300,300)
root.title('22222')
'''
def okcancel():
    # 弹出对话框
    result=tkinter.messagebox.askokcancel(title='okcancel',message='选择啥啊')
    print(result)
btn1=tkinter.Button(root,text='okcancel',command=okcancel)

btn1.pack()
'''

'''
def question():
#弹出对话框
    result=tkinter.messagebox.askquestion(title='question',message='122221212121')
    print(result)
# 添加按钮


btn2=tkinter.Button(root,text='question',command=question)
btn2.pack()
'''
'''
def askname():
    result=tkinter.simpledialog.askstring(title='获取信息',prompt='请输入xxx',initialvalue='匿名')
    print(result)

btn3=tkinter.Button(root,text='获取用户名',command=askname)
btn3.pack()
'''
'''
# 定义函数
def filename():
    path=tkinter.filedialog.askopenfilename() # askopenfilename 选择单个文件获取路径   askopenfilenames 多个文件路径 元组
    print(path)                                #askopenfile 打开文件获取单个文件指针具有open的作用   askopenfiles打开多个文件 。。。
                                               #askdirectory获取一个文件夹路径
                                               # asksaveasfilename()选择保存路径
def openfile():
    path=tkinter.filedialog.askopenfilename(initialdir='d:/',initialfile='abc.exe',title='打开某个文件')
btn4=tkinter.Button(root,text='filename',command=openfile)
btn4.pack()
'''

def color():
    result=tkinter.colorchooser.askcolor(color='cyan')
    print(result)
    root['bg']=result[1]
btn5=tkinter.Button(root,text='选择颜色',command=color)
btn5.pack()



root.mainloop()