from src import api,read,player
import os
import sys
import json

os.system('clear')
dsktp=['0. 播放音乐(本地)','1. 播放歌单(本地)','2. 制作歌单(本地)','3. 收藏(本地)','4. 删除(本地)','5. 下载歌单内所有音乐(网易云)','6. 在线播放歌单(网易云)','7. 读取歌单(本地-网易云)','s. 设置','q. 退出']
for s in dsktp:
	print('\033[1;36m'+s+'\033[0m',end='\n\033[1;34m===========\033[0m\n\n')
ipt=input('\n\033[1;7;36m请输入序号:\033[0m')
os.system('clear')

if ipt=='0':
	print('\033[1;36m音乐正在加载中...\n\033[0m')
	api.show_ls(list(api.get_dirhash().keys()))
	print('\033[1;32m\n完成!\n\033[0m')
	ipt=input('\033[1;7;36m请输入歌曲前的序号以播放(可以用空格分隔开多个序号,播放全部请输入a):\033[0m')
	print('\n\033[1;36m你可以通过快捷键\033[0m\033[1;32mCtrl C\033[0m\033[1;36m停止播放或切换下一首歌!\033[0m')
	if ipt=='a':
		api.play('a',read.player_core)
		print('\033[1;32m\n完成!\n\033[0m')
		sys.exit(1)
	else:
		name=api.back_name(api.make_list(ipt))
		api.play(name,read.player_core)
		print('\033[1;36m是/否(y/n)把刚刚播放的音乐添加入歌单?\033[0m')
		chs=input('\033[1;7;36my / n :\033[0m')
		if chs=='y':
			print('\n\033[1;36m歌单正在加载中...\n\033[0m')
			print('\033[1;36m目前已有的歌单:\033[0m\n')
			api.show_ls(os.listdir(read.list_dir))
			list_name=input('\033[1;7;36m\n请为这张歌单命名:\033[0m')
			api.write_into(ipt,list_name)
			print('\033[1;32m\n完成!\n\033[0m')
			sys.exit(1)
		else:
			sys.exit(1)

if ipt=='1':
	print('\033[1;36m歌单正在加载中...\n\033[0m')
	api.show_ls(os.listdir(read.list_dir))
	print('\033[1;32m\n完成!\n\033[0m')
	ipt=input('\033[1;7;36m请输入歌单前的序号以播放:\033[0m')
	for hsh in api.back_hash(ipt):
		api.play_hash(hsh)
	sys.exit(1)

if ipt=='2':
	print('\033[1;36m音乐正在加载中...\n\033[0m')
	api.show_ls(list(api.get_dirhash().keys()))
	print('\033[1;32m\n完成!\n\033[0m')
	ipt=input('\033[1;7;36m请输入歌曲前的序号,每个序号间用空格分隔开:\033[0m')
	name=api.back_name(api.make_list(ipt))
	print('\n\033[1;36m歌单正在加载中...\n\033[0m')
	print('\033[1;36m目前已有的歌单:\033[0m\n')
	api.show_ls(os.listdir(read.list_dir))
	list_name=input('\033[1;7;36m\n请为这张歌单命名:\033[0m')
	api.write_into(ipt,list_name)
	print('\033[1;32m\n完成!\n\033[0m')
	sys.exit(1)

if ipt=='3':
	print('\033[1;36m音乐正在加载中...\n\033[0m')
	api.show_ls(list(api.get_dirhash().keys()))
	print('\033[1;32m\n完成!\n\033[0m')
	ipt=input('\033[1;7;36m请输入歌曲前的序号,每个序号间用空格分隔开:\033[0m')
	api.like(ipt)
	print('\033[1;32m\n完成!\n\033[0m')
	sys.exit(1)

