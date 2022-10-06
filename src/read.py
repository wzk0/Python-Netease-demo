import yaml
import json
import os

'''
读取配置文件并做传递的准备
'''
def get_good_name(name):
	name=name.replace('(','\(')
	name=name.replace(')','\)')
	name=name.replace(' ','\ ')
	return name

conf=yaml.load(open('src/conf.yaml'),Loader=yaml.FullLoader)
server=conf['server']
playlist_limit=conf['playlist_limit']
history_limit=conf['history_limit']
singersongs_limit=conf['singersongs_limit']
songs_limit=conf['songs_limit']
search_limit=conf['search_limit']
comment_limit=conf['comment_limit']
album_limit=conf['album_limit']
albumsinger_limit=conf['albumsinger_limit']
singer_limit=conf['singer_limit']
mv_limit=conf['mv_limit']
da_limit=conf['da_limit']
auto_download=conf['auto_download']
dl_dir=conf['dl_dir']
auto_lyric=conf['auto_lyric']
music_dltype=conf['music_dltype']
auto_id=conf['auto_id']
icon_ui=conf['icon_ui']
ui_len=conf['ui_len']
rainbow=conf['rainbow']
auto_ls=conf['auto_ls']
pure_color=conf['pure_color']
auto_play=conf['auto_play']
sleep_time=conf['sleep_time']
preview=conf['preview']

music_dir=dl_dir+'/音乐/'
lrc_path=dl_dir+'/歌词/'
list_dir=dl_dir+'/本地歌单/'
player_core=conf['player_core']
if player_core=='cvlc ':
	player_core='cvlc --play-and-exit '
music_dir=get_good_name(music_dir)
list_dir=get_good_name(list_dir)

'''
用于美化输出任何列表
'''
def ls(lis):
	print('\n')
	for ls in lis:
		print('\033[1;34m'+icon_ui*ui_len+'\033[0m\n')
		print('\033[1;35;44m'+str(lis.index(ls))+'.\033[0m | \033[0m\033[1;36m'+ls+'\033[0m')

'''
读取cookies
'''
with open("src/cookies.json",'r', encoding='UTF-8') as f:
	cookies=json.load(f)

'''
根据检查是否缺少相关文件夹
并采取相应措施
'''
def check_dir():
	if not os.path.exists(dl_dir)==True:
		os.system('mkdir '+dl_dir)
	if not os.path.exists(dl_dir+'/音乐')==True:
		os.system('mkdir '+dl_dir+'/音乐')
	if not os.path.exists(dl_dir+'/歌词')==True:
		os.system('mkdir '+dl_dir+'/歌词')
	if not os.path.exists(dl_dir+'/本地歌单')==True:
		os.system('mkdir '+dl_dir+'/本地歌单')
	if auto_id==True:
		if not os.path.exists(dl_dir+'/列表')==True:
			os.system('mkdir '+dl_dir+'/列表')