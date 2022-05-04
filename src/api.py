import requests
import json
from . import read

server=read.server
cookies=read.cookies

def login(part,phone,pwd):
	params={
	'cellphone':phone,
	'password':pwd
	}
	r=requests.get(server+part,params=params)
	cookies=requests.utils.dict_from_cookiejar(r.cookies)
	cookies=str(cookies).replace('\'','\"')
	return r.text

def model_0(part):
	r=requests.get(server+part,cookies=cookies)
	return json.loads(r.text)

def model_1(part,uid):
	params={
	'uid':uid
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

def model_2(part,uid,limit):
	params={
	'uid':uid,
	'limit':limit
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

def singer_hot(part,uid,limit):
	params={
	'order':'hot',
	'id':uid,
	'limit':limit
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return r.text

def sublist(part):
	params={
	'limit':'50'
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

def model_limit(part,limit):
	params={
	'limit':limit
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

def model_id(part,uid):
	params={
	'id':uid
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

def model_ids(part,uid):
	params={
	'ids':uid
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

def model_lid(part,uid,limit):
	params={
	'id':uid,
	'limit':limit
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

def search_all(part,keywords,limit):
	params={
	'keywords':keywords,
	'limit': limit
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

def hot_comment(part,uid,limit,type_id):
	params={
	'id':uid,
	'type':type_id,
	'limit':limit
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

def hot_search():
	part='search/hot/detail'
	r=requests.get(server+part,cookies=cookies)
	return json.loads(r.text)

def history_recommend(part,date):
	params={
	'date':date
	}
	r=requests.get(server+part,params=params,cookies=cookies)
	return json.loads(r.text)

def mvid(part,uid):
	params={
	'mvid':uid
	}
	r=requests.get(server+part,cookies=cookies)
	return json.loads(r.text)

def auto_dl(url,name,music_type):
	act='wget '+url+' -O '+read.dl_dir+'/音乐/'+name+'.'+music_type
	return act

def auto_lyric(text,name):
	with open(read.dl_dir+'/歌词/'+name+'.txt','w')as f:
		f.write(text)

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

def info_limit(uid):
	result=model_ids('song/detail',uid)
	for ele in result['songs']:
		name=ele['name']
		uid=str(ele['id'])
		ar=ele['ar'][0]['name']
		name=name.replace(' ','_')
		name=name.replace('(','_')
		name=name.replace(')','')
		ar=ar.replace(' ','_')
		ar=ar.replace('(','_')
		ar=ar.replace(')','')
		if read.music_dltype=='0':
			return name+'-'+ar
		else:
			return ar+'-'+name