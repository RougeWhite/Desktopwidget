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
@FileName  :GetData.py

@Time      :2022/7/20 10:08

@Author    :Guan_jh

@Email     :guan_jh@qq.com

@Describe  :
'''
import requests
from bs4 import BeautifulSoup
import re
import os
import sys
import json
import tkinter as tk
from DragWindow import DragWindow
import math
import webbrowser

def getHTML(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except Exception as err:
        return str(err)

def getData(soup):
    #  获取链接
    hrefList = gethrefData(soup)
    Result_List = []
    # 分析数据
    Title_items = soup.find_all("div", class_="cc-cd")
    for Title_item in Title_items:
        tmp_sum_list = []
        tmp_b_list = []
        r_paihang_list = []
        temp = Title_item.text.strip()
        tmplist = temp.split("\n")
        # 去空
        paihang_list = list(filter(not_empty, tmplist))
        # 加入标题
        tmp_b_list.append(paihang_list[0])
        # 加入名称
        tmp_b_list.append(paihang_list[1])
        # 移除标题
        paihang_list.pop(0)
        # 移除名称
        paihang_list.pop(0)
        # 移除结尾无效值
        paihang_list.pop(len(paihang_list)-1)
        # 移除结尾时间
        paihang_list.pop(len(paihang_list)-1)
        # 重新计算分布
        if (paihang_list[len(paihang_list)-3].isdigit()):
            # 将排行list改变成3个一组
            for b in [paihang_list[i:i + 3] for i in range(0, len(paihang_list), 3)]:
                r_paihang_list.append(b)
            # 添加测试总数
            tmp_b_list.append(paihang_list[len(paihang_list) - 3])
        elif(paihang_list[len(paihang_list)-2].isdigit()):
            # 将排行list改变成2个一组
            for b in [paihang_list[i:i + 2] for i in range(0, len(paihang_list), 2)]:
                r_paihang_list.append(b)
            # 添加测试总数
            tmp_b_list.append(paihang_list[len(paihang_list) - 2])

        for k in r_paihang_list:
            try:
                if(len(k[1])>20 and len(k[1])<40):
                    tmplist = list(k[1])
                    tmplist.insert(20, '\n')
                    k[1] = ''.join(tmplist)
                if(len(k[1])>40):
                    tmplist = list(k[1])
                    tmplist.insert(20, '\n')
                    del tmplist[40:len(tmplist)-1]
                    tmplist.append("...")
                    k[1] = ''.join(tmplist)
            except Exception as r:
                print('未知错误 %s' %r)

        # 添加计算总数
        tmp_b_list.append(len(r_paihang_list))
        # 验证总数是否正确
        if(tmp_b_list[2]==str(tmp_b_list[3])):
            tmp_sum_list.append("yes")
            tmp_sum_list.append(tmp_b_list[2])
        else:
            tmp_sum_list.append("no")
            tmp_sum_list.append(tmp_b_list[2])
        # 添加头
        tmp_sum_list.append(tmp_b_list)
        # yes时认为可以获取数据
        if(tmp_sum_list[0]=="yes"):
            list_num = int(tmp_sum_list[1])
            for i in range(list_num):
                r_paihang_list[i].append(hrefList[0])
                hrefList.pop(0)
        else:
            list_num = int(tmp_sum_list[1])
            for i in range(list_num):
                hrefList.pop(0)

        #  将链接放入
        # print(r_paihang_list)

        # 添加详细
        tmp_sum_list.append(r_paihang_list)

        Result_List.append(tmp_sum_list)

    return Result_List

# 非空
def not_empty(s):
    return s and s.strip()

# 获取href数据
def gethrefData(soup):
    href_List = []
    # 分析数据
    href_items = soup.find_all(attrs={"itemid": re.compile(".*")})
    for href_item in href_items:
        temp = href_item['href']
        href_List.append(temp)
    return href_List

# 处理最后结果list
def DealList(data):
    result = []
    # 去除
    num = 0
    for i in data:
        if(i[0]=="yes"):
            i.insert(0, num)
            i.insert(1, i[3][0])
            i.insert(2, i[4][1])
            i.pop(3)
            i.pop(3)
            i.pop(3)
            result.append(i)
            num = num+1
    return result

# 新建文件
def text_create(path, msg):
    f = open(path, 'w')
    f.write(msg)
    f.close()




def Setting(retval,default_setting_filename):

    default_setting_filename_dir = retval + "\\" + default_setting_filename
    if os.path.exists(default_setting_filename_dir):
        # 读取配置文件
        SetJson = loadSet(default_setting_filename_dir)
        User_Setting_filename = SetJson["userconfig"]
        User_setting_filename_dir = retval + "\\" + User_Setting_filename
        #  创建配置文件
        if os.path.exists(User_setting_filename_dir) ^ 1:
            print("正在创建配置文件,请稍后")
            xuanzhong = InIdata(SetJson)
            text_create(User_setting_filename_dir, xuanzhong)
            print("用户配置文件创建完成")
            return SetJson
        else:
            print("用户配置文件存在")
            return SetJson
    else:
        print("code:400 初始化失败:配置文件丢失")
        exit()

# 获取用户设置
def GetUserSet(SetJson):
    Now_Path = os.getcwd()
    UserSetFileName = SetJson["userconfig"]
    Dir_Name = Now_Path+"\\"+UserSetFileName
    f = open(Dir_Name)
    data = f.readlines()
    return data

# 加载系统设置
def loadSet(default_setting_filename_dir):
    with open(default_setting_filename_dir, 'r') as f:
        SetJson = json.load(f)
    return SetJson

# 初始化数据
def InIdata(SetJson):
    Result_List = GetData(SetJson)
    xuanzhong = str(list(range(len(Result_List))))
    return xuanzhong

# 获取数据集合
def GetData(SetJson):
    print("正在获取数据")
    # 获取url
    url = SetJson["url"]
    # 得到网页html
    req = getHTML(url)
    # 对html解析
    Result_List = DealList(getData(BeautifulSoup(req.text, features="html.parser")))
    return Result_List


def UserSet4Data(UserSet,Data_List):
    Result_List = []
    for i in UserSet:
        Result_List.append(Data_List[i])
    return Result_List

def Gui(root,SetJson,Result_List,nowpage,UserSet):
    # 创建Tk对象，Tk代表窗口
    # root = tk.Tk()
    # 设置窗口标题
    # 创建Label对象，第一个参数指定该Label放入root
    # 　导入DragWindow类
    print("当前第"+str(nowpage)+"个，对应的值是"+str(UserSet[nowpage]))
    print(UserSet)
    load_list = Result_List[nowpage]
    des_list = load_list[3]
    widget_width = int(SetJson["widget_width"])
    widget_height = int(SetJson["widget_height"])
    widget_postion_width = int(SetJson["widget_postion_width"])
    widget_postion_height = int(SetJson["widget_postion_height"])

    root.set_window_size(widget_width, widget_height)
    root.set_display_postion(widget_postion_width, widget_postion_height)
    la = tk.Label(root, text="今日热榜",  # 设置文本内容
             justify='left',  # 设置文本对齐方式：左对齐
             anchor='nw',  # 设置文本在label的方位：西北方位
             font=('微软雅黑', 18),  # 设置字体：微软雅黑，字号：18
             fg="white",
             bg="black")
    la.place(x=widget_width * 0.057, y=widget_height * 0.036)
    lb = tk.Label(root, text=load_list[2],  # 设置文本内容
             justify='left',  # 设置文本对齐方式：左对齐
             anchor='nw',  # 设置文本在label的方位：西北方位
             font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.0319)),  # 设置字体：微软雅黑，字号：18
             fg="white",
             bg="black",  # 设置x方向内边距：20
             )
    lb.place(x=widget_width * 0.07, y=widget_height * 0.11)
    if(len(load_list[1])==2):
        title = tk.Label(root, text=load_list[1],  # 设置文本内容
                 justify='left',  # 设置文本对齐方式：左对齐
                 anchor='nw',  # 设置文本在label的方位：西北方位
                 # font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.0205)),  # 设置字体：微软雅黑，字号：18
                 font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.05698)),  # 设置字体：微软雅黑，字号：18
                 fg="red",
                 bg="black",  # 设置x方向内边距：20
                 )
        title.place(x=widget_width*0.7428, y=widget_height*0.05454)
    elif(len(load_list[1])==3):
        title = tk.Label(root, text=load_list[1],  # 设置文本内容
                 justify='left',  # 设置文本对齐方式：左对齐
                 anchor='nw',  # 设置文本在label的方位：西北方位
                 # font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.0205)),  # 设置字体：微软雅黑，字号：18
                 font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.05698)),  # 设置字体：微软雅黑，字号：18
                 fg="red",
                 bg="black",  # 设置x方向内边距：20
                 )
        title.place(x=widget_width*0.6571, y=widget_height*0.05454)
    elif(len(load_list[1]) == 4):
        title = tk.Label(root, text=load_list[1],  # 设置文本内容
             justify='left',  # 设置文本对齐方式：左对齐
             anchor='nw',  # 设置文本在label的方位：西北方位
             # font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.0205)),  # 设置字体：微软雅黑，字号：18
             font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.05698)),  # 设置字体：微软雅黑，字号：18
             fg="red",
             bg="black",  # 设置x方向内边距：20
             )
        title.place(x=widget_width*0.5714, y=widget_height*0.05454)
    elif(len(load_list[1]) == 5):
        title = tk.Label(root, text=load_list[1],  # 设置文本内容
             justify='left',  # 设置文本对齐方式：左对齐
             anchor='nw',  # 设置文本在label的方位：西北方位
             # font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.0205)),  # 设置字体：微软雅黑，字号：18
             font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.05698)),  # 设置字体：微软雅黑，字号：18
             fg="red",
             bg="black",  # 设置x方向内边距：20
             )
        title.place(x=widget_width*0.4857, y=widget_height*0.05454)
    else:
        title = tk.Label(root, text=load_list[1],  # 设置文本内容
                 justify='left',  # 设置文本对齐方式：左对齐
                 anchor='nw',  # 设置文本在label的方位：西北方位
                 # font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.0205)),  # 设置字体：微软雅黑，字号：18
                 font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.05698)),  # 设置字体：微软雅黑，字号：18
                 fg="red",
                 bg="black",  # 设置x方向内边距：20
                 )
        title.place(x=widget_width*0.4, y=widget_height*0.05454)
    if(len(des_list)<10):
        num = len(des_list)
    else:
        num = 10
    lc_list = []
    ml_list = []
    lp_list = []


    for i in range(num):
        error_list = []
        lc = tk.Label(root, text=des_list[i][0],  # 设置文本内容
                 justify='center',  # 设置文本对齐方式：左对齐
                 anchor='nw',  # 设置文本在label的方位：西北方位
                 font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.025)),  # 设置字体：微软雅黑，字号：18
                 fg="yellow",
                 bg="black",
                 )
        lc.place(x=widget_width * 0.09, y=widget_height * 0.182 + widget_height * 0.0727 * i)
        lc_list.append(lc)

        try:
            ml = tk.Label(root, text=des_list[i][1],  # 设置文本内容20字
                          justify='left',  # 设置文本对齐方式：左对齐
                          anchor='nw',  # 设置文本在label的方位：西北方位
                          font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.0205)),  # 设置字体：微软雅黑，字号：18
                          fg="white",
                          bg="black",
                          textvariable=des_list[i][3]
                          )
            ml.place(x=widget_width * 0.17, y=widget_height * 0.182 + widget_height * 0.073 * i)

            ml.bind('<Button>', lambda event: changeColor(event, i))
        except:
            ml = tk.Label(root, text="报错了！无法查看！",  # 设置文本内容20字
                          justify='left',  # 设置文本对齐方式：左对齐
                          anchor='nw',  # 设置文本在label的方位：西北方位
                          font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.0205)),  # 设置字体：微软雅黑，字号：18
                          fg="white",
                          bg="black",
                          textvariable="https://www.baidu.com"
                          )
            error_list.append(UserSet[nowpage])
            error_list = list(set(error_list))


            ml.place(x=widget_width * 0.17, y=widget_height * 0.182 + widget_height * 0.073 * i)

            ml.bind('<Button>', lambda event: changeColor(event, i))
        ml_list.append(ml)

        lp = tk.Label(root, text=des_list[i][2],  # 详细情况
                 justify='left',  # 设置文本对齐方式：左对齐
                 anchor='nw',  # 设置文本在label的方位：西北方位
                 font=('微软雅黑', int(math.sqrt(int(widget_width * widget_height)) * 0.0205)),  # 设置字体：微软雅黑，字号：18
                 fg="white",
                 bg="black",
                 )
        lp.place(x=widget_width * 0.83, y=widget_height * 0.182 + widget_height * 0.073 * i)
        lp_list.append(lp)
    if(len(error_list)==1):
        print("当前页面"+str(nowpage)+"有问题，值是"+str(error_list[0]))
        UserSet,Result_List = WriteUserSet(SetJson, error_list)

    tk.Button(root, text="<<", command=lambda: Pre(root,nowpage,UserSet,Result_List,SetJson,la,lb,lc_list,lp_list,title,ml_list)).place(x=widget_width / 4, y=widget_height * 0.94)
    tk.Button(root, text="退出", command=root.quit).place(x=widget_width / 2, y=widget_height * 0.94)
    tk.Button(root, text=">>", command=lambda: Next(root,nowpage,UserSet,Result_List,SetJson,la,lb,lc_list,lp_list,title,ml_list)).place(x=widget_width / 4 * 3, y=widget_height * 0.94)


def Pre(root,nowpage,UserSet,Result_List,SetJson,la,lb,lc_list,lp_list,title,ml_list):

    la.destroy()
    lb.destroy()
    for lc in lc_list:
        lc.destroy()
    for lp in lp_list:
        lp.destroy()
    title.destroy()
    for ml in ml_list:
        ml.destroy()
    if nowpage == 0:
        page_num = len(UserSet)-1
    else:
        page_num = nowpage-1
    Gui(root,SetJson, Result_List, page_num, UserSet)

def Next(root,nowpage,UserSet,Result_List,SetJson,la,lb,lc_list,lp_list,title,ml_list):
    la.destroy()
    lb.destroy()
    for lc in lc_list:
        lc.destroy()
    for lp in lp_list:
        lp.destroy()
    title.destroy()
    for ml in ml_list:
        ml.destroy()
    if nowpage == len(UserSet) - 1:
        page_num = 0
    else:
        page_num = nowpage + 1
    Gui(root,SetJson, Result_List, page_num, UserSet)



def changeColor(event,j):
    url = str(event.widget['textvariable'])
    print(event.widget['textvariable'])
    webbrowser.open(url, new=0, autoraise=True)

def WriteUserSet(SetJson,error_List):
    Now_Path = os.getcwd()
    user_setting_filename = SetJson["userconfig"]
    User_setting_filename_dir =Now_Path + "\\" + user_setting_filename
    # 获取设置
    UserSet = json.loads(str(GetUserSet(SetJson)).split('\'')[1])
    try:
        UserSet.remove(error_List[0])
    except:
        print("页面已经移除了")
    text_create(User_setting_filename_dir, str(UserSet))
    Result_List = UserSet4Data(UserSet, Data_List)
    return UserSet,Result_List


if __name__ == '__main__':
    #  系统初始化
    Now_Path = os.getcwd()
    default_setting_filename = "config.json"
    default_setting_filename_dir = Now_Path + "\\" + default_setting_filename

    #  Setting
    # 获取系统设置
    SetJson = Setting(Now_Path,default_setting_filename)
    # 获取用户设置
    UserSet = json.loads(str(GetUserSet(SetJson)).split('\'')[1])

    #  获取详细数据
    Data_List = GetData(SetJson)

    #  根据用户配置文件读取数据
    Result_List = UserSet4Data(UserSet, Data_List)

    #  渲染数据到GUI
    root = DragWindow()
    page_num = 0
    Gui(root,SetJson, Result_List, page_num,UserSet)
    root.mainloop()




