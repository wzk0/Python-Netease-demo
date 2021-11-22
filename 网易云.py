import requests
import json
import os

s = "song"
l = "lyric"
s= "search"
m = "mv"
h = "hot"
llink = "http://iwenwiki.com:3000"

## 备用:https://autumnfish.cn
## 备用:http://iwenwiki.com:3000
## 备用:http://119.45.25.73

print("\n\n\n———————————————————————")
print("网易云辅助demo！(´◊ω◊｀)\n")
print("由听话的便当手打制作！٩(๑ᵒ̴̶̷͈᷄ᗨᵒ̴̶̷͈᷅)و")
print("\n您当前的API服务器为:" + llink + "\n如需更换，请修改llink的值！")
print("-----------------------------------------------")
print("\n0)登陆(目前没什么卵用(||๐_๐))\n\n1)获取歌曲         2)获取歌词\n\n3)搜索             4)获取MV\n\n5)获取热评         6)获取热搜\n\n7)获取歌手热门\n")
print("-----------------------------------------------")
type = input ("请输入序号:")

if type == "0":

  phone = input("请输入手机号码:")
  password = input("请输入密码:")
  url = llink + "/login/cellphone?phone=" + phone +"&password=" + password
  r = requests.post(url)
  text = r.text
  temp = json.loads(text)
  if temp['code'] == 200:
     print("已经成功登陆啦！❛‿˂̵✧")
  else:
     print("不知道什么原因失败了...\n请检查密码是否正确 (*꒦ິ⌓꒦ີ)")

if type == "1":

  id = input("请输入歌曲ID:")
  print("已确定类型:" + s)
  print("调用方法:/song/url?id=" + id)
  print("直链来啦！")

  url1 = llink + "/song/url?id=" + id
  r = requests.post(url1)
  text = r.text
  temp = json.loads(text)
  print("——————————————")
  print("高品质临时链接:")
  print(temp['data'][0]['url'])
  print("——————————————")
  print("永久直链:")
  print("https://music.163.com/song/media/outer/url?id=" + id)
  print("——————————————")

elif type == "2":

  id = input("请输入歌曲ID:")
  print("已确定类型:" + l)
  print("调用方法:/lyric?id=" + id)
  print("歌词来啦！")

  url2 = llink + "/lyric?id=" + id
  r = requests.post(url2)
  text = r.text
  temp = json.loads(text)
  print(temp['lrc']['lyric'])

elif type == "3":

  word = input("请输入关键词:")
  print("已确定类型:" + s)
  print("调用方法:/search?keywords=" + word)
  print("结果来啦！")

  url3= llink + "/search?keywords=" + word + "&limit=5"
  r = requests.post(url3)
  text = r.text
  temp = json.loads(text)

  print("——————————————")
  print("歌曲名称:")
  print(temp['result']['songs'][0]['name'])
  print("———————————")
  print("歌曲ID:")
  print(temp['result']['songs'][0]['id'])
  print("—————————")
  print("歌手:")
  print(temp['result']['songs'][0]['artists'][0]['name'])
  print("——————————————")

  print("——————————————")
  print("歌曲名称:")
  print(temp['result']['songs'][1]['name'])
  print("———————————")
  print("歌曲ID:")
  print(temp['result']['songs'][1]['id'])
  print("—————————")
  print("歌手:")
  print(temp['result']['songs'][1]['artists'][0]['name'])
  print("——————————————")

  print("——————————————")
  print("歌曲名称:")
  print(temp['result']['songs'][2]['name'])
  print("———————————")
  print("歌曲ID:")
  print(temp['result']['songs'][2]['id'])
  print("—————————")
  print("歌手:")
  print(temp['result']['songs'][2]['artists'][0]['name'])
  print("——————————————")

  print("——————————————")
  print("歌曲名称:")
  print(temp['result']['songs'][3]['name'])
  print("———————————")
  print("歌曲ID:")
  print(temp['result']['songs'][3]['id'])
  print("—————————")
  print("歌手:")
  print(temp['result']['songs'][3]['artists'][0]['name'])
  print("——————————————")

  print("——————————————")
  print("歌曲名称:")
  print(temp['result']['songs'][4]['name'])
  print("———————————")
  print("歌曲ID:")
  print(temp['result']['songs'][4]['id'])
  print("—————————")
  print("歌手:")
  print(temp['result']['songs'][4]['artists'][0]['name'])
  print("——————————————")

elif type == "4":

  id = input("请输入MV的ID:")
  print("调用方法:/mv/url?id=" + id)
  url = llink + "/mv/url?id=" + id
  r = requests.post(url)
  text = r.text
  temp = json.loads(text)
  print(temp['data']['url'])

