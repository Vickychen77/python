# —*— coding:utf-8 -*-
import requests

'''Please input base_url and file_path'''
base_url='http://www.meizu.com'
file_path='/Users/chenqi1/Desktop/params.txt'

total_para=open(file_path,'r')
parameters=total_para.readlines()
i=0
for para in parameters:
	url=base_url
	real_para=str(para).strip()

	#update parameters
	payload={'param1': 2921205, 'param2': 'fdsfXdEc2'}
	
	r=requests.post(url,data=payload)
	i=i+1
	print(r.json())
	

