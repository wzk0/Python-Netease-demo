import requests
import json
from . import read

server=read.server
cookies=read.cookies

def login(part,phone,pwd):
	params={'cellphone':phone,'password':pwd}
	r=requests.get(server+part,params=params)
	cookies=requests.utils.dict_from_cookiejar(r.cookies)
	cookies=str(cookies).replace('\'','\"')
	return cookies

def detail(part,uid):
	params={'uid':uid}
	r=requests.get(server+part,params=params)
	return json.loads(r.text)