#!/usr/bin/python3
# -*- coding: UTF-8 -*-

##定义一个懒得每次都输入的p
def p(str):
  print(str)

##导入这些模块
import time
import requests
import json
import os
import wget
import sys

##这里填入API服务器
llink = "https://autumnfish.cn"

## 备用: http://139.59.227.215:3000
## 备用: http://10.194.154.116:3000
## 备用: https://autumnfish.cn
## 备用: http://iwenwiki.com:3000
## 备用: http://119.45.25.73
## 备用: http://148.100.79.209:3000

##检测是否有cookie存在，不存在则创建并写入模板
filename = 'cookie.txt'
if not os.path.exists(filename):
  os.system("touch cookie.txt")
  with open('cookie.txt', 'w') as f:
    f.write("NMTID=xxx; MUSIC_U=xxx; remember_me=true; csrf=xxx")
  p("\033[31m\n未登陆！已创建临时cookie，保存在cookie.txt中！\033[0m")

##检测是否有music文件夹存在，不存在则创建
filename = 'music'
if not os.path.exists(filename):
  os.system("mkdir music")

##读取cookie
f=open(r'cookie.txt','r')
cookies={}
for line in f.read().split(';'):
  name,value=line.strip().split('=',2)
  cookies[name]=value

##定义一个懒得每次都请求的req
def req(url):
  r = requests.get(url,cookies=cookies)
  global temp
  temp = json.loads(r.text)

##定义输入的类
class 输入(object):

##类的属性
  def __init__(self,num):
    self.num=num

##具体操作

##更新
  def update(self):
    url = "https://raw.githubusercontent.com/wzk0/Python-Netease-demo/main/%E7%BD%91%E6%98%93%E4%BA%91.py"
    r = requests.get(url)
    with open('网易云.py', 'w') as f:
      f.write(r.text)
    act = "chmod +x 网易云.py"
    os.system(act)
    p("\033[36m更新完啦！现在你可以通过 \033[0m\033[31m./网易云.py \033[0m\033[36m来重启程序！\033[0m")

##登陆
  def login(self):
    phone = input("\033[36m请输入手机号码:\033[0m")
    password = input("\033[36m请输入密码:\033[0m")
    url = llink + "/login/cellphone?phone=" + phone +"&password=" + password
    p("\033[31m\n请复制下面这段链接并粘贴到Alook浏览器，然后通过它自带的工具箱功能获取此链接的cookie，并保存到cookie.txt文件中(或者通过F12抓取cookie)\n\033[0m")
    p(url)
    p("\033[34m\n这是Alook浏览器的蓝奏云下载地址:\nhttps://wangzhuoke.lanzoul.com/itBPEy74rpc 密码：666\n\033[0m")
    p("\033[36m\n如果不想下载的话，可以按照下面的方法:\033[0m")
    req(url)
    temp = str(temp['cookie'])
    p("\n\033[31m这是cookie(未删减)，请复制并打开cookie.txt:\033[m\n")
    p(temp)
    p("\n\033[36m然后将其删减修改为这种格式:(是我太菜了)\n\033[m")
    p("\033[31mNMTID=xxx; MUSIC_U=xxx; remember_me=true; csrf=xxx \033[0m")

##退出
  def quit(self):
    p("\033[36mBye*╭︎( ˙º˙)╯︎*\033[0m")
    os._exit(0)

##歌词
  def lyric(self):
    id = input("\033[36m请输入歌曲ID:\033[0m")
    p("\033[31m歌词来啦！\033[0m\n")
    url = llink + "/lyric?id=" + id
    req(url)
    p(temp['lrc']['lyric'])

