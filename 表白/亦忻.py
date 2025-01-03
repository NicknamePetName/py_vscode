import tkinter
import random
from tkinter import messagebox
# 图片模块
# from PIL import Image, ImageTk
 
root = tkinter.Tk()
root.title('表白信——>XXX')
root.geometry('750x500')
 
# 设置第一个页面的内容
frame_1 = tkinter.Frame(root)
frame_1.pack()
 
# 添加文本
lab_1 = tkinter.Label(frame_1, text='XXX，我喜欢你，所以要你做我女朋友！！',
                      font=50, padx=100, pady=30)
lab_1.pack(side=tkinter.LEFT)
 

# 添加文本
# lab_2 = tkinter.Label(frame_1, padx=30, pady=30,
#                       anchor=tkinter.N)
# lab_2.pack(side=tkinter.LEFT)


# 添加文本（表白人）
lab_3 = tkinter.Label(frame_1, text='表白人：XXX',
                      font=50, padx=100, pady=30, height=40, anchor=tkinter.S)
lab_3.pack(side=tkinter.LEFT)
 
# 设置按钮（同意或者不同意）
yes = tkinter.Button(frame_1, text='同意')
no = tkinter.Button(frame_1, text='不同意')
yes.place(relx=0.1, rely=0.9)
no.place(relx=0.5, rely=0.9)
 
# 第二页，老板同意离职了，我们应该谢谢他
frame_2 = tkinter.Frame(root)
# 设置文本
tkinter.Label(frame_2, text='我就知道\n\n你会同意的\n\n现在你就是我的人了\n\n执子之手,与子偕老!!!',
              font=('宋体', 15),
              height=200,
              fg='red',
              padx=60).pack()
tkinter.Button(frame_2, text='同意', command=root.quit).place(relx=0.8, rely=0.9)
 
# 跳转第二页后需要把第一页销毁
def sure():
    # 销毁第一页pack_forget()销毁函数
    frame_1.pack_forget()
    # 布局第二页
    frame_2.pack()
 
# 点击同意才能跳转至第二页   command调用函数
yes.config(command=sure)
 
 
# 做一个不能点击不同意按钮，按钮会到处跑
def move(event):
    no.place(relx=random.uniform(0.05, 0.95), rely=random.uniform(0.05, 0.95))
 
# 需要捕捉到关闭窗口，不允许他点击
def no_exit():
    messagebox.showwarning(title='我警告你，别点我!',
                           message='不允许关闭，小心你的爪子，赶快给我同意')
 
root.protocol('WM_DELETE_WINDOW', no_exit)
 
no.bind('<Enter>', move)
 
# 阻止最小化
def on_focus_out(event):
    root.update()
    root.deiconify()

# 监听窗口焦点的变化
root.bind("<FocusOut>", on_focus_out)
root.mainloop()
