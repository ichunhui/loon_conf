# !/usr/bin/python
# encoding:utf-8

import requests

'''
东东工厂互助码api
http://api.turinglabs.net/api/v1/jd/ddfactory/create/互助码/

查看上车人数
http://api.turinglabs.net/api/v1/jd/ddfactory/count/

京喜工厂互助码api
http://api.turinglabs.net/api/v1/jd/jxfactory/create/互助码/

查看上车人数
http://api.turinglabs.net/api/v1/jd/jxfactory/count/

种豆提交互助码api
http://api.turinglabs.net/api/v1/jd/bean/create/互助码/

查看上车人数
http://api.turinglabs.net/api/v1/jd/bean/count/

农场提交互助码api
http://api.turinglabs.net/api/v1/jd/farm/create/互助码/

查看上车人数
http://api.turinglabs.net/api/v1/jd/farm/count/

萌宠提交互助码api
http://api.turinglabs.net/api/v1/jd/pet/create/互助码/

查看上车人数
http://api.turinglabs.net/api/v1/jd/pet/count/

查看数据库清空时间
http://api.turinglabs.net/api/v1/jd/cleantimeinfo/
'''

#ddfactory = 'http://api.turinglabs.net/api/v1/jd/ddfactory/create/'
#ddfactorydata = ['P04z54XCjVWnYaS5jYJDGjx3nhIkwk0', 'P04z54XCjVWnYaS5m9cZxGCpxw083240A7kvA'] #1,3

#jxfactory = 'http://api.turinglabs.net/api/v1/jd/jxfactory/create/'
#jxfactorydata = ['U2URkN81Loo84dPu_sj94Q=='] #1

bean = 'http://api.turinglabs.net/api/v1/jd/bean/create/'
beandata = ['ucpjlpwnmy2nk75jrfodjhhiqa', 'igefhjvuw6xvscczs5ojykn7nodbt3wbidrtxyi', '2vgtxj43q3jqznayta53va7id6b3lsggdiq7o4a', 't7obxmpebrxkd25fys3tfytdhfiu5b4qpcqh7oq']

farm = 'http://api.turinglabs.net/api/v1/jd/farm/create/'
farmdata = ['83aead50c97541259ca5d84df0922c7f', '325cdaf9627d485a9193dd55de57ae27', '43f855a035094b92bfb825948ee0df91', '804dc4a80e61463ca1ffac92a0010185']

pet = 'http://api.turinglabs.net/api/v1/jd/pet/create/'
petdata = ['MTE1NDQ5OTUwMDAwMDAwMzkwNTAxMTE=', 'MTE1NDAxNzgwMDAwMDAwMzkzMTEwMTU=', 'MTAxODExNTM5NDAwMDAwMDA0MDc2MTMxNw==', 'MTE1NDQ5OTIwMDAwMDAwNDI0OTU4Mjk=']

def get(link, data):
	for i in data:
		url = link + i
		print(url)
		r=requests.get(url)
		print(r.text)

get(ddfactory,ddfactorydata)
get(jxfactory,jxfactorydata)
get(bean,beandata)
get(farm,farmdata)
get(pet,petdata)

print("finished")