##获取
  def get(self):
    id = input("\033[36m请输入歌曲ID:\033[0m")
    p("\033[31m直链来啦！\033[0m\n")
    url = llink + "/song/url?id=" + id
    req(url)
    urll = llink + "/song/detail?ids=" +id
    rr = requests.get(urll,cookies=cookies)
    tem = json.loads(rr.text)
    tem = tem['songs'][0]
    ar = tem['ar'][0]
    al =tem['al']
    p("\033[36m关于这首歌的信息:\n\033[0m\n歌曲名: \033[36m" + tem['name'] + "\033[0m")
    p("\033[31m 歌曲ID: \033[0m" + str(tem['id']))
    p("歌手名: \033[36m" + ar['name'] + "\033[0m")
    p("\033[31m 歌手ID: \033[0m" + str(ar['id']))
    p("所属专辑: \033[36m" + al['name'] + "\033[0m")
    p("\033[31m 专辑ID: \033[0m " + str(al['id']))
    p("\033[34m—————————————————\033[0m")
    p("\033[36m高品质临时链接:\033[0m")
    p(temp['data'][0]['url'])
    p("\033[34m—————————————————\033[0m")
    p("\033[36m永久直链:\033[0m")
    p("https://music.163.com/song/media/outer/url?id=" + id)
    p("\033[34m—————————————————\033[0m\n")
    p("\033[36m0) 继续     1) 下载 \n\n2) 在线听   3) 下载并播放\n")
    p("\033[34m—————————————————\033[0m\n")
    choooses = input("\033[36m请输入序号:\033[0m")
    if choooses == "0":
      os.system("python3 网易云.py")
    if choooses == "1":
      ur = llink + "/song/detail?ids=" +id
      rr = requests.get(ur,cookies=cookies)
      tem = json.loads(rr.text)
      name = tem['songs'][0]['name']
      ar = tem['songs'][0]['ar'][0]['name']
      name = name + " - " + ar + ".mp3"
      name = ''.join(name.split())
      p("\033[36m\n下载进度:\033[0m")
      realname = name
      fn = wget.download(temp['data'][0]['url'],realname)
      mv = "mv " + realname + " music"
      os.system(mv)
      p("\n\n\033[36m歌曲已下载！名称为 \033[0m./music/" + realname)
      p("\n\033[36m是/否收藏?\033[0m")
      like = input("\033[36my/n:\033[0m")
      if like == "y":
        url = llink + "/like?id=" + id
        req(url)
        if temp['code'] == 200:
          p("\n\033[31m收藏成功啦！૧(●´৺`●)૭")
        else:
          p("\n\033[31m收藏失败︎了..不然你再试试?")
    if choooses == "2":
      action = "nohup play " + temp['data'][0]['url'] + "&"
      os.system(action)
      time.sleep(2)
      p("\n\033[36m是/否下载?\033[0m")
      download = input("\033[36my/n:\033[0m")
      if download == "y":
        ur = llink + "/song/detail?ids=" +id
        rr = requests.get(ur,cookies=cookies)
        tem = json.loads(rr.text)
        name = tem['songs'][0]['name']
        ar = tem['songs'][0]['ar'][0]['name']
        name = name + " - " + ar + ".mp3"
        name = ''.join(name.split())
        p("\033[36m\n下载进度:\033[0m")
        realname = "./music/" + name
        fn = wget.download(temp['data'][0]['url'],name)
        mv = "mv " + name + " music"
        os.system(mv)
        p("\n\n\033[36m歌曲已下载！名称为: \033[0m" + realname)
        p("\n\033[36m是/否收藏?\033[0m")
        like = input("\033[36my/n:\033[0m")
        if like == "y":
          url = llink + "/like?id=" + id
          req(url)
        if temp['code'] == 200:
          p("\n\033[31m收藏成功啦！૧(●´৺`●)૭")
        else:
          p("\n\033[31m收藏失败了..不然你再试试?")
    if choooses == "3":
      ur = llink + "/song/detail?ids=" +id
      rr = requests.get(ur,cookies=cookies)
      tem = json.loads(rr.text)
      name = tem['songs'][0]['name']
      ar = tem['songs'][0]['ar'][0]['name']
      name = name + " - " + ar + ".mp3"
      name = ''.join(name.split())
      p("\033[36m\n下载进度:\033[0m")
      realname = "./music/" + name
      fn = wget.download(temp['data'][0]['url'],name)
      mv = "mv " + name + " music"
      os.system(mv)
      p("\n\n\033[36m歌曲已下载！名称为: \033[0m" + realname)
      action = "nohup play music/" + name + "&"
      os.system(action)
      time.sleep(2)
      p("\n\033[36m是/否收藏?\033[0m")
      like = input("\033[36my/n:\033[0m")
      if like == "y":
        url = llink + "/like?id=" + id
        req(url)
        if temp['code'] == 200:
          p("\n\033[31m收藏成功啦！૧(●´৺`●)૭")
        else:
          p("\n\033[31m收藏失败了..不然你再试试?")


  def test(self):
    print('你输入了:%s'%(self.num))

##收藏
  def like(self):
    id = input("\033[36m请输入歌曲ID:\033[0m")
    url = llink + "/like?id=" + id
    req(url)
    if temp['code'] == 200:
      p("\n\033[31m收藏成功啦！૧(●´৺`●)૭")
    else:
      p("\n\033[31m收藏失败了..不然你再试试?")

