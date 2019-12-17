# encoding=utf-8
# @Author :Alan
# @Time : 2019/12/4 16:40
# @File : getTicketPrice.PY
import re
import time
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class priGet(object):
	def __init__(self,driver):
		self.driver = driver
	def getstring(self):
		#先滑动到能看到信息的位置
		self.driver.execute_script('document.getElementsByClassName("frame-main-cont-body")[2].scrollTop=500')
		time.sleep(3)
		#读取信息并返回string
		priceFr=self.driver.find_element_by_class_name('oD0')
		time.sleep(1)
		self.driver.switch_to_frame(priceFr)

		ele = self.driver.find_elements_by_xpath('//div[@style="line-height: 20px; font-size: 12px;"]')
		if ele !=[]:
			string = str(ele[1].text.encode('utf-8'))
		else:
			try:
				ele = self.driver.find_element_by_xpath('//*[@id="content"]/b')
				string = str(ele.text[50:120].encode('utf-8'))
			except NoSuchElementException:
				string = '票款共计0.0元'
		print string
		return  string

class getPrice(object):
	def __init__(self,driver):
		self.driver = driver
		self.priGet=priGet(self.driver)
		self.string=self.priGet.getstring()

	def getprice(self):
		parton = "[0-9]+\\.[0-9]+"
		string_list = self.string.replace('，', ',').split(',')
		if u'应退票款' in self.string:
			#string_list = self.string.replace('，', ',').split(',')
			for list in string_list:
				if u'应退票款' in list:
					result2 = re.findall(parton,str(list))[0]
					result = float(result2)
					result = result * (-1)

		elif u'票款共计' in self.string:
			for list in string_list:
				if u'票款共计' in list:
					result2 = re.findall(parton,str(list))[0]
					result = float(result2)
		else:
			result = 0.0
		return result


# if __name__=="__main__":
#
# 	driver = webdriver.Chrome()
# 	time.sleep(40)
# 	getprice = getPrice(driver)
# 	price = getprice.getprice()
# 	print price
