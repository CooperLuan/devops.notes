'''
Created by auto_sdk on 2014-12-17 17:22:51
'''
from top.api.base import RestApi
class FenxiaoGradesGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'taobao.fenxiao.grades.get'
