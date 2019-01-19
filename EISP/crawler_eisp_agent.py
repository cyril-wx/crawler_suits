#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


if False:
	import os
	cmd1 = "export http_proxy=http://F3200278:Foxconn%402016@10.191.131.43:3128 ;"
	cmd2 = "export https_proxy=http://F3200278:Foxconn%402016@10.191.131.43:3128 ;"
	cmd3 = " sudo pip3 install bs4 ;"
	cmd4 = " sudo pip3 install requests ;"
	cmd5 = " sudo pip3 install requests_ntlm ;"
	cmd = cmd1+cmd2+cmd3+cmd4+cmd5
	os.system(cmd)

from bs4 import BeautifulSoup
#from crawler_eisp_agent import getEISPHTML
import requests
from requests_ntlm import HttpNtlmAuth
	
def getPunchTime(headers, proxies, session, startDate, endDate, HankCard=""):
	print('================getPunchTime BEGIN================')
	url="http://eisp.idpbg.efoxconn.com/WEB/PersonnelInfo/PersonnelCardInfo.aspx?FormTypeID=&Module_ID=356&Item_ID=262"
	headers['Referer']="http://eisp.idpbg.efoxconn.com/WEB/PersonnelInfo/PersonnelCardInfo.aspx?FormTypeID=&Module_ID=356&Item_ID=262"
	headers['Host']='eisp.idpbg.efoxconn.com'
	
	data={}
	data['__VIEWSTATEGENERATOR']='43D78820'
	data['imgbtn_Query.x']='37'
	data['imgbtn_Query.y']='8'
#	data['txt_CardDate']='2018-11-01'
#	data['txt_EndDate']='2018-11-13'
	data['txt_CardDate']=startDate
	data['txt_EndDate']=endDate
	data['ddl_HankCard']=HankCard	# 0:否 1:是 “”:全部
	data['txt_PageNum']=''
	data['__VIEWSTATE']='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'
	
	res=session.post(url, headers=headers, data=data, proxies=proxies)
	print(url)
	print("StatusCode:",res.status_code)
	print("headers=",headers)
	print(res.cookies)

	with open("./getPunchTime.html","w") as f:
		f.write(res.text)
	print('================getPunchTime END================')
	
def getPersonalInfo(headers, proxies, session):
	print("=============getPersonalInfo BEGIN=============")	
	from requests.cookies import RequestsCookieJar	

	url="http://eisp.idpbg.efoxconn.com/WEB/EmpBaseInfo/EmpPernonelInfo.aspx?FormTypeID=&Module_ID=515&Item_ID=595"
	data={}
	data['Module_ID']="515"
	data['Item_ID']="595"	
	data['FormTypeID']=""

#	headers['Cookie']=''.join(["ASP.NET_SessionId=",session_co[1],"; EISPCookie=USER_NO=F1235027&USER_NAME=%e8%94%a3%e7%b6%ad%e7%86%99&IS_FOREIGN=0&SESSION_ID=",session_co[1],"&FIH_TOKEN="])
	headers['Referer']="http://eisp.idpbg.efoxconn.com/WEB/Public/TableTypeDetail.aspx?Module_ID=515"
	headers['Host']="eisp.idpbg.efoxconn.com"
	
	res=session.post(url, data=data, headers=headers)
	
	print(res.url)
	print("StatusCode:",res.status_code)
	print(res.headers)
	print(res.cookies)
	#print(res.text)
	for cookie in res.cookies:
			print(cookie.name)
			print(cookie.value)	
	with open("./PersonalInfo.html","w") as f:
		f.write(res.text)
	print("=============getPersonalInfo END=============")


def loginEISP(headers, proxies, session):
	print("=============loginEISP BEGIN=============")
	
#	r=requests.get("http://10.195.226.130:80",auth=HttpNtlmAuth('dpbg\\F1235027','Cyril201810'), proxies=proxies)
	r=session.get("http://10.195.226.130:80", headers=headers, proxies=proxies)
	print(r.status_code)
	print(r.headers)
	print(r.cookies)
	#print(r.text)
	for cookie in r.cookies:
		print(cookie.name)
		print(cookie.value)
		print("=============loginEISP END=============")
		return session

