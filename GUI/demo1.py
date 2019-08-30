#导入tkinter模块
import tkinter

# 创建主窗口对象
root=tkinter.Tk()
# 设置界面大小
# root.minsize(500,500)
root.geometry('300x400')
'''
绝对布局 单位像素
# 创建组件
btn1=tkinter.Button(root,text='按钮1')
btn1.place(x=100,y=20,width=50,height=50)

# 创建组件
btn1=tkinter.Button(root,text='按钮1')
btn1.place(x=200,y=20)

'''
# 字体
btn1=tkinter.Button(root,text='按钮1',bg='#1100ff',font=('黑体',40,'bold','italic'))
btn1.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.5)

# 锚点
btn2=tkinter.Button(root,text='锚点',anchor='nw',relief='flat')
btn2.pack(ipadx=20,ipady=20)

#位图
btn3=tkinter.Button(root,text='233',bitmap='question')
btn3.pack()

# 鼠标样式
btn4=tkinter.Button(root,text='鼠标',cursor="heart")
btn4.pack(ipadx=30,ipady=30)

# 图片设置


# 将主窗口对象加入消息循环 一直显示
# 主界面设置鼠标
root['cursor']='spider'
root.mainloop()