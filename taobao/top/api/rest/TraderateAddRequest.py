'''
Created by auto_sdk on 2014-12-17 17:22:51
'''
from top.api.base import RestApi
class TraderateAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.anony = None
		self.content = None
		self.oid = None
		self.result = None
		self.role = None
		self.tid = None

	def getapiname(self):
		return 'taobao.traderate.add'
