import requests
import json
from . import read

'''
读取配置
'''
server=read.server
cookies=read.cookies

'''
登录的封装
不知道为什么不能用...一直返回错误信息
可能是因为网易云加了登录验证功能
'''
def login(part,phone,pwd):
	params={
	'cellphone':phone,
	'password':pwd
	}
	r=requests.get(server+part,params=params)
	cookies=requests.utils.dict_from_cookiejar(r.cookies)
	cookies=str(cookies).replace('\'','\"')
	return r.text

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
		name=name.replace('\'','')
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