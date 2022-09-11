# 基于网易云API的终端网易云

> 当然,指的是[Node.js版网易云API](https://github.com/Binaryify/NeteaseCloudMusicApi)

> 这是一个尚未完工的项目!

---

## 特点

* 支持登录
* 不需要打开花里胡哨的网页,或是卡顿的程序;
* 信息量大,全
* 自定义度极高
* 拥有下载/歌词/本地操作等功能
* 可调用的封装好的API
* 详细的代码注释
* 美观

---

## 效果

![1](https://raw.githubusercontent.com/wzk0/photo/main/202209111451899.png)

![2](https://raw.githubusercontent.com/wzk0/photo/main/202209111452097.png)

![3](https://raw.githubusercontent.com/wzk0/photo/main/202209111452200.png)

![4](https://raw.githubusercontent.com/wzk0/photo/main/202209111454696.png)

![5](https://raw.githubusercontent.com/wzk0/photo/main/202209111454806.png)

---

## 安装

### 前提：

你需要一个有`Python`环境的`Linux`终端(各种各样的发行版和Termux都是可以的!)

请确保你的电脑上安装有`python3`,`wget`,`git`.

### 如果你只想快速开始:

clone此仓库:
```
git clone https://github.com/wzk0/Python-Netease-demo
```

#### 必选:

安装`requests`模块:
```
pip3 install requests
```

安装`pyyaml`模块:
```
pip3 install pyyaml
```

---

#### 可选:

* 要使用`播放器`功能需安装:

`wget`(用于下载),`sox`(用于终端播放)和`libsox-fmt-all`(处理音乐头文件)

安装方法:

```
sudo apt install wget libsox-fmt-all sox -y
```

(其他发行版请自行更换包管理器)

---

随后编辑配置文件:
```
nano src/conf.yaml
```

可以使用了!

---

## 用法

0. 根据菜单(如图所示)输入序号进行选择:

![主页面](https://raw.githubusercontent.com/wzk0/photo/main/202209111451899.png)

1. 本地会生成一个结构如下的文件树来保存数据:

```
.
├── 本地歌单
│   └── hello-world ##本地歌单名
├── 歌词
│   └── K-forest-Find_Me.txt    ##歌词文件
├── 列表
│   └── 911    ##列表文件
└── 音乐
    └── K-forest-Find_Me.mp3    ##音频文件
```

`列表`和`本地歌单`不一样的地方是`列表储存的是网易云歌单内的歌曲ID,以明文保存在本地,可以操作此文件进行下载或者在线播放等功能;本地歌单储存的是本地被标记的音频文件的hash值,只能进行播放或删除等文件操作`.

---

### 如果你想开发:

项目树状图:
```
.
├── main.py	##主程序
├── player_main.py ##本地播放器
└── src
    ├── api.py	##API模型
    ├── conf.yaml	##配置文件
    ├── cookies.json	##cookies存放
    ├── __init__.py	##证明文件
    ├── player.py	##播放器及其他
    └── read.py		##读取配置和检查
```

由于我比较懒,加上之前那个本地播放器功能问题实在是太多,所以我直接复制了[另一个项目](https://github.com/wzk0/terminal-player)的东西过来...

---

## 相关

由于我没有服务器,所以请自行寻找API服务器(我调试的时候用的是手机跑API,内网使用)

API功能 - [网易云音乐 Node.js API service](https://github.com/Binaryify/NeteaseCloudMusicApi)

终端播放器功能 - [一个根据文件hash操作的,基于sox或cvlc的终端播放器.](https://github.com/wzk0/terminal-player)