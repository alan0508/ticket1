# encoding=utf-8
# @Author :Alan
# @Time : 2019/12/4 10:30
# @File : readconfig.PY
import xlrd

class readexcel(object):
	def __init__(self,file_name):
		#self.file_name=file_name
		self.xl = xlrd.open_workbook(file_name)
	def read(self):
		self.table = self.xl.sheet_by_name('login')
		self.row = self.table.row_values(1)
		for i in range(len(self.row)):
			if isinstance(self.row[i],float):
				self.row[i]=str(int(self.row[i]))
		return self.row

if __name__=="__main__":
	excel = readexcel('config.xlsx')
	excel.read()