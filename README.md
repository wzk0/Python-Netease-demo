# Python-Netease-demo

**项目已经不再（懒得）更新（重构）了！**

> 第一个Python小项目——调用了网易云API以获取多个信息.(虽然项目很菜但是`README`还是要写好的！)

## 安装(或者可以称为"获取"):

```
wget https://raw.githubusercontent.com/wzk0/Python-Netease-demo/main/%E7%BD%91%E6%98%93%E4%BA%91.py
```

或者

```
git clone https://github.com/wzk0/Python-Netease-demo.git
```

(内存不够删除一下`README.md`和`LICENSE`即可🌚)

## 依赖:

> 需要安装`requests`，`wget`插件

```
pip3 install requests

pip3 install wget
```

或者

```
pip install -r requirements.txt
```

> 如果有播放需求，则需要安装`sox`播放器(`在线播放`还需安装wget):

```
pkg install sox
```

或者

```
apt install sox
```

综上所述，你可以执行以下两种命令之一来安装此程序的完整版:

1. 

```
apt upgrade && apt update
apt install wget python sox -y
wget https://raw.githubusercontent.com/wzk0/Python-Netease-demo/main/%E7%BD%91%E6%98%93%E4%BA%91.py
pip3 install requests wget
python3 网易云.py
```

2. 

```
apt upgrade && apt update
apt install wget python git sox -y
git clone https://github.com/wzk0/Python-Netease-demo.git
pip3 install -r requirements.txt
python3 网易云.py
```

## 启动：


```python
python3 网易云.py
```

## 支持的功能:

![如图所示](https://raw.githubusercontent.com/wzk0/photo/main/Screenshot_2021-12-11-14-16-05-44.jpg)

以及

* 一键更新功能(输入`update`)

## 流程:

1. 进入后，会先检测是否有`cookie.txt`(登陆凭证)和`music`文件夹(音频储存)，如果没有，会创建并在`cookie.txt`中写入一个`cookie模板`；
2. 读取`cookie.txt`并`json编码`一下，保存为`cookies`变量
3. 根据不同的序号进行不同的反馈，请求时携带`cookies`；
4. 反馈后自动重启，用了很不靠谱的`os.system("python3 网易云.py")`；

## 相关:

[Node.js版网易云API](https://github.com/Binaryify/NeteaseCloudMusicApi)
