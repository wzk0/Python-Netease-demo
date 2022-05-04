# 基于网易云API的终端网易云

> 当然,指的是[Node.js版网易云API](https://github.com/Binaryify/NeteaseCloudMusicApi)

> 这里有两篇自述文件,oldREADME.md里记述的是Version1.0,对应代码只有一个'网易云.py'.已经不再更新它了!

> 这是一个尚未完工的项目!

## 特点

* 不需要打开花里胡哨的网页,或是卡顿的程序;
* 信息量大,全(大概)
* 自定义度极高(可能)
* 拥有下载/歌词等海量(应该)功能
* 可以调用很多(或许)封装好的API模型,进行带有精美前端的二改

## 用法

### 前提：

你需要一个有Python环境的Linux终端(各种各样的发行版和Termux都是可以的!)

### 如果你只想快速开始:

clone此仓库:
'''
git clone https://github.com/wzk0/Python-Netease-demo
'''

安装requests模块:
'''
pip3 install requests
'''

随后编辑配置文件:
'''
nano src/conf.yaml
'''

可以使用了!

如果想使用登录相关的功能,请获得自己的网易云cookies并按照'cookies.json'的格式写入其中.

### 如果你想开发:

项目树状图:
'''
.
├── main.py	##主程序
└── src
    ├── api.py	##API模型
    ├── conf.yaml	##配置文件
    ├── cookies.json	##cookies存放
    ├── __init__.py	##证明文件
    ├── player.py	##播放器及其他
    └── read.py		##读取配置和检查
'''

Sorry...没有写注释,不过代码很简单,除了requests也没导入其他库!

登录功能暂时没做出来,原因是:

1. 网易云现在登录需要验证
2. 明文传输的账号信息不安全

如果你可以做的话请fork!

## 相关

由于我没有服务器,所以请自行寻找API服务器(我调试的时候用的是手机跑API,内网使用)
