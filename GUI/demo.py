import tkinter as tk
from PIL import Image,ImageTk
root=tk.Tk()

img=Image.open("img04.jpeg")
photo=ImageTk.PhotoImage(img)

lable1=tk.Label(root,text='这是一个标签',image=photo)
lable1.pack()


def onclick():
    print("点击了按钮")
btn=tk.Button(root,text="按钮",command=onclick)
btn.pack()

def click():
    global e
    print(""+e.get())
tk.Checkbutton(root,text="23333",command=click).pack()
tk.Checkbutton(root,text="23333",command=click).pack()

# 文本输入
e= tk.StringVar()
entry=tk.Entry(root,textvariable=e)
e.set("请输入...")
entry.pack()
def click1():
    global int_val
    print("选择的是",int_val.get())
int_val=tk.IntVar()
tk.Radiobutton(root,text="男",value="2",variable=int_val,command=click1).pack()
tk.Radiobutton(root,text="女",value="3",variable=int_val,command=click1).pack()

tk.Entry(root,show="#").pack()

root.mainloop()

