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

@Time      :2022/7/21 12:09

@Author    :Guan_jh

@Email     :guan_jh@qq.com

@Describe  :
'''

# -*- coding: utf-8 -*-

import wx
import wx.adv


class FolderBookmarkTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = 'icon.ico'
    TITLE = '测试系统托盘图标'

    MENU_ID1, MENU_ID2 = wx.NewIdRef(count=2)

    def __init__(self):
        super().__init__()

        # 设置图标和提示
        self.SetIcon(wx.Icon(self.ICON), self.TITLE)

        # 绑定菜单项事件
        self.Bind(wx.EVT_MENU, self.onOne, id=self.MENU_ID1)
        self.Bind(wx.EVT_MENU, self.onExit, id=self.MENU_ID2)

    def CreatePopupMenu(self):
        '''生成菜单'''

        menu = wx.Menu()
        # 添加两个菜单项
        menu.Append(self.MENU_ID1, '弹个框')
        menu.Append(self.MENU_ID2, '退出')
        return menu

    def onOne(self, event):
        wx.MessageBox('111')

    def onExit(self, event):
        wx.Exit()


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__()
        FolderBookmarkTaskBarIcon()


class MyApp(wx.App):
    def OnInit(self):
        MyFrame()
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

