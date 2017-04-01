# 爬虫合集 #

## 1.JXNU教务在线爬虫 ##
首先申明一下，此代码仅作学习交流。切勿进行非法用途！
最后要实现的效果图如下：
![实现效果](image\xiaoguo.png)

我们要爬取的数据有学生的学号，姓名，班级，性别，照片。
存放数据的格式约定：
照片的命名方式是：学号.jpg。
然后把 学号，姓名，班级，性别 这四个字段的数据存入，学号.txt的文本文档中。
目录结构效果如上图。

然后说明一下环境。
我在Windows 10下开发的，事实上这个代码在Linux上也可以跑。我已经试过了。所以你在Windows的其他版本或者是Linux环境下编写也是可以的。这是系统的环境，一般问题不大。
语言用的是python，版本是2.7,推荐使用pycharm进行python代码的编写。
还需要python的一些库，例如requests,re,os。其中re是正则表达式库，os用来文件操作的库。都是系统自带的，requests需要安装，如果你有pip，你可以直接在cmd中pip install requests,如果你在Windows上输入这条命令没有用，那是因为你没把pip.exe所在的目录路径加入到系统变量中，cmd自然就检索不到pip.exe。那你要么把该目录加入到系统变量中，要么就在cmd中输入 完整路径\pip install requests。Ok，安装好之后重启下pycharm就可以使用requests库了。好了，环境ok，接下来，我们就可以来写代码了。
Windows 10 安装包 可以到 [http://msdn.itellyou.cn/](http://msdn.itellyou.cn/) 这个网站下载
python 2.7可以到[https://www.python.org/downloads/](https://www.python.org/downloads/)这个网站下载
pycharm可以到[http://www.jetbrains.com/pycharm/](http://www.jetbrains.com/pycharm/)这个网站下载
pycharm 使用教程[http://blog.csdn.net/u013088062/article/details/50100121](http://blog.csdn.net/u013088062/article/details/50100121)
requests安装教程[http://www.zhidaow.com/post/python-requests-install-and-brief-introduction](http://www.zhidaow.com/post/python-requests-install-and-brief-introduction)
正则表达式：[http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html](http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html)
re.findAll()用法：[http://blog.csdn.net/cashey1991/article/details/8875213](http://blog.csdn.net/cashey1991/article/details/8875213)
----------
爬虫呢其实就是从网页源代码中提取我们想要的内容。
那么很显然，你要知道URL是什么，还好，URL一般都是有规律的。比如学号为1308092061的学生，它的信息存储在URL=“http://jwc.jxnu.edu.cn/MyControl/All_Display.aspx?UserControl=All_StudentInfor.ascx&UserType=Student&UserNum=1308092061”的页面中。
那么我们只要枚举学号就可以构造出URL，从而达到了获取所有学生的目的。这里考虑把学生分成三个部分，第一个部分是年级，第二个部分是班级，第三个部分是班级内编号。这样，第一层循环枚举年级，第二层循环枚举班级号，第三层循环枚举班级内号，这样比直接从0000000001枚举到9999999999要高效得多。然后，并不是构造出来的每一个学号都是有效的，如果学号无效我们就break掉第三层循环。
构造好URL，接下来就是要获取URL对应HTML页面的源代码了，那很简单，只要requests.get(URL)就可以获取网页源码了。但是这个URL是登录之后才能访问的，可以用cookies来解决这个问题，你登录成功后有个cookies，你把cookies复制下来就可以模拟浏览器登录了。
怎么获取cookies呢？
利用chrome获取cookies[https://www.zhihu.com/collection/75739883](https://www.zhihu.com/collection/75739883)
获取到cookies后，比如把cookies存在cook变量中。
然后requests.get(URL，cookies=cook)就可获取网页源码了。
然后用正则表达式把想要的内容提取出来就可以了。
先说这么多，看源代码把。