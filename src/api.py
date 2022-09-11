import requests
import json
from . import read
import hashlib
import os

'''
读取配置
'''
server=read.server
cookies=read.cookies

'''
登录的封装
'''
def login(part,phone,pwd):
	params={
	'phone':phone,
	'password':pwd
	}
	r=requests.get(server+part,params=params)
	true=True
	false=False
	null='无'
	data=r.text
	data=json.loads(data)
	print('欢迎!'+data['profile']['nickname']+',登录成功!')
	c=data['cookie']
	c=c.split('; ')
	lis=[]
	for a in c:
		if 'MUSIC_U' in a:
			lis.append(a)
		if 'NMTID' in a:
			lis.append(a)
		if '__csrf' in a:
			lis.append(a)
	ls=';;'.join(lis)
	ls=ls.split(';;')
	lis=[]
	for path in ls:
		if 'Path'not in path:
			lis.append(path)
	lis=str(lis).replace('[','')
	lis=str(lis).replace(']','')
	lis=str(lis).replace('=','\": \"')
	lis=str(lis).replace(',',',\n')
	lis=str(lis).replace(' ','')
	lis=str(lis).replace('\'','\"')
	tem="\"__remember_me\": \"true\"\n"
	result='{\n'+lis+',\n'+tem+'}'
	return result

'''
模型0
不携带任何参数的请求
'''
def model_0(part):
	r=requests.get(server+part,cookies=cookies)
	return json.loads(r.text)