def getEISPHTML(EISPUser, EISPPwd):
	'''getEISPHTML function 保存EISP相关HTML页面
        已实现 1>.getPersonalInfo()
               2>.getPunchTime()
	'''
	headers={}
	headers['Accept']="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
	headers['Accept-Encoding']="gzip,deflate,sdch"
	headers['Accept-Language']="zh-CN,zh;q=0.8,zh-TW;q=0.6"
	headers['Connection']="keep-alive"
	headers['User-Agent']="Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36"

	proxies={}
	proxies['http']="http://F3200278:Foxconn%402016@10.191.131.43:3128"
	proxies['https']="http://F3200278:Foxconn%402016@10.191.131.43:3128"

	# 通过Session类新建一个会话
	session = requests.Session()
	session.auth = HttpNtlmAuth('dpbg\\' + EISPUser, EISPPwd)
	session=loginEISP(headers=headers, proxies=proxies, session=session)

#	getPersonalInfo(headers, proxies, session)

	getPunchTime(headers, proxies, session, '2018-11-01', '2018-11-30')
	

def parse_PunchTime_HTML():
	"""
	parse_PunchTime_HTML function 解析考勤HTML数据
	"""
	print("================ parse_PunchTime_HTML BEGIN ================")
	with open("./getPunchTime.html","r") as f:
		html_str=f.read()
	soup = BeautifulSoup(html_str,'html.parser')

#	print(soup.text) #去掉所有标签，只留文本
#	tab_title=soup.find('tr',class_="xpth")

	tab_data=soup.find_all('td')
	print("================ parse_PunchTime_HTML END ================")
	return getTableList(col=7, tab_data=tab_data)  #表单数据为7列
	

def getTableList(col,tab_data):
	"""getTableList function 将源数据转化为列表
	param 'col': table columns
	param 'tab_data': original data type<soup.find_all> 
	"""
	data_all=[]
	data_record=[]
	i=0
	for item in tab_data:
		if i<col:
			data_record.append(item.text)
			i+=1
		elif i==col:
			data_all.append(data_record)
			data_record=[]
			i=0
		else:
			pass
	del data_all[-1]
	return data_all

def calcuPunchTimeByDay(arrayList):
	'''calcuPunchTimeByDay function 计算每日加班时数
	
	'''
	print("================ calcuPunchTimeByDay BEGIN ================")
	ls=arrayList
	dic_punchdate=dict()
	list_punchtime=list()
	for i in range(len(ls)):
		if i>0:
			if ls[i][5]!=ls[i-1][5]:
				list_punchtime=list()
			list_punchtime.append(ls[i][6])
			dic_punchdate[ls[i][5]]=list_punchtime

#	print(dic_punchdate) # 此处已将刷卡时间转化成如下格式
			     # {'2018/11/01': ['07:51:09', '17:41:25', '19:31:43'], 
			     #	'2018/11/02': ['07:57:33', '18:40:52'], ...}
	print("刷卡日期 : 星期数 : 加班时数(H)")
	total=0 #总加班时数
	for key in dic_punchdate.keys():
		dic_punchdate[key].sort()
		week = calcuWeek(key) #计算星期几
		work_class=judgeClass(dic_punchdate[key][0]) #计算班别
		
		if work_class == 0: #白班
			timeinterval_hr=calcuTimeInterval('17:30:00',dic_punchdate[key][-1]) #这是白班加班的计算方法
			if week == 6 or week == 7:
				timeinterval_hr=calcuTimeInterval(dic_punchdate[key][0],dic_punchdate[key][-1])-1.5 #星期六 星期天 算上下班打卡时间
		elif work_class == 1: #中班
			timeinterval_hr=calcuTimeInterval('12:00:00',dic_punchdate[key][-1]) #这是中班加班的计算方法
			if week == 6 or week ==7:
				timeinterval_hr=calcuTimeInterval(dic_punchdate[key][0],dic_punchdate[key][-1])-0.5 #星期六 星期天 算上下班打卡时间
		elif work_class == 2: #晚班 
			timeinterval_hr=calcuTimeInterval('22:00:00',dic_punchdate[key][-1]) #这是晚班加班的计算方法
			if week == 6 or week ==7:
				timeinterval_hr=calcuTimeInterval(dic_punchdate[key][0],dic_punchdate[key][-1])-1 #星期六 星期天 算上下班打卡时间
		else: #打卡时间异常,不计加班时数
			timeinterval_hr=0
		
		timeinterval_hr=calcuTimeInterval_calibration(timeinterval_hr, work_class, week)

		total=total+timeinterval_hr
		print(key," : ", week, " : ", timeinterval_hr)
		
	print("加班时数(H) Total:",total)
	print("================ calcuPunchTimeByDay END ================")

