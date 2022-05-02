import os
from src import api
def ls(lis):
	print('\n')
	for ls in lis:
		print('='*12)
		print(str(lis.index(ls))+'. '+ls)
		
os.system('clear')
print('Netease for Terminal\n','功能如下:')
desktop=['登录','个人']
ls(desktop)
print('='*12)
mode=input('\n请选择模式:')
if mode=='0':
	phone=input('\n请输入网易云账号手机号码:')
	pwd=input('\n请输入网易云账号密码:')
	result=api.login('login/cellphone',phone,pwd)
	if os.path.exists('src/cookies.json'):
		mode=input('\n你似乎已经登录过了...是/否(y/n)刷新cookies:')
		print('\n')
		if mode=='y':
			os.system('rm src/cookies.json && touch src/cookies.json')
			with open('src/cookies.json','w')as f:
				f.write(result)
		else:
			pass
	else:
		with open('src/cookies.json','w')as f:
			f.write(result)
if mode=='1':
	desktop=['用户详情','账号信息','音乐信息','等级信息','绑定信息']
	ls(desktop)
	print('='*12)
	mode=input('\n请选择模式:')
	if mode=='0':
		uid=input('\n请输入用户ID:')
		print('\n')
		result=api.detail('user/detail',uid)
		dic={
		'用户ID':result['userPoint']['userId'],
		'用户等级':result['level'],
		'累积听歌':result['listenSongs'],
		'用户昵称':result['profile']['nickname'],
		'用户生日':result['profile']['birthday'],
		'用户城市':result['profile']['city'],
		'用户类型':result['profile']['vipType'],
		'用户简介':result['profile']['signature'],
		'关注数量':result['profile']['newFollows'],
		'歌单数量':result['profile']['playlistCount'],
		'账号天数':result['createDays']
		}
		for key,value in zip(dic.keys(),dic.values()):
			print(key+': '+str(value),end='\n')