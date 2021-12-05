#!/usr/bin/python

import requests
import json
import os
import wget

s = "song"
l = "lyric"
se = "search"
m = "mv"
h = "hot"
llink = "https://autumnfish.cn"

## 备用: http://10.194.154.116:3000
## 备用: https://autumnfish.cn
## 备用: http://iwenwiki.com:3000
## 备用: http://119.45.25.73
## 备用: http://148.100.79.209:3000

print("\n\n\n\033[34m————————————————————————\033[0m")
print("\033[36m网易云辅助demo！(´◊ω◊｀)\033[0m")
print("\033[34m————————————————————————\n\033[0m")
print("\033[36m由听话的便当手打制作！٩(๑ᵒ̴̶̷͈᷄ᗨᵒ̴̶̷͈᷅)و\033[0m")
print("\n\033[36m您当前的API服务器为:\033[0m" + llink + "\n如需更换，请\033[31m修改llink的值\033[0m！")
print("\033[34m-----------------------------------------------\033[0m")
print("\n\033[32m0)\033[0m \033[36m登陆(目前没什么卵用(||๐_๐))\033[0m\n\n\033[32m1)\033[0m \033[36m获取歌曲\033[0m         \033[32m2)\033[0m \033[36m获取歌词\033[0m\n\n\033[32m3)\033[0m \033[36m搜索\033[0m             \033[32m4)\033[0m \033[36m获取MV\033[0m\n\n\033[32m5)\033[0m \033[36m获取热评\033[0m         \033[32m6)\033[0m \033[36m获取当前热搜\033[0m\n\n\033[32m7)\033[0m \033[36m获取歌手信息\033[0m\n")
print("\033[34m-----------------------------------------------\033[0m")
type = input ("\033[36m请输入序号:\033[0m")

if type == "0":

  phone = input("\033[36m请输入手机号码:\033[0m")
  password = input("\033[36m请输入密码:\033[0m")
  url = llink + "/login/cellphone?phone=" + phone +"&password=" + password
  r = requests.post(url)
  text = r.text
  temp = json.loads(text)
  if temp['code'] == 200:
    print("\033[36m\n已经成功登陆啦！❛‿˂̵✧\033[0m")
  else:
    print("\033[36m\n不知道什么原因导致登陆失败了...\n请检查密码是否正确 (*꒦ິ⌓꒦ີ)\033[0m")

if type == "1":

  id = input("\033[36m请输入歌曲ID:\033[0m")
  print("\033[31m直链来啦！\033[0m\n")
  url1 = llink + "/song/url?id=" + id
  r = requests.post(url1)
  text = r.text
  temp = json.loads(text)
  print("\033[34m—————————————————\033[0m")
  print("\033[36m高品质临时链接:\033[0m")
  print(temp['data'][0]['url'])
  print("\033[34m—————————————————\033[0m")
  print("\033[36m永久直链:\033[0m")
  print("https://music.163.com/song/media/outer/url?id=" + id)
  print("\033[34m—————————————————\033[0m\n")
  print("\033[36m0) 继续     1) 下载 \n\n2) 在线听   3) 下载并播放\n")
  print("\033[34m—————————————————\033[0m\n")
  chooses = input("\033[36m请输入序号:\033[0m")
  if chooses == "0":
    os.system("python 网易云.py")

  if chooses == "1":
    name = id + ".mp3"
    print("\033[36m\n下载进度:\033[0m")
    fn = wget.download(temp['data'][0]['url'],name)
    print("\n\n\033[36m歌曲已下载！名称为 \033[0m" + fn)

  if chooses == "2":
    action = "play " + temp['data'][0]['url']
    os.system(action)

  if chooses == "3":
    name = id + ".mp3"
    print("\033[36m\n下载进度:\033[0m")
    fn = wget.download(temp['data'][0]['url'],name)
    print("\n\n\033[36m歌曲已下载！名称为: \033[0m" + fn)
    action = "play " + fn
    os.system(action)

