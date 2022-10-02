import os
import json
from src import api,read,player
import sys

read.check_dir()
		
os.system('clear')
print('Netease for Terminal\n','功能如下:',end='')
desktop=['登录','个人','歌单','评论','歌手','专辑','MV','收藏','音乐','搜索','日推','签到','播放器','设置','退出']
read.ls(desktop)
print('\033[1;34m'+read.icon_ui*read.ui_len+'\033[0m\n')
mode=input('\n\033[1;7;36m请选择模式:\033[0m')
if mode=='0':
	phone=input('\n\033[1;7;36m请输入网易云账号手机号码:\033[0m')
	pwd=input('\n\033[1;7;36m请输入网易云账号密码:\033[0m')
	result=api.login('login/cellphone',phone,pwd)
	if os.path.exists('src/cookies.json'):
		os.system('rm src/cookies.json && touch src/cookies.json')
		with open('src/cookies.json','w')as f:
			f.write(result)
		sys.exit(1)
	else:
		with open('src/cookies.json','w')as f:
			f.write(result)
if mode=='1':
	desktop=['查询用户','账号信息','音乐信息','等级信息']
	read.ls(desktop)
	print('\033[1;34m'+read.icon_ui*read.ui_len+'\033[0m\n')
	mode=input('\n\033[1;7;36m请选择模式:\033[0m')
	if mode=='0':
		uid=input('\n\033[1;7;36m请输入用户ID:\033[0m')
		print('\n')
		result=api.model_1('user/detail',uid)
		dic={
		'用户ID':result['userPoint']['userId'],
		'用户等级':result['level'],
		'累积听歌':result['listenSongs'],
		'用户昵称':result['profile']['nickname'],
		'用户生日':result['profile']['birthday'],
		'用户城市':result['profile']['city'],
		'用户简介':result['profile']['signature'],
		'是否为VIP':result['profile']['vipType'],
		'是否为音乐人':result['profile']['djStatus'],
		'关注数量':result['profile']['newFollows'],
		'歌单数量':result['profile']['playlistCount'],
		'账号天数':result['createDays']
		}
		for key,value in zip(dic.keys(),dic.values()):
			print(key+': '+str(value),end='\n')
		sys.exit(1)
	if mode=='1':
		result=api.model_0('user/account')
		dic={
		'我的ID':result['account']['id'],
		'我的昵称':result['profile']['nickname'],
		'我的生日':result['profile']['birthday'],
		'我的城市':result['profile']['city'],
		'我的简介':result['profile']['signature'],
		'是否为VIP':result['profile']['vipType'],
		'是否为音乐人':result['profile']['djStatus'],
		'最后一次登录时间':result['profile']['lastLoginTime'],
		'最后一次登录IP':result['profile']['lastLoginIP']
		}
		for key,value in zip(dic.keys(),dic.values()):
			print(key+': '+str(value),end='\n')
		sys.exit(1)
	if mode=='2':
		result=api.model_0('user/subcount')
		dic={
		'收藏电台数':result['djRadioCount'],
		'收藏MV数':result['mvCount'],
		'收藏歌手数':result['artistCount'],
		'收藏歌单数':result['subPlaylistCount'],
		'创建电台数':result['createDjRadioCount'],
		'创建歌单数':result['createdPlaylistCount']
		}
		for key,value in zip(dic.keys(),dic.values()):
			print(key+': '+str(value),end='\n')
		sys.exit(1)
	if mode=='3':
		result=api.model_0('user/level')
		info=result['data']['info'].replace('$','\n')
		nextPlayCount=result['data']['nextPlayCount']
		nextLoginCount=result['data']['nextLoginCount']
		nowPlayCount=result['data']['nowPlayCount']
		nowLoginCount=result['data']['nowLoginCount']
		dic={
		'我的ID':result['data']['userId'],
		'我的等级':result['data']['level'],
		'等级特权':'\n'+info,
		'距离下一等级需要听歌首数':str(nextPlayCount-nowPlayCount),
		'距离下一等级需要登录天数':str(nextLoginCount-nowLoginCount)
		}
		for key,value in zip(dic.keys(),dic.values()):
			print(key+': '+str(value),end='\n')
		sys.exit(1)

