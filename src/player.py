from . import read,api
import os

'''
方便用户选择时使用(只输入序号而并非输入文件名)
返回文件与序号的字典
'''
def get_dic(uid,path):
	value=[]
	key=[]
	for ls in os.listdir(path):
		value.append(ls)
	for ls in range(0,int(len(value))):
		key.append(ls)
	dic=dict(zip(key,value))
	return dic[int(uid)]

'''
从'列表'文件夹(储存所有歌单ID)
按换行读取序号对应的文件并返回列表
'''
def get_ids(uid):
	path=read.dl_dir+'/列表/'
	vle=get_dic(uid,read.dl_dir+'/列表/')
	with open(path+vle,'r') as f:
		id_ls=f.read().splitlines()
	return id_ls

'''
读取路径并储存为列表
随后美化输出
'''
def read_dir(path):
	read.ls(os.listdir(path))

'''
按换行读取序号对应的文件并返回列表
将列表转换为逗号隔开的ids
批量请求歌曲信息
'''
def read_list(uid):
	ids=','.join(get_ids(uid))
	result=api.model_ids('song/detail',ids)
	api.info_real(result['songs'])

'''
按换行读取序号对应的文件并返回列表
批量获取音乐直链并下载
'''
def dl_list(uid):
	ids=get_ids(uid)
	print('歌单共'+str(len(ids))+'首歌,正在下载...')
	for i in ids:
		result=api.model_id('song/url',i)['data'][0]
		print('\n正在下载 '+api.info_limit(i)+'...')
		if result['url']==None:
			print('下载失败!')
		else:
			if read.auto_lyric:
				part='lyric'
				res=api.model_id(part,i)
				api.auto_lyric(res['lrc']['lyric'],api.info_limit(i))
			else:
				pass
			os.system(api.auto_dl(result['url'],api.info_limit(i),result['type']))
			print(api.info_limit(i)+'下载完成!\n')

'''
选择序号对应的单曲
返回播放该单曲的指令
'''
def local_play(uid):
	vle=get_dic(uid,read.dl_dir+'/音乐/')
	return 'play '+read.dl_dir+'/音乐/'+vle

'''
以空格分隔对用户输入的序号生成列表
随后按照序号与文件名的对照生成列表并返回
'''
def make_list(thing):
	string=thing.split(' ')
	value=[]
	key=[]
	for ls in os.listdir(read.dl_dir+'/音乐/'):
		value.append(ls)
	for ls in range(0,int(len(value))):
		key.append(str(ls))
	dic=dict(zip(key,value))
	lis=[]
	for ls in string:
		imp=dic[ls]
		lis.append(imp)
	return lis