# -*- coding:utf-8 -*-
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import random
##选用开发者模式，创建一个浏览器对象，可避免被检测到是selenium模拟浏览器
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
browser = webdriver.Chrome(options=option)

#browser = webdriver.PhantomJS(executable_path='/Users/cyril/Public/phantomjs-2.1.1-macosx/bin/phantomjs')
#browser.set_page_load_timeout(30)
def get_track(distance ):
    track = []
    current = 0
    mid = distance * (4/5)
    t = 2
    v = 0
    v1  = 0
    a1 = 2
    a = 4
    while current < distance:
        if current < mid:
            move = v * t + 1/2 * a *t * t
            current += move
            track.append(round(move))
            v = v + a*t
        else:
            move1 = v1 * t + 1/2 * a1 *t *t
            current += move1
            track.append(round(move1))
            v1 = v1 + a1*t

    return track
def main():
    browser.get('https://login.taobao.com/member/login.jhtml?')
    # browser.find_element_by_id('J_Quick2Static').click()#点击密码登录按钮，选择用密码方式登录,如打开浏览器的界面是登录，此行可省略

    input = browser.find_element_by_xpath("//*[@id='TPL_username_1']")
    #input.send_keys('18273494490')
    input.send_keys("18574721996")
    input.send_keys(Keys.ENTER)
    password = browser.find_element_by_id('TPL_password_1')
    #password.send_keys('Cyril202003*')
    password.send_keys("Cyril2020")
    time.sleep(1)
    password.send_keys(Keys.ENTER)
    time.sleep(1)
    password1 = browser.find_element_by_id('TPL_password_1')
    password1.send_keys('Cyril202003*')
    slider = browser.find_element_by_xpath("//*[@id='nc_1_n1z']")#找到滑动按钮
    ActionChains(browser).click_and_hold(slider).perform()
    track = get_track(2000)#模拟运动轨迹，速度先快后慢
    for x in track:

        ActionChains(browser).drag_and_drop_by_offset(slider,xoffset=x,yoffset=random.randint(1,3)).perform()
    ActionChains(browser).release().perform()
    denglu =browser.find_element_by_xpath('//*[@id="J_SubmitStatic"]')
    denglu.click()#点击登录按钮
    time.sleep(3)
    browser.get_screenshot_as_file('./scraping_2.png')

    browser.find_element_by_id('bought').click()#进入自己的账户界面，点击全部订单
    time.sleep(2)
    time.sleep(3)
    browser.get_screenshot_as_file('./scraping_3.png')

if __name__ == '__main__':
    main()