if mode=='2':
	desktop=['查询用户歌单','歌单详情','歌单歌曲','相似歌单']
	read.ls(desktop)
	print('\033[1;34m'+read.icon_ui*read.ui_len+'\033[0m\n')
	mode=input('\n\033[1;7;36m请选择模式:\033[0m')
	if mode=='0':
		uid=input('\n\033[1;7;36m请输入用户ID:\033[0m')
		print('\n')
		result=api.model_1('user/playlist',uid)
		lis=result['playlist']
		for ele in lis:
			name=ele['name']
			uid=ele['id']
			playCount=ele['playCount']
			trackCount=ele['trackCount']
			description=ele['description']
			print(str(lis.index(ele))+'\n'+'='*20+'\n歌单名: '+name+'\n'+'歌单ID: '+str(uid)+'\n'+'播放次数: '+str(playCount)+'\n'+'包含歌曲数: '+str(trackCount)+'\n'+'描述: \n'+str(description)+'\n',end='\n\n')
		sys.exit(1)
	if mode=='1':
		uid=input('\n\033[1;7;36m请输入歌单ID:\033[0m')
		print('\n')
		result=api.model_id('playlist/detail',uid)
		print(result)
		sys.exit(1)
	if mode=='2':
		uid=input('\n\033[1;7;36m请输入歌单ID:\033[0m')
		print('\n')
		result=api.model_lid('playlist/track/all',uid,read.songs_limit)
		api.info_list(result['songs'])
		sys.exit(1)
	if mode=='3':
		uid=input('\n\033[1;7;36m请输入歌单ID:\033[0m')
		print('\n')
		result=api.model_id('simi/playlist',uid)
		print(result)
		sys.exit(1)

if mode=='3':
	desktop=['查询用户历史评论','获取评论']
	read.ls(desktop)
	print('\033[1;34m'+read.icon_ui*read.ui_len+'\033[0m\n')
	mode=input('\n\033[1;7;36m请选择模式:\033[0m')
	if mode=='0':
		uid=input('\n\033[1;7;36m请输入用户ID:\033[0m')
		print('\n')
		result=api.model_1('user/comment/history',uid)
		print(result)
		sys.exit(1)
	if mode=='1':
		desktop=['歌曲','MV','歌单','专辑']
		read.ls(desktop)
		print('\033[1;34m'+read.icon_ui*read.ui_len+'\033[0m\n')
		type_id=input('\n\033[1;7;36m请输入资源类型ID:\033[0m')
		uid=input('\n\033[1;7;36m请输入资源ID:\033[0m')
		result=api.hot_comment('comment/hot',uid,read.comment_limit,type_id)
		api.comment_real(result)
		sys.exit(1)

if mode=='4':
	desktop=['歌手热门歌曲','歌手专辑','歌手MV','歌手信息','相似歌手','热门歌手']
	read.ls(desktop)
	print('\033[1;34m'+read.icon_ui*read.ui_len+'\033[0m\n')
	mode=input('\n\033[1;7;36m请选择模式:\033[0m')
	uid=input('\n\033[1;7;36m请输入歌手ID:\033[0m')
	if mode=='0':
		result=api.singer_hot('artist/songs',uid,read.singersongs_limit)
		print(result)
		sys.exit(1)
	if mode=='1':
		result=api.model_lid('artist/album',uid,read.albumsinger_limit)
		print(result)
		sys.exit(1)
	if mode=='5':
		result=api.model_limit('top/artists',read.singer_limit)
		print(result)
		sys.exit(1)
	else:
		def choose(mode):
			if mode=='2':
				return 'artist/mv'
			if mode=='3':
				return 'artist/desc'
			if mode=='4':
				return 'simi/artist'
		part=choose(mode)
		result=api.model_id(part,uid)
		print(result)
		sys.exit(1)
 