if ipt=='4':
	dsktp=['0. 删除本地单曲文件','1. 删除本地歌单文件','2. 从歌单中删除单曲','3. 清空本地所有歌单内容','4. 清空本地所有歌单文件']
	for s in dsktp:
		print('\033[1;36m'+s+'\033[0m',end='\n\033[1;34m===========\033[0m\n\n')
	ipt=input('\n\033[1;7;36m请输入序号:\033[0m')
	os.system('clear')
	if ipt=='0':
		print('\033[1;36m音乐正在加载中...\n\033[0m')
		api.show_ls(list(api.get_dirhash().keys()))
		print('\033[1;32m\n完成!\n\033[0m')
		ipt=input('\033[1;7;36m请输入歌曲前的序号以删除(可以用空格分隔开多个序号,删除全部请输入a):\033[0m')
		name=api.back_name(api.make_list(ipt))
		if ipt=='a':
			api.play('a','rm -rf ')
			print('\033[1;32m\n完成!\n\033[0m')
			sys.exit(1)
		else:
			name=api.back_name(api.make_list(ipt))
			api.play(name,'rm -rf ')
			print('\033[1;32m\n完成!\n\033[0m')
			sys.exit(1)
	if ipt=='1':
		print('\033[1;36m歌单正在加载中...\n\033[0m')
		api.show_ls(os.listdir(read.list_dir))
		print('\033[1;32m\n完成!\n\033[0m')
		ipt=input('\033[1;7;36m请输入歌单前的序号以删除:\033[0m')
		api.rm_ls(ipt)
		print('\033[1;32m\n完成!\n\033[0m')
		sys.exit(1)
	if ipt=='2':
		print('\033[1;36m歌单正在加载中...\n\033[0m')
		api.show_ls(os.listdir(read.list_dir))
		print('\033[1;32m\n完成!\n\033[0m')
		ipt=input('\033[1;7;36m请输入歌单前的序号以选择:\033[0m')
		hsh=api.back_hash(ipt)
		nms=api.back_name(hsh)
		path=api.get_path(ipt)
		os.system('clear')
		print('\033[1;36m音乐正在加载中...\n\033[0m')
		api.show_ls(nms)
		print('\033[1;32m\n完成!\n\033[0m')
		ipt=input('\033[1;7;36m请输入歌曲前的序号以删除(可以用空格分隔开多个序号,删除全部请输入a):\033[0m')
		if ipt=='a':
			b=api.get_b('a',hsh,path)
			print('\033[1;32m\n完成!\n\033[0m')
			sys.exit(1)
		else:
			b=api.get_b(ipt,hsh,path)
			api.compare(b)
			print('\033[1;36m\n新歌单将会如上图所示,是/否(y/n)应用?\033[0m')
			chs=input('\033[1;7;36my / n :\033[0m')
			if chs=='y':
				api.rm_ls_inside(b,path)
				print('\033[1;32m\n完成!\n\033[0m')
				sys.exit(1)
			else:
				print('\033[1;32m\n已撤销操作!\n\033[0m')
				sys.exit(1)
		
	if ipt=='3':
		api.clear_all()
		print('\033[1;32m\n完成!\n\033[0m')
		sys.exit(1)
	if ipt=='4':
		api.dl_all_file()
		print('\033[1;32m\n完成!\n\033[0m')
		sys.exit(1)

if ipt=='5':
	path=read.dl_dir+'/列表/'
	player.read_dir(path)
	uid=input('\n请输入要下载的歌单前的序号:')
	player.dl_list(uid)

if ipt=='6':
	uid=input('\n请输入网易云歌单ID:')
	result=api.model_lid('playlist/track/all',uid,read.songs_limit)
	ids=api.get_online_ids(result['songs'])
	print('\n你可以随时输入Ctrl C终止播放!\n')
	for i in ids:
		result=api.model_id('song/url',i)['data'][0]
		os.system('play '+result['url'])
		print('\n你可以随时输入Ctrl C终止播放!\n')

if ipt=='7':
	path=read.dl_dir+'/列表/'
	player.read_dir(path)
	uid=input('\n请输入要读取的歌单前的序号:')
	player.read_list(uid)

if ipt=='s':
	os.system('nano src/conf.yaml')
	sys.exit(1)

if ipt=='q':
	print('\033[1;36m\nBye~~ O(∩_∩)O~~\n\033[0m')
	sys.exit(1)