def calcuTimeInterval_calibration(timeinterval, work_class, week):
	'''calcuTimeInterval_calibration 时间差值校准 根据下班打卡时间差及班别判断
	param ‘timeinterval’: %H 未校准过的时间
	param 'work_class': int 班别  白0/中1/晚2
	param 'week': int 星期数
	'''
	threshold=0.09 #设定时间阈值为0.09h, 即约为5分钟
	if work_class==0:
		point=0.5
	elif work_class==1 or work_class==2:
		point=1
	else: # 异常
		point=0
	
	if timeinterval >= 2-threshold and timeinterval < 4: # 不超过4H的打卡时间都算正常2h
		timeinterval=2
	elif timeinterval > 0 and timeinterval < 2:
#		timeinterval=float("%.2f" %timeinterval)
		tmp=timeinterval-int(timeinterval)
		if tmp > point - threshold:
			timeinterval=int(timeinterval) + point #提前5分钟打卡算一个小时 
		else:					#即使补偿5分钟也达不到0.5h或1.0h则只算.0h或.5h
			timeinterval=int(timeinterval) + point - 0.5
	elif timeinterval >= 4-threshold and timeinterval < 12 and (week == 6 or week ==7):
#		timeinterval=float("%.2f" %timeinterval)
		tmp=timeinterval-int(timeinterval)
		if tmp > point - threshold:
			timeinterval=int(timeinterval) + point #提前5分钟打卡算一个小时
		else:                                   #即使补偿5分钟也达不到0.5h或1.0h则只算.0h或.5h
			timeinterval=int(timeinterval) + point - 0.5
	else:   #其他情况算异常，不计当天加班时数
		timeinterval=0
	return timeinterval

def judgeClass(puncktime):
	'''judgeClass function 判断班别
	param 'puncktime': "%H:%M:%S" # 以上班打卡时间计，判断班别
	## 白班 0
	## 中班 1
	## 晚班 2
	'''	
	threshold=2	# 设定判断阈值为2个小时

	if calcuTimeInterval("08:00:00",puncktime) < 2 :
		#print("白班")
		return 0
	elif calcuTimeInterval("13:00:00",puncktime) < 2 :
		#print("中班")
		return 1
	elif calcuTimeInterval("20:00:00",puncktime) < 2 :
		#print("晚班")
		return 2
	else:
		#print("Unknow Work Class")
		return -1
		
def calcuWeek(date=""):
	'''calcuWeek function 计算星期几
	param 'date':default "" #默认为空，即计算今天星期几
	param 'date': '%Y/%M/%D' #给指定日期，计算当天星期几:
	'''
	import time
	import datetime
	if date:
		dsplit=date.split("/",2)
		anyday=datetime.date(int(dsplit[0]),int(dsplit[1]),int(dsplit[2])).strftime("%w")
		return int(anyday)
	else:
		today=int(time.strftime("%w"))
		return int(today)
		 
	
def calcuTimeInterval(startTime, endTime):
	'''calcuTimeInterval function 计算时间差
	param 'startTime': "%H:%M:%S"
	param 'endTime': "%H:%M:%S"
	return 'timeinterval': int , hour
	'''
	import datetime
	d1=datetime.datetime.strptime(str(startTime), "%H:%M:%S")	
	d2=datetime.datetime.strptime(str(endTime), "%H:%M:%S")
	
	timeinterval_hr=(d2-d1).seconds/3600
	if timeinterval_hr > 12:
		timeinterval_hr=(d1-d2).seconds/3600
#	print(timeinterval_hr)
	return timeinterval_hr
	

if __name__ == "__main__":

	getEISPHTML('F1235027','Cyril201811')
	#getEISPHTML('F1228225','Adpbg4a4')
	#getEISPHTML('F1233396', "Zf201811")
	#getEISPHTML('F1235028','xiao123.')
	#getEISPHTML('F1232399','Victor28')

	ls=parse_PunchTime_HTML() 
	for item in ls:
		print(item)

	# 计算超时加班时数
	calcuPunchTimeByDay(ls)

	
