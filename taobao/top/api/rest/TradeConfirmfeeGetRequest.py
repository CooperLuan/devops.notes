'''
Created by auto_sdk on 2014-12-17 17:22:51
'''
from top.api.base import RestApi
class TradeConfirmfeeGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.is_detail = None
		self.tid = None

	def getapiname(self):
		return 'taobao.trade.confirmfee.get'
