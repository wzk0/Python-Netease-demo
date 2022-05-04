from . import read,api
import os

root_dir=read.dl_dir
path=root_dir+'/列表/'

def get_ids(uid):
	value=[]
	key=[]
	for ls in os.listdir(path):
		value.append(ls)
	for ls in range(0,int(len(value))):
		key.append(ls)
	dic=dict(zip(key,value))
	vle=dic[int(uid)]
	with open(path+vle,'r') as f:
		id_ls=f.read().splitlines()
	return id_ls

def read_dir():
	read.ls(os.listdir(path))

def read_list(uid):
	ids=','.join(get_ids(uid))
	result=api.model_ids('song/detail',ids)
	api.info_real(result['songs'])

def dl_list(uid):
	ids=get_ids(uid)
	print('歌单共'+str(len(ids))+'首歌,正在下载...')
	for i in ids:
		result=api.model_id('song/url',i)['data'][0]
		print('\n正在下载 '+api.info_limit(i)+'...')
		os.system(api.auto_dl(result['url'],api.info_limit(i),result['type']))
		print(api.info_limit(i)+'下载完成!\n')