import tkinter
root=tkinter.Tk()
'''
text=tkinter.StringVar()
text.set("222222")
# 设置复选框勾选与否的值
result=tkinter.IntVar()

# 设置操作checkbutton的方法
def func():
    print(result.get())
checkbtn=tkinter.Checkbutton(root,textvariable=text,variable=result,command=func)
checkbtn=tkinter.Checkbutton(root,textvariable=text,variable=result,command=func,onvalue=66,offvalue=77)
checkbtn.pack()
'''


'''
# 单行文本输入
username=tkinter.Entry(root,width=50)
username.pack()

password=tkinter.Entry(root,show="*")
password.pack()
'''



'''
#  创建框架1
frame1=tkinter.Frame(root,bg="red",width="500",height="100")
frame1.pack(side='top')
# 框架1中横向摆放
btn1=tkinter.Button(frame1,text="按钮1")
btn1.pack()
btn2=tkinter.Button(frame1,text="按钮1")
btn2.pack()
btn3=tkinter.Button(frame1,text="按钮1")
btn3.pack()

frame2=tkinter.Frame(root,bg="blue",width="500",height="100")
frame2.pack()
'''


'''
lableframe=tkinter.LabelFrame(root,text='122222222')
lableframe.pack()
btn1=tkinter.Button(lableframe,text='wwww')
btn1.pack()
'''


'''
lable=tkinter.Label(root,text='标签')
lable.pack()
'''


'''
# 设置listbox内容
names=('1111','222222','33333','44444444','555555')
# 将数据转换为tkinter额字符串变量
strings=tkinter.StringVar(value=names)

listbox=tkinter.Listbox(root,listvariable=strings)
listbox.pack()
'''
def p():
    print('1111')


'''
# 1创建主菜单
menu1=tkinter.Menu(root)
# 2.创建子菜单    设置菜单不具有撕下功能
filemenu=tkinter.Menu(menu1,tearoff=0)
# 子菜单可以添加功能
filemenu.add_command(label='打开文件',command=p)
# 3.将子菜单加入主菜单
menu1.add_cascade(label='文件',menu=filemenu)
# 2.创建子菜单
filemenu=tkinter.Menu(menu1,tearoff=0)
# 3.将子菜单加入主菜单
menu1.add_cascade(label='创建',menu=filemenu)

# 4.将主菜单加入界面
root.config(menu=menu1)
'''

'''
text=tkinter.Text(root,width=50,height=10)
text.pack()

text.insert('0.0','222222333333333')
'''

''''''
def talk():
    newroot=tkinter.Toplevel()

btn=tkinter.Button(root,text='新窗口',command=talk)
btn.pack()



root.mainloop()