'''
模型1
携带uid参数
'''
def model_1(part,uid):
	params={
	'uid':uid
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

'''
模型2
携带uid和limit(限制)
'''
def model_2(part,uid,limit):
	params={
	'uid':uid,
	'limit':limit
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

'''
模型3
只携带limit的请求
'''
def model_limit(part,limit):
	params={
	'limit':limit
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

'''
模型4
只携带id的请求
'''
def model_id(part,uid):
	params={
	'id':uid
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

'''
模型5
携带ids的请求
'''
def model_ids(part,uid):
	params={
	'ids':uid
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

'''
模型6
携带id和limit的请求
'''
def model_lid(part,uid,limit):
	params={
	'id':uid,
	'limit':limit
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

'''
特殊模型0
携带order,id和limit的歌手歌曲请求
'''
def singer_hot(part,uid,limit):
	params={
	'order':'hot',
	'id':uid,
	'limit':limit
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return r.text

'''
特殊模型1
携带limit的收藏的歌手列表请求
'''
def sublist(part):
	params={
	'limit':'50'
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)


'''
特殊模型2
携带limit的关键词搜索请求
'''
def search_all(part,keywords,limit):
	params={
	'keywords':keywords,
	'limit': limit
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

'''
特殊模型3
携带id,type和limit的热评请求
'''
def hot_comment(part,uid,limit,type_id):
	params={
	'id':uid,
	'type':type_id,
	'limit':limit
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

'''
特殊模型4
携带date的历史日推请求
'''
def history_recommend(part,date):
	params={
	'date':date
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

'''
特殊模型5
携带mvid的MV请求
'''
def mvid(part,uid):
	params={
	'mvid':uid
	}
	r=requests.get(server+part,cookies=cookies)
	return json.loads(r.text)

'''
自动下载音乐设置开启时
会调用此函数返回下载指令
'''
def auto_dl(url,name,music_type):
	act='wget '+url+' -O '+read.dl_dir+'/音乐/'+name+'.'+music_type
	return act

'''
自动下载歌词设置开启时
会调用此函数写入歌词
'''
def auto_lyric(text,name):
	with open(read.dl_dir+'/歌词/'+name+'.txt','w')as f:
		f.write(text)


'''
根据请求结果过滤出歌单ID
并以列表返回
'''
def get_online_ids(lis):
	ud=[]
	for ele in lis:
		uid=str(ele['id'])
		ud.append(uid)
	return ud

'''
根据传入的歌曲ID和用户的命名设置
返回最终命名
'''
def info_limit(uid):
	result=model_ids('song/detail',uid)
	for ele in result['songs']:
		name=ele['name']
		uid=str(ele['id'])
		ar=ele['ar'][0]['name']
		name=name.replace(' ','_')
		name=name.replace('(','_')
		name=name.replace(')','')
		name=name.replace('\'','')
		ar=ar.replace(' ','_')
		ar=ar.replace('(','_')
		ar=ar.replace(')','')
		ar=ar.replace('\'','')
		if read.music_dltype=='0':
			return name+'-'+ar
		else:
			return ar+'-'+name

'''
歌单的格式化输出
同时检查用户设置并决定写入歌单名称
'''
def info_list(lis):
	ud=[]
	for ele in lis:
		name=ele['name']
		uid=str(ele['id'])
		ud.append(uid)
		def ar(lis):
			arid=[]
			arname=[]
			for ele in lis:
				arid.append(str(ele['id']))
				arname.append(ele['name'])
			return dict(zip(arid,arname))
		ar=ar(ele['ar'])
		print('\n歌名: '+name+'\n歌曲ID: '+uid+'\n'+'歌手名: '+' , '.join(str(i) for i in ar.values())+'\n'+'歌手ID: '+' , '.join(str(i) for i in ar.keys())+'\n'+'所属专辑名: '+ele['al']['name']+'\n'+'所属专辑ID: '+str(ele['al']['id']),end='\n')
	if read.auto_id==True:
		listname=input('\n检测到你开启了自动保存列表功能,请输入列表名:')
		with open(read.dl_dir+'/列表/'+listname,'w')as f:
			f.write('\n'.join(ud))

'''
专辑的格式化输出
'''
def info_real(lis):
	for ele in lis:
		name=ele['name']
		uid=str(ele['id'])
		def ar(lis):
			arid=[]
			arname=[]
			for ele in lis:
				arid.append(str(ele['id']))
				arname.append(ele['name'])
			return dict(zip(arid,arname))
		ar=ar(ele['ar'])
		print('\n歌名: '+name+'\n歌曲ID: '+uid+'\n'+'歌手名: '+' , '.join(str(i) for i in ar.values())+'\n'+'歌手ID: '+' , '.join(str(i) for i in ar.keys())+'\n'+'所属专辑名: '+ele['al']['name']+'\n'+'所属专辑ID: '+str(ele['al']['id']),end='\n')

##获取文件hash
def get_hash(path):
	h=hashlib.sha1()
	zero=0
	with open(path,'rb')as f:
		while zero!=b'':
			zero=f.read(1024)
			h.update(zero)
	return h.hexdigest()

##获取hash与文件名对照的字典
def get_dirhash():
	songs=os.listdir(read.music_dir)
	songs_name=[]
	songs_hash=[]
	for song in songs:
		songs_hash.append(get_hash(read.music_dir+song))
		songs_name.append(song)
	songs_list=dict(zip(songs_name,songs_hash))
	return songs_list

##美化输出序号和列表内容
def show_ls(names):
	lenth=len(names)-1
	zero=0
	while zero<=lenth:
		print('\033[1;35;44m'+str(zero)+'.\033[0m | \033[0m\033[1;36m'+str(names[zero])+'\033[0m')
		zero+=1

##通过输入序号生成歌曲的hash列表
def make_list(ipt):
	ids=ipt.split(' ')
	songs_name=get_dirhash()
	lenth=len(songs_name)
	ids_list=dict(zip(range(0,lenth),songs_name))
	name_list=[]
	for i in ids:
		name=ids_list[int(i)]
		name_list.append(name)
	hash_list=[]
	for name in name_list:
		hsh=songs_name[name]
		hash_list.append(hsh)
	return hash_list

##通过hash列表返回歌曲名
def back_name(hash_list):
	songs_list=dict(zip(list(get_dirhash().values()),list(get_dirhash().keys())))
	name_list=[]
	for hsh in hash_list:
		name_list.append(songs_list[hsh])
	return name_list

##通过列表播放歌曲
def play(thing,act):
	if thing=='a':
		os.system(act+read.music_dir+'*')
	else:
		for name in thing:
			name=read.get_good_name(name)
			os.system(act+read.music_dir+name)

##写入hash到文件
def write_into(ipt,list_name):
	hash_list=make_list(ipt)
	with open(read.list_dir+list_name,'w')as f:
		f.write('\n'.join(hash_list)+'\n')

##通过hash播放歌曲
def play_hash(hsh):
	songs_list=dict(zip(list(get_dirhash().values()),list(get_dirhash().keys())))
	name=songs_list[hsh]
	name=read.get_good_name(name)
	os.system(read.player_core+read.music_dir+name)

##通过输入序号返回歌单的hash列表
def back_hash(ipt):
	ls=os.listdir(read.list_dir)
	lenth=len(ls)
	list_list=dict(zip(range(0,lenth),ls))
	with open(read.list_dir+list_list[int(ipt)])as f:
		f=f.read()
	f=f.split('\n')
	return f[:-1]

##根据输入序号获取歌单路径
def get_path(ipt):
	ls=os.listdir(read.list_dir)
	lenth=len(ls)
	list_list=dict(zip(range(0,lenth),ls))
	return read.list_dir+list_list[int(ipt)]

##删除歌单文件
def rm_ls(ipt):
	list_list=get_path(ipt)
	os.system('rm -rf '+list_list)

##收藏音乐
def like(ipt):
	hash_list=make_list(ipt)
	with open(read.list_dir+'我的收藏','a')as f:
		f.write('\n'.join(hash_list)+'\n')

##删除所有
def dl_all_file():
	os.system('rm -rf '+read.list_dir+'*')

##清空所有
def clear_all():
	ls=os.listdir(read.list_dir)
	os.system('rm -rf '+read.list_dir+'*')
	for l in ls:
		os.system('touch '+read.list_dir+l)

##获取补集
def get_b(ipt,hsh,path):
	if ipt=='a':
		os.system('rm -rf '+path)
		os.system('touch '+path)
	else:
		ls=ipt.split(' ')
		wd=[]
		for i in ls:
			wd.append(hsh[int(i)])
		b=list(set(hsh)-(set(wd)))
		return b

##删除歌单内音乐
def rm_ls_inside(b,path):
	os.system('rm -rf '+path)
	with open(path,'w')as f:
		f.write('\n'.join(b)+'\n')

##新旧歌单作比较
def compare(b):
	nms=back_name(b)
	os.system('clear')
	show_ls(nms)