elif type == "5":

  print("0: 歌曲，1: mv，2: 歌单，3: 专辑，4: 电台，5: 视频")
  id = input("请输入资源ID:")
  type = input("请输入资源类型的序号:")
  print("已确定类型:" + h)
  print("调用方法:/comment/hot?id=" + id + "&type=" + type)
  print("热评来啦！")
  url5 = llink + "/comment/hot?id=" + id + "&type=" + type + "&limit=5"
  r = requests.post(url5)
  text = r.text
  temp = json.loads(text)

  print("——————————————————")
  print("来自用户:")
  print(temp['hotComments'][0]['user']['nickname'])
  print("——————————————")
  print("的热评:")
  print("--------")
  print(temp['hotComments'][0]['content'])
  print("--------")
  print("点赞数:")
  print(temp['hotComments'][0]['likedCount'])
  print("——————————————")

  print("——————————————————")
  print("来自用户:")
  print(temp['hotComments'][1]['user']['nickname'])
  print("——————————————")
  print("的热评:")
  print("--------")
  print(temp['hotComments'][1]['content'])
  print("--------")
  print("点赞数:")
  print(temp['hotComments'][1]['likedCount'])
  print("——————————————")

  print("——————————————————")
  print("来自用户:")
  print(temp['hotComments'][2]['user']['nickname'])
  print("——————————————")
  print("的热评:")
  print("--------")
  print(temp['hotComments'][2]['content'])
  print("--------")
  print("点赞数:")
  print(temp['hotComments'][2]['likedCount'])
  print("——————————————")

  print("——————————————————")
  print("来自用户:")
  print(temp['hotComments'][3]['user']['nickname'])
  print("——————————————")
  print("的热评:")
  print("--------")
  print(temp['hotComments'][3]['content'])
  print("--------")
  print("点赞数:")
  print(temp['hotComments'][3]['likedCount'])
  print("——————————————")

  print("——————————————————")
  print("来自用户:")
  print(temp['hotComments'][4]['user']['nickname'])
  print("——————————————")
  print("的热评:")
  print("--------")
  print(temp['hotComments'][4]['content'])
  print("--------")
  print("点赞数:")
  print(temp['hotComments'][4]['likedCount'])
  print("——————————————")

elif type == "6":
  urlll = llink + "/search/hot/"
  r = requests.post(urlll)
  text = r.text
  temp = json.loads(text)
  print("———————————")
  print("第一名:")
  print(temp['result']['hots'][0]['first'])
  print("———————————")
  print("第二名:")
  print(temp['result']['hots'][1]['first'])
  print("———————————")
  print("第三名:")
  print(temp['result']['hots'][2]['first'])
  print("———————————")
  print("第四名:")
  print(temp['result']['hots'][3]['first'])
  print("———————————")
  print("第五名:")
  print(temp['result']['hots'][4]['first'])
  print("———————————")
  print("第六名:")
  print(temp['result']['hots'][5]['first'])
  print("———————————")
  print("第七名:")
  print(temp['result']['hots'][6]['first'])
  print("———————————")
  print("第八名:")
  print(temp['result']['hots'][7]['first'])
  print("———————————")
  print("第九名:")
  print(temp['result']['hots'][8]['first'])
  print("———————————")
  print("第十名:")
  print(temp['result']['hots'][9]['first'])
  print("———————————")

if type == "7":

  id = input("请输入歌手ID:")
  print("调用方法:/artist/top/song?id=" + id)
  url = llink + "/artist/top/song?id=" + id
  r = requests.post(url)
  text = r.text
  temp = json.loads(text)
  print("—————————")
  print("歌名:")
  print(temp['songs'][0]['name'])
  print("id:")
  print(temp['songs'][0]['id'])
  print("—————————")
  print("歌名:")
  print(temp['songs'][1]['name'])
  print("id:")
  print(temp['songs'][1]['id'])
  print("—————————")
  print("歌名:")
  print(temp['songs'][3]['name'])
  print("id:")
  print(temp['songs'][3]['id'])
  print("—————————")
  print("歌名:")
  print(temp['songs'][4]['name'])
  print("id:")
  print(temp['songs'][4]['id'])
  print("—————————")
  print("歌名:")
  print(temp['songs'][5]['name'])
  print("id:")
  print(temp['songs'][5]['id'])
  print("—————————")
  print("歌名:")
  print(temp['songs'][6]['name'])
  print("id:")
  print(temp['songs'][6]['id'])
  print("—————————")
  print("歌名:")
  print(temp['songs'][7]['name'])
  print("id:")
  print(temp['songs'][7]['id'])
  print("—————————")
  print("歌名:")
  print(temp['songs'][8]['name'])
  print("id:")
  print(temp['songs'][8]['id'])
  print("—————————")
  print("歌名:")
  print(temp['songs'][9]['name'])
  print("id:")
  print(temp['songs'][9]['id'])
  print("—————————")

re = input("输入1以继续获取；0为退出程序(๑ت๑):")

if re == "1":
  os.system("python 网易云.py")
if re == "0":
  print("Bye*╭︎( ˙º˙)╯︎*")
