# encoding=utf-8
# @Author :Alan
# @Time : 2019/12/4 11:47
# @File : main.PY

from selenium import webdriver
import time
import readconfig
import  getTicketPrice

totalSum=0.0
url ="http://mail.163.com"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
#用用户名密码登录
driver.maximize_window()
driver.find_element_by_id('lbNormal').click()

#输入用户名和密码
config = readconfig.readexcel('config.xlsx')
account = config.read()[0]
pwd = config.read()[1]
frame = driver.find_element_by_xpath('//*[@id="loginDiv"]/iframe')
driver.switch_to_frame(frame)
time.sleep(2)
ac_ele = driver.find_element_by_name('email')
ac_ele.clear()
ac_ele.send_keys(account)
time.sleep(3)
pwd_ele = driver.find_element_by_name('password')
#pwd_ele = driver.find_element_by_xpath('//input[@name="password"]')
pwd_ele.send_keys(pwd)
time.sleep(3)
driver.find_element_by_id('dologin').click()

#点击更多文件夹
time.sleep(5)
driver.find_element_by_id('_mail_component_87_87').click()
time.sleep(2)
driver.find_element_by_id('_mail_component_229_229').click()
#driver.find_element_by_xpath('//span[@title="12306"]').click()
time.sleep(2)

#获取每页的邮件列表
siglePageList = driver.find_elements_by_xpath('//*[@class="tv0"]/div')
sigleId= str(siglePageList[1].get_attribute('id'))
driver.find_element_by_id(sigleId).click()

while True:
	price = 0.0

	#调用getTicketPrice
	getprice = getTicketPrice.getPrice(driver)
	price = getprice.getprice()
	print price
	totalSum = totalSum+price
	driver.switch_to_default_content()
	button = driver.find_elements_by_xpath('//div[@role="button" and contains(@title,"下一封")]')
	button[0].click()
	time.sleep(3)
	try:
		driver.find_element_by_xpath('//div[@role="button" and contains(@title,"无下一封")]')
		time.sleep(2)
		break
	except Exception:
		continue


print totalSum
