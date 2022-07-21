# DesktopWidget
## 在桌面上生成一个小组件，可以显示当前的热点信息

### 准备工作

文件架中包括如下四部分

![image-20220721140726431](F:\Python\Desktopwidget\ReadMe.assets\image-20220721140726431.png)

images为图片资源

config.json为默认配置

desktopwidget.exe为主要运行文件

icon.ico是系统文件

**请保证上述四个文件存在**

### 运行中

系统状态栏出现

![image-20220721140649558](F:\Python\Desktopwidget\ReadMe.assets\image-20220721140649558.png)

程序开始运行，若是首次运行加载时间为15s，随后桌面出现

![image-20220721140819333](F:\Python\Desktopwidget\ReadMe.assets\image-20220721140819333.png)

软件运行成功

### 说明

通过点击翻页按钮来获取不同信息，若是出现如下信息：

![image-20220721140925301](F:\Python\Desktopwidget\ReadMe.assets\image-20220721140925301.png)

可以跳过，下次启动将不会再次加载该数据。

### 关于配置

修改弹出窗口大小，弹出位置等请修改根目录下的config.json文件中的

```json
  "widget_width": 350,
  "widget_height": 550,
  "widget_postion_width": 1570,
  "widget_postion_height": 15,
```

默认打开请修改(为了保证不会出错，请确保page_num中的值在UserConfig.ini)中存在

```json
 "page_num": 0,
```

UserConfig.ini中保存了热榜信息，具体请对照Help.txt中填写