if mode=='5':
	desktop=['专辑内容','专辑信息','我的数专']
	read.ls(desktop)
	print('\033[1;34m'+read.icon_ui*read.ui_len+'\033[0m\n')
	mode=input('\n\033[1;7;36m请选择模式:\033[0m')
	uid=input('\n\033[1;7;36m请输入专辑ID:\033[0m')
	if mode=='0':
		result=api.model_id('album',uid)
		print(result)
		sys.exit(1)
	if mode=='1':
		result=api.model_id('album/detail/dynamic',uid)
		print(result)
		sys.exit(1)
	if mode=='2':
		result=api.model_limit('digitalAlbum/purchased',read.da_limit)
		print(result)
		sys.exit(1)

if mode=='6':
	desktop=['获取MV','MV详情','MV排行','推荐MV']
	read.ls(desktop)
	print('\033[1;34m'+read.icon_ui*read.ui_len+'\033[0m\n')
	mode=input('\n\033[1;7;36m请选择模式:\033[0m')
	if mode=='2':
		result=api.model_limit('top/mv',read.mv_limit)
		print(result)
		sys.exit(1)
	if mode=='3':
		result=api.model_0('personalized/mv')
		print(result)
		sys.exit(1)
	else:
		uid=input('\n\033[1;7;36m请输入MV的ID\033[0m')
		def choose(mode):
			if mode=='0':
				result=api.model_id('mv/url',uid)
				return result
			if mode=='1':
				result=api.mvid('mv/detail',uid)
				return result
		result=choose(mode)
		print(result)

if mode=='7':
	desktop=['收藏歌手','收藏专栏','收藏歌单','收藏MV','收藏专辑']
	read.ls(desktop)
	print('\033[1;34m'+read.icon_ui*read.ui_len+'\033[0m\n')
	mode=input('\n\033[1;7;36m请选择模式:\033[0m')
	if mode=='0':
		result=api.model_0('artist/sublist')
		print(result)
		sys.exit(1)
	if mode=='1':
		result=api.sublist('topic/sublist')
		print(result)
		sys.exit(1)
	if mode=='2':
		pass
	if mode=='3':
		result=api.model_0('mv/sublist')
		print(result)
		sys.exit(1)
	if mode=='4':
		result=api.model_limit('album/sublist',read.album_limit)
		print(result)

if mode=='8':
	desktop=['获取音乐','获取歌词','相似歌曲','收藏音乐(动词)','高级获取']
	read.ls(desktop)
	print('\033[1;34m'+read.icon_ui*read.ui_len+'\033[0m\n')
	mode=input('\n\033[1;7;36m请选择模式:\033[0m')
	uid=input('\n\033[1;7;36m请输入歌曲ID:\033[0m')
	result=api.model_ids('song/detail',uid)
	print('\n此歌曲的相关信息: ',end='')
	api.info_real(result['songs'])
	if mode=='0':
		result=api.model_id('song/url',uid)['data'][0]
		if result['url']==None:
			print('下载失败!')
		else:
			print('\n歌曲ID: '+str(result['id'])+'\n歌曲码率: '+str(result['br'])+'\n大小: '+str(result['size'])+'\nmd5: '+result['md5']+'\n音频直链: \n'+result['url']+'\n音频格式: '+result['type'])
			if read.auto_download==True:
				print('\n开始自动下载...')
				act=api.auto_dl(result['url'],api.info_limit(uid),result['type'])
				os.system(act)
			sys.exit(1)
	if mode=='1':
		part='lyric'
		result=api.model_id(part,uid)
		print('\n歌词如下:\n'+result['lrc']['lyric'])
		if read.auto_lyric==True:
			api.auto_lyric(result['lrc']['lyric'],api.info_limit(uid))
		sys.exit(1)
	if mode=='2':
		part='simi/song'
		result=api.model_id(part,uid)
		sys.exit(1)
	if mode=='3':
		part='like'
		result=api.model_id(part,uid)
		sys.exit(1)
	if mode=='4':
		part='song/download/url'
		result=api.model_id(part,uid)
		sys.exit(1)

