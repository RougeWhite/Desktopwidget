# -*- coding:utf-8 -*-
#                 ____                                       _____  __         
#                /\  _`\                                    /\___ \/\ \        
#                \ \ \L\_\  __  __     __      ___          \/__/\ \ \ \___    
#                 \ \ \L_L /\ \/\ \  /'__`\  /' _ `\           _\ \ \ \  _ `\  
#                  \ \ \/, \ \ \_\ \/\ \L\.\_/\ \/\ \         /\ \_\ \ \ \ \ \ 
#                   \ \____/\ \____/\ \__/.\_\ \_\ \_\        \ \____/\ \_\ \_\
#                    \/___/  \/___/  \/__/\/_/\/_/\/_/  _______\/___/  \/_/\/_/
#                                                      /\______\               
#                                                      \/______/  
'''
@FileName  :test.py

@Time      :2022/7/20 14:43

@Author    :Guan_jh

@Email     :guan_jh@qq.com

@Describe  :
'''

# 导入tkinter库，并设置别名为tk
import tkinter as tk
import math

from DragWindow import DragWindow


def GUI():
    # 创建Tk对象，Tk代表窗口
    # root = tk.Tk()
    # 设置窗口标题
    # 创建Label对象，第一个参数指定该Label放入root
    # 　导入DragWindow类

    widget_width =350
    widget_height = 550
    widget_postion_width =1570
    widget_postion_height =15
    root = DragWindow()
    root.set_window_size(widget_width,widget_height)
    root.set_display_postion(widget_postion_width,widget_postion_height)
    tk.Label(root, text="今日热榜",  # 设置文本内容
             justify='left',  # 设置文本对齐方式：左对齐
             anchor='nw',  # 设置文本在label的方位：西北方位
             font=('微软雅黑', 18),  # 设置字体：微软雅黑，字号：18
             fg="white",
             bg="black").place(x=widget_width*0.057,y=widget_height*0.036)
    tk.Label(root, text="微信",  # 设置文本内容
             justify='left',  # 设置文本对齐方式：左对齐
             anchor='nw',  # 设置文本在label的方位：西北方位
             font=('微软雅黑', int(math.sqrt(int(widget_width*widget_height))*0.0319)),  # 设置字体：微软雅黑，字号：18
             fg="white",
             bg="black",  # 设置x方向内边距：20
             ).place(x=widget_width*0.07, y=widget_height*0.11)
    tk.Label(root, text="十大热门话题",  # 设置文本内容
             justify='left',  # 设置文本对齐方式：左对齐
             anchor='nw',  # 设置文本在label的方位：西北方位
             font=('微软雅黑', int(math.sqrt(int(widget_width*widget_height))*0.0205)),  # 设置字体：微软雅黑，字号：18
             fg="white",
             bg="black",  # 设置x方向内边距：20
             ).place(x=widget_width*0.75, y=widget_height*0.11)
    for i in range(10):
        j=0
        hhh = tk.StringVar().set(str(i))
        tk.Label(root, text=i + 1,  # 设置文本内容
                 justify='left',  # 设置文本对齐方式：左对齐
                 anchor='nw',  # 设置文本在label的方位：西北方位
                 font=('微软雅黑', int(math.sqrt(int(widget_width*widget_height))*0.025)),  # 设置字体：微软雅黑，字号：18
                 fg="white",
                 bg="black",
                 ).place(x=widget_width * 0.09, y=widget_height * 0.182 + widget_height * 0.0727 * i)
        ml = tk.Label(root, text="热门内容呢热门内容呢热门内容呢热门内容呢\n"
                            "热门内容呢热门内容呢热门内容呢热门内容呢...",  # 设置文本内容20字
                 justify='left',  # 设置文本对齐方式：左对齐
                 anchor='nw',  # 设置文本在label的方位：西北方位
                 font=('微软雅黑', int(math.sqrt(int(widget_width*widget_height))*0.0205)),  # 设置字体：微软雅黑，字号：18
                 fg="white",
                 bg="black",
                 textvariable="aaaaaaaaaaaaaaaaaaaaa"
                 )
        ml.place(x=widget_width * 0.17, y=widget_height * 0.182 + widget_height * 0.073 * i)


        ml.bind('<Button>', lambda event:changeColor(event, i))

        tk.Label(root, text="热销1.5w",  # 设置文本内容20字
                 justify='left',  # 设置文本对齐方式：左对齐
                 anchor='nw',  # 设置文本在label的方位：西北方位
                 font=('微软雅黑', int(math.sqrt(int(widget_width*widget_height))*0.0205)),  # 设置字体：微软雅黑，字号：18
                 fg="white",
                 bg="black",
                 ).place(x=widget_width * 0.83, y=widget_height * 0.182 + widget_height * 0.073 * i)
    tk.Button(root, text="退出", command=root.quit).place(x=widget_width/2, y=widget_height*0.94)
    # var = tk.StringVar()
    # w = tk.Label(root, text="Hello Python!", textvariable=var, fg='blue', font=("微软雅黑", 40))
    # var.set("Hello Python!")
    # # 调用pack进行布局
    # w.pack()


    # # 测试用途
    # def onGo():
    #     print("go go go!")
    #     print(var.get())


    # # 测试用途
    # goBtn = tk.Button(text="测试", command=onGo, fg='blue', font=("黑体", 20))
    # goBtn.pack()

    # 启动主窗口的消息循环
    root.mainloop()

def changeColor(event,j):
    print("点击了aa"+str(event)+str(j))
    print(event.widget['textvariable'])

if __name__ == '__main__':
    GUI()

