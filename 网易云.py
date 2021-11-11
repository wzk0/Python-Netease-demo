import requests
import json
import os

s = "song"
l = "lyric"
s= "search"
m = "mv"
h = "hot"
print("\n\n\n———————————————————————")
print("网易云辅助demo！(´◊ω◊｀)\n")
print("由听话的便当手打制作！٩(๑ᵒ̴̶̷͈᷄ᗨᵒ̴̶̷͈᷅)و")
print("-----------------------------------------------------")
print("0代表登陆，01:检查是否登陆(目前登陆没什么卵用(||๐_๐))\n1代表歌曲，2代表歌词，\n3代表搜索，4代表MV，5代表热评")
print("-----------------------------------------------------")
type = input ("请输入序号:")

if type == "0":

  phone = input("请输入手机号码:")
  password = input("请输入密码:")
  url = "https://163.lpddr5.cn/login/cellphone?phone=" + phone +"&password=" + password
  r = requests.post(url)
  text = r.text
  temp = json.loads(text)
  if temp['code'] == 200:
     print("已经成功登陆啦！❛‿˂̵✧")
  else:
     print("不知道什么原因失败了...\n请检查密码是否正确 (*꒦ິ⌓꒦ີ)")

if type == "01":

  url = "https://163.lpddr5.cn/login/status"
  r = requests.post(url)
  text = r.text
  temp = json.loads(text)
  if temp['data']['code'] == 200:
     print("是登陆状态！վ'ᴗ' ի")
     print("——————————————")
  else:
     print("还没登陆呢！(꒪⌓꒪) ")
     print("——————————————")

if type == "1":

  id = input("请输入歌曲ID:")
  print("已确定类型:" + s)
  print("调用方法:song/url?id=" + id)
  print("直链来啦！")

  url1 = "https://163.lpddr5.cn/song/url?id=" + id
  r = requests.post(url1)
  text = r.text
  temp = json.loads(text)
  print("——————————————")
  print("高品质临时链接:")
  print(temp['data'][0]['url'])
  print("——————————————")
  print("永久直链:")
  print("http://music.163.com/song/media/outer/url?id=" + id)
  print("——————————————")

elif type == "2":

  id = input("请输入歌曲ID:")
  print("已确定类型:" + l)
  print("调用方法:lyric?id=" + id)
  print("歌词来啦！")

  url2 = "https://163.lpddr5.cn/lyric?id=" + id
  r = requests.post(url2)
  text = r.text
  temp = json.loads(text)
  print(temp['lrc']['lyric'])

elif type == "3":

  word = input("请输入关键词:")
  print("已确定类型:" + s)
  print("调用方法:search?keywords=" + word)
  print("结果来啦！")

  url3= "https://163.lpddr5.cn/search?keywords=" + word + "&limit=3"
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

elif type == "4":

  print (m)

elif type == "5":

  print("0: 歌曲，1: mv，2: 歌单，3: 专辑，4: 电台，5: 视频")
  id = input("请输入资源ID:")
  type = input("请输入资源类型的序号:")
  print("已确定类型:" + h)
  print("调用方法:comment/hot?id=" + id + "&type=" + type)
  print("热评来啦！")
  url5 = "https://163.lpddr5.cn/comment/hot?id=" + id + "&type=" + type + "&limit=5"
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

elif type != "0""1""2""3""4""5""01":

  print("输入的序号必须是已有的序号！")
  print("正在重启...")
  print("——————————————————————————————")
  os.system("python ~/Python/wyy.py")

re = input("输入1以继续获取；0为退出程序(๑ت๑):")

if re == "1":
  os.system("python 网易云.py")
if re == "0":
  print("Bye*╭︎( ˙º˙)╯︎*")
