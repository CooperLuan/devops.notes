'''
Created by auto_sdk on 2014-12-17 17:22:51
'''
from top.api.base import RestApi
class TicketItemGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.item_id = None

	def getapiname(self):
		return 'taobao.ticket.item.get'
