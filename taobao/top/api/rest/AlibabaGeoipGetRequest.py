'''
Created by auto_sdk on 2014-12-17 17:22:51
'''
from top.api.base import RestApi
class AlibabaGeoipGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ip = None
		self.language = None

	def getapiname(self):
		return 'alibaba.geoip.get'
