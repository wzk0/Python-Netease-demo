import yaml
import json

conf=yaml.load(open('src/conf.yaml'),Loader=yaml.FullLoader)
server=conf['server']
with open("src/cookies.json",'r', encoding='UTF-8') as f:
	cookies=json.load(f)