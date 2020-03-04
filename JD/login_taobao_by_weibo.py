# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
class taobao_infos:

	def __init__(self, url):
		self.url = 'https://login.taobao.com/member/login.jhtml'
		# self.browser = webdriver.Chrome()
		self.browser = webdriver.PhantomJS(executable_path='/Users/cyril/Public/phantomjs-2.1.1-macosx/bin/phantomjs')
		self.wait = WebDriverWait(self.browser, 10)

	# 处理登陆信息
	def login(self):
		self.browser.get(self.url)
		#sleep(6)
		#self.browser.find_element_by_xpath('//*[@class="forget-pwd J_Quick2Static"]').click()
		sleep(2)

		# snapshot
		self.browser.get_screenshot_as_file('./log/login_ui.png')

		# choise weibo acc login
		self.browser.find_element_by_xpath('//*[@id="J_OtherLogin"]/a[1]').click()
		sleep(3)

		# snapshot
		self.browser.get_screenshot_as_file('./log/login_weibo_ui.png')

		# username
		self.browser.find_element_by_name('username').send_keys('18574721996')
		sleep(5)

		# pwd
		self.browser.find_element_by_name('password').send_keys('Cyril2020')
		sleep(4)

		# login btn
		#self.browser.find_element_by_xpath('//*[@id="pl_login_logged"]/div[2]/div[7]/div[1]/a/span').click()
		self.browser.find_element_by_xpath('//*[@class="btn_tip"]/a/span').click()
		sleep(10)

		# snapshot
		self.browser.get_screenshot_as_file('./log/after_click_login.png')


url = 'https://login.taobao.com/member/login.jhtml'
#url = 'https://weibo.com/login.php?spm=a2107.1.0.0.347b11d9NIpPdN&entry=taobao&goto=https%3A%2F%2Flogin.taobao.com%2Faso%2Ftvs%3Fdomain%3Dweibo%26sid%3Dd4ad03983a01e3fe8167ed27f44f8320%26target%3D68747470733A2F2F7777772E74616F62616F2E636F6D2F&goto2=https%3A%2F%2Fwww.taobao.com%2F'

a = taobao_infos(url)
a.login()