##歌手热门
  def singer(self):
    id = input("\033[36m请输入歌手ID:\033[0m")
    limit = input("\033[36m取出数量:\033[0m")
    url = llink + "/artist/songs?id=" + id + "&limit=" + limit
    req(url)
    temp = temp['songs']
    for name in temp:
      p("\n歌名: \033[31m" + name['name'] + "\033[0m")
      p(" \033[34m歌曲ID: \033[0m" + str(name['id']),end="\n\n")

##歌曲详细信息
  def detail(self):
    ids = input("\033[36m请输入歌曲ID:\033[0m")
    url = llink + "/song/detail?ids=" +ids
    req(url)
    temp = temp['songs'][0]
    ar = temp['ar'][0]
    al =temp['al']
    p("\n歌曲名: \033[36m" + temp['name'] + "\033[0m")
    p("\033[31m 歌曲ID: \033[0m" + str(temp['id']))
    p("歌手名: \033[36m" + ar['name'] + "\033[0m")
    p("\033[31m 歌手ID: \033[0m" + str(ar['id']))
    p("所属专辑: \033[36m" + al['name'] + "\033[0m")
    p("\033[31m 专辑ID: \033[0m " + str(al['id']))

##收藏信息
  def liked(self):
    do = "/user/account"
    url = llink + do
    req(url)
    uid = str(temp['account']['id'])
    like = llink + "/likelist?uid=" + uid
    rr = requests.get(like,cookies=cookies)
    tem = json.loads(rr.text)
    tem = tem['ids']
    p("\033[36m接下来的过程比较漫长...如果想终止请输入\033[0m\033[36mCtrl C\n\033[0m")
    for te in tem:
      url = llink + "/song/detail?ids=" + str(te)
      req(url)
      temp = temp['songs'][0]
      ar = temp['ar'][0]
      al =temp['al']
      try:
        p("\n歌曲名: \033[36m" + temp['name'] + "\033[0m")
        p("\033[31m 歌曲ID: \033[0m" + str(temp['id']))
        p("歌手名: \033[36m" + ar['name'] + "\033[0m")
        p("\033[31m 歌手ID: \033[0m" + str(ar['id']))
        p("所属专辑: \033[36m" + al['name'] + "\033[0m")
        p("\033[31m 专辑ID: \033[0m " + str(al['id']))
      except KeyboardInterrupt:
        p("\n\033[31m已停止！\033[0m")

##日推
  def daily(self):
    t = time.localtime()
    p("\n\033[31m" + str(t.tm_year) + "年" +  str(t.tm_mon) + "月" + str(t.tm_mday) + "日" + "的日推来啦！\033[0m\n")
    url = llink + "/recommend/songs"
    req(url)
    for name in temp['data']['dailySongs']:
      p("歌名: " + "\033[31m" + name['name'])
      p(" \033[36m歌曲ID: \033[0m" + str(name['id']))
      p("歌手名: " + "\033[31m" + name['ar'][0]['name'])
      p(" \033[36m歌手ID: \033[0m" + str(name['ar'][0]['id']),end="\n\n")