elif type == "2":

  id = input("\033[36m请输入歌曲ID:\033[0m")
  print("\033[31m歌词来啦！\033[0m\n")
  url2 = llink + "/lyric?id=" + id
  r = requests.post(url2)
  text = r.text
  temp = json.loads(text)
  print(temp['lrc']['lyric'])

elif type == "3":

  word = input("\033[36m请输入关键词:\033[0m")
  time = input("\033[36m取出数量:\033[0m")
  print("\033[31m结果来啦！多帮你查了一首噢(๑ت๑)\033[0m")
  time = int(time)
  limit = time + 1
  limit = str(limit)
  url3= llink + "/search?keywords=" + word + "&limit=" + limit
  r = requests.post(url3)
  text = r.text
  temp = json.loads(text)

  time = int(time)
  while 0 <= time:
    time = int(time)
    t = time + 1
    t = str(t)
    print("\n\033[0;31;44m \033[0m")
    print("第" + t + "首:")
    time = int(time)
    print("\033[31m##############\033[0m")
    print("\033[34m歌曲名称: \033[0m" + str(temp['result']['songs'][time]['name'])+ "\n")
    print("\033[34m歌曲ID: \033[0m" + str(temp['result']['songs'][time]['id']) + "\n")
    print("\033[34m歌手: \033[0m" + str(temp['result']['songs'][time]['artists'][0]['name']))
    time = int(time)
    time -= 1

elif type == "4":

  id = input("\033[36m请输入MV的ID:\033[0m")
  url = llink + "/mv/url?id=" + id
  r = requests.post(url)
  text = r.text
  temp = json.loads(text)
  print("\033[31mMV来啦！\033[0m")
  print(temp['data']['url'])

elif type == "5":

  id = input("\033[36m请输入资源ID:\033[0m")
  print("\033[36m\n0: 歌曲，1: mv，2: 歌单，3: 专辑，4: 电台，5: 视频\033[0m")
  type = input("\033[36m请输入资源类型的序号:\033[0m")
  time = input("\033[36m取出数量:\033[0m")
  time = int(time)
  limit = time + 1
  limit = str(limit)
  print("\033[31m热评来啦！\033[0m\n")
  url5 = llink + "/comment/hot?id=" + id + "&type=" + type + "&limit=" + limit
  r = requests.post(url5)
  text = r.text
  temp = json.loads(text)

  time = int(time)
  while 0 <= time:
    time = int(time)
    print("\033[0;34;44m————————————————————————————————\033[0m")
    print("\033[36m来自用户:\033[0m" + str(temp['hotComments'][time]['user']['nickname']) + "\033[36m的热评:\033[0m")
    print("\n")
    print(temp['hotComments'][time]['content'])
    print("\n")
    print("\033[31m点赞数:\033[0m" + str(temp['hotComments'][time]['likedCount']) + "\n")
    time = int(time)
    time -= 1

elif type == "6":
  urlll = llink + "/search/hot/"
  r = requests.post(urlll)
  text = r.text
  temp = json.loads(text)
  print("\033[31m热搜来啦！\033[0m")
  time = 9
  while 0 <= time:
    print("\033[34m———————————\033[0m")
    time = int(time)
    t = time + 1
    t = str(t)
    time = int(time)
    print("\033[36m第\033[0m" + t + "\033[36m名: \033[0m" + str(temp['result']['hots'][time]['first']))
    time = int(time)
    time -= 1

if type == "7":

  id = input("\033[36m请输入歌手ID:\033[0m")
  url = llink + "/artists?id=" + id
  r = requests.post(url)
  text = r.text
  temp = json.loads(text)
  print("\033[34m—————————\033[0m")
  print(temp['artist']['alias'][0])
  print(temp['artist']['briefDesc'])

re = input("\033[35m\n输入1以继续获取；0为退出程序(๑ت๑):\033[0m")

if re == "1":
  os.system("python 网易云.py")
if re == "0":
  print("\033[36mBye*╭︎( ˙º˙)╯︎*\033[0m")
