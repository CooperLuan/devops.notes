'''
Created by auto_sdk on 2014-12-17 17:22:51
'''
from top.api.base import RestApi
class ItemPropimgDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.num_iid = None

	def getapiname(self):
		return 'taobao.item.propimg.delete'