##个人信息
  def me(self):
    p("\033[36m\n1) 账户信息  2) 收藏信息\033[0m")
    do = input("\033[36m\n请输入序号:\033[0m")
    if do == "1":
      do = "/user/account"
      url = llink + do
      req(url)
      p("\033[31m\n你好啊！\033[0m" + str(temp['profile']['nickname']) + "\033[31m (⁎⁍̴̛͂▿⁍̴̛͂⁎)*✲ﾟ*\033[0m")
      p("\033[34m—————————————————\033[0m")
      p("\033[36m我的ID: \033[0m" + str(temp['account']['id']))
      p("\033[34m—————————————————\033[0m")
      p("\033[36m我的头像:\033[0m\n" + str(temp['profile']['avatarUrl']))
      p("\033[34m—————————————————\033[0m")
      p("\033[36m我的背景:\033[0m\n" + str(temp['profile']['backgroundUrl']))
      p("\033[34m—————————————————\033[0m")
      p("\033[36m我的个人简介:\033[0m\n" + str(temp['profile']['signature']))
      p("\033[34m—————————————————\033[0m\n")
      vip = str(temp['account']['vipType'])
      if vip == "0":
        p("\033[36m诶，你不是会员诶 վ'ᴗ' ի")
    if do == "2":
      do = "/user/subcount"
      url = llink + do
      req(url)
      p("\n\033[34m—————————————————\033[0m")
      p("收藏的电台数:" + str(temp['djRadioCount']))
      p("\033[34m—————————————————\033[0m")
      p("收藏的MV数:" + str(temp['mvCount']))
      p("\033[34m—————————————————\033[0m")
      p("收藏的歌手数:" + str(temp['artistCount']))
      p("\033[34m—————————————————\033[0m")
      p("创建的歌单数:" + str(temp['createdPlaylistCount']))
      p("\033[34m—————————————————\033[0m")
      p("收藏的歌单数:" + str(temp['subPlaylistCount']))
      p("\033[34m—————————————————\033[0m")
      p("\n\033[36m0) 继续      1) 查看收藏歌手详情\n\n2) 查看收藏MV详情\n\033[0m")
      ty = input("\033[36m请输入序号:\033[0m")
      if ty == "1":
        url = llink + "/artist/sublist"
        req(url)
        temp = temp['data']
        for name in temp:
          p("\n\033[36m歌手名: \033[0m" + name['name'] + "\n\033[36m ID: \033[0m" + "\033[31m" + str(name['id']) + "\033[0m" + "\033[0m", end = "\n")
        p("\n")
        os.system("python3 网易云.py")
      if ty == "2":
        url = llink + "/mv/sublist"
        req(url)
        temp = temp['data']
        for title in temp:
          p("\033[36mMV名称: \033[0m" + title['title'] + "\n\033[36m MV作者: \033[0m" + title['creator'][0]['userName'] + "\n\033[36m作者ID: \033[0m\033[31m" + str(title['creator'][0]['userId']) + "\n\033[0m\033[36m" + "MVID: \033[0m\033[31m" + str(title['vid']),end = "\n\n")
        p("\n")
        os.system("pytho3n 网易云.py")

##签到
  def signin(self):
    url = llink + "/daily_signin"
    req(url)
    if temp['code'] == 200:
       p("\033[31m\n每日签到成功！૧(●´৺`●)૭\033[0m")
    if temp['code'] == -2:
      p("\033[31m\n你已经签到过啦（ '▿ ' ）\033[0m")
    if temp['code'] == 301:
      p("\033[31m\n没登陆你签到个啥。。\033[0m")
    urll = llink + "/yunbei/sign"
    rr = requests.get(urll,cookies=cookies)
    tem = json.loads(rr.text)
    if tem['code'] == 200:
      p("\033[31m\n云贝签到成功！૧(●´৺`●)૭\033[0m")

##搜索
  def search(self):
    word = input("\033[36m请输入关键词:\033[0m")
    time = input("\033[36m取出数量:\033[0m")
    p("\033[31m结果来啦！多帮你查了一首噢(๑ت๑)\033[0m\n")
    time = int(time)
    limit = time + 1
    limit = str(limit)
    url = llink + "/search?keywords=" + word + "&limit=" + limit + "&type=1"
    req(url)
    time = int(time)
    try:
      while 0 <= time:
        time = int(time)
        t = time + 1
        t = str(t)
        time = int(time)
        p("歌曲名称: \033[31m" + str(temp['result']['songs'][time]['name'])+ "\033[0m")
        p("\033[34m  歌曲ID: \033[0m" + str(temp['result']['songs'][time]['id']))
        p("歌手: \033[31m" + str(temp['result']['songs'][time]['artists'][0]['name']) + "\033[0m")
        p("  \033[34m歌手ID: \033[0m" + str(temp['result']['songs'][time]['artists'][0]['id']))
        p("专辑名称: \033[31m" + str(temp['result']['songs'][time]['album']['name']) + "\033[0m")
        p("  \033[34m专辑ID: \033[0m" + str(temp['result']['songs'][time]['album']['id']) + "\n")
        time -= 1
    except IndexError and KeyError:
      p("\033[36m一次性获取太多啦！(或者这首歌没有那么多版本)\033[0m")

##MV
  def mv(self):
    id = input("\033[36m请输入MV的ID:\033[0m")
    url = llink + "/mv/url?id=" + id
    req(url)
    p("\033[31mMV来啦！\033[0m")
    p(temp['data']['url'])

