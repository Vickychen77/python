'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
'''

import random


# date=input('input date')
# print(date)

data= ('{"count":' + str(
        random.randint(100, 1000)) +
       ',"daily":"2017-11-22","province_id":20,"device":'
       '"phone"}')

print(data)

with open('/Users/chenqi1/Desktop/mysql.txt','r') as files:

    for sql in files.readlines():
        print(sql,end='\n')