if mode=='9':
	desktop=['全局搜索','热搜列表']
	read.ls(desktop)
	print('\033[1;34m'+read.icon_ui*read.ui_len+'\033[0m\n')
	mode=input('\n\033[1;7;36m请选择模式:\033[0m')
	if mode=='1':
		result=api.model_0('search/hot/detail')
		for ele in result['data']:
			print('\n热搜关键词: '+ele['searchWord']+'\n热度: '+str(ele['score']))
		sys.exit(1)
	else:
		keywords=input('\n\033[1;7;36m请输入关键词:\033[0m')
		result=api.search_all('cloudsearch',keywords,read.search_limit)
		print('\n已找到'+str(result['result']['songCount'])+'条可用结果,返回'+read.search_limit+'条\n')
		api.info_real(result['result']['songs'])
		sys.exit(1)

if mode=='10':
	desktop=['日推歌单','日推歌曲','可用历史日推','获取历史日推']
	read.ls(desktop)
	print('\033[1;34m'+read.icon_ui*read.ui_len+'\033[0m\n')
	mode=input('\n\033[1;7;36m请选择模式:\033[0m')
	if mode=='3':
		date=input('\n\033[1;7;36m请输入日期(格式:2020-06-21):\033[0m')
		result=api.history_recommend('history/recommend/songs/detail',date)
		api.info_list(result['data']['songs'])
		sys.exit(1)
	if mode=='0':
		part='recommend/resource'
		result=api.model_0(part)
		for ele in result['recommend']:
			print(str(result['recommend'].index(ele))+'\n歌单名称: '+ele['name']+'\n歌单ID: '+str(ele['id'])+'\n歌曲数量: '+str(ele['trackCount'])+'\n'+ele['copywriter']+'\n来自用户: '+ele['creator']['nickname']+' 创建的歌单',end='\n\n')
		sys.exit(1)
	if mode=='1':
		part='recommend/songs'
		result=api.model_0(part)
		api.info_list(result['data']['dailySongs'])
		sys.exit(1)	
	if mode=='2':
		part='history/recommend/songs'
		result=api.model_0(part)
		def back(lis):
			for e in lis:
				return e+' '
		print('\n可用的历史日推时间: \n'+back(result['data']['dates'])+'\n'+result['data']['description']+','+result['data']['noHistoryMessage'])
		sys.exit(1)

if mode=='11':
	desktop=['签到','云贝签到','一键全签']
	read.ls(desktop)
	print('\033[1;34m'+read.icon_ui*read.ui_len+'\033[0m\n')
	mode=input('\n\033[1;7;36m请选择模式:\033[0m')
	if mode=='2':
		api.model_0('daily_signin')
		api.model_0('yunbei/sign')
		print('\033[1;32m\n成功!\n\033[0m')
		sys.exit(1)
	def choose(mode):
		if mode=='0':
			return 'daily_signin'
		if mode=='1':
			return 'yunbei/sign'
	part=choose(mode)
	result=api.model_0(part)
	if result['code']==200:
		print('\033[1;32m\n签到成功!\033[0m')
		print('\n\033[1;36m获得积分:\033[1;32m'+str(result['point'])+'\033[0m\033[0m')
		sys.exit(1)
	else:
		print('\n\033[1;31m签到失败!请检查账户或网络\033[0m')
		sys.exit(1)

if mode=='12':
	os.system('python3 player_main.py')

if mode=='13':
	os.system('nano src/conf.yaml')

if mode=='14':
	sys.exit(1)