##评论
  def talk(self):
    id = input("\033[36m请输入资源ID:\033[0m")
    p("\033[36m\n0: 歌曲，1: mv，2: 歌单，3: 专辑，4: 电台，5: 视频\033[0m")
    type = input("\033[36m请输入此资源类型的序号:\033[0m")
    time = input("\033[36m取出数量:\033[0m")
    time = int(time)
    limit = time + 1
    limit = str(limit)
    p("\033[31m热评来啦！\033[0m\n")
    url = llink + "/comment/hot?id=" + id + "&type=" + type + "&limit=" + limit
    req(url)
    try:
      time = int(time)
      while 0 <= time:
        time = int(time)
        p("\033[37;45m" + str(temp['hotComments'][time]['user']['nickname']) + "\033[0m" + "\033[36m 的热评:\033[0m")
        p("\033[30;47m" + temp['hotComments'][time]['content'] + "\033[0m")
        p("\033[31m点赞数: \033[0m" + str(temp['hotComments'][time]['likedCount']) + "\n")
        time = int(time)
        time -= 1
    except IndexError:
        p("\033[36m一次性得不到这么多评论啦(或者这首歌评论很少)վ'ᴗ' ի")

##热搜
  def hot(self):
    url = llink + "/search/hot/"
    req(url)
    p("\033[31m热搜来啦！\033[0m")
    time = 9
    while 0 <= time:
      p("\033[34m———————————\033[0m")
      time = int(time)
      t = time + 1
      t = str(t)
      time = int(time)
      p("\033[36m第\033[0m" + t + "\033[36m名: \033[0m" + str(temp['result']['hots'][time]['first']))
      time = int(time)
      time -= 1

##歌手信息
  def message(self):
    id = input("\033[36m请输入歌手ID:\033[0m")
    url = llink + "/artists?id=" + id
    req(url)
    p("\033[34m—————————\033[0m")
    p(temp['artist']['briefDesc'])

##简陋的主页面
p("\n\n\n\033[34m————————————————————————\033[0m")
p("\033[36m网易云辅助demo！(´◊ω◊｀)\033[0m")
p("\033[34m————————————————————————\n\033[0m")
p("\033[36m由便当手打制作！٩(๑ᵒ̴̶̷͈᷄ᗨᵒ̴̶̷͈᷅)و\033[0m")
p("\n\033[36m您当前的API服务器为:\033[0m" + llink + "\n如需更换，请\033[31m修改llink的值\033[0m！")
p("\033[34m-----------------------------------------------\033[0m")
p("\n\033[32m0)\033[0m \033[36m登陆(输入以查看登陆方法说明)\033[0m\n\n\033[32m1)\033[0m \033[36m获取歌曲\033[0m         \033[32m2)\033[0m \033[36m获取歌词\033[0m\n\n\033[32m3)\033[0m \033[36m搜索\033[0m             \033[32m4)\033[0m \033[36m获取MV\033[0m\n\n\033[32m5)\033[0m \033[36m获取热评\033[0m         \033[32m6)\033[0m \033[36m获取当前热搜\033[0m\n\n\033[32m7)\033[0m \033[36m获取歌手信息\033[0m     \033[32m8)\033[0m \033[36m签到(登陆可用)\n\033[0m\n\033[32m9)\033[0m \033[36m个人中心\033[0m\033[32m         10)\033[0m \033[36m获取日推\033[0m\n\033[32m\n11) \033[0m\033[36m我喜欢\033[0m          \033[32m12) \033[0m\033[36m歌曲详情\033[0m\n\n\033[32m13) \033[0m\033[36m获取歌手热门\033[0m    \033[32m14)\033[0m \033[36m收藏音乐(这是一个动词)\n\033[0m")
p("\033[34m-----------------------------------------------\033[0m")
num = input ("\033[36m\n请输入序号:\033[0m")

##把输入的数字作为类并操作
if num=="quit":
  num=输入(num)
  num.quit()

if num=="update":
  num=输入(num)
  num.update()

if num=="0":
  num=输入(num)
  num.login()

if num=="1":
  num=输入(num)
  num.get()

if num=="2":
  num=输入(num)
  num.lyric()

if num=="3":
  num=输入(num)
  num.search()

if num=="4":
  num=输入(num)
  num.mv()

if num=="5":
  num=输入(num)
  num.talk()

if num=="6":
  num=输入(num)
  num.hot()

if num=="7":
  num=输入(num)
  num.update()

if num=="8":
  num=输入(num)
  num.signin()

if num=="9":
  num=输入(num)
  num.me()

if num=="10":
  num=输入(num)
  num.daily()

if num=="11":
  num=输入(num)
  num.liked()

if num=="12":
  num=输入(num)
  num.detail()

if num=="13":
  num=输入(num)
  num.singer()

if num=="14":
  num=输入(num)
  num.message()

##是否重启
re = input("\033[35m\n输入1以继续获取；0为退出程序(๑ت๑):\033[0m")
if re == "1":
  os.system("python3 网易云.py")
if re == "0":
  num.quit()
