'''
Created by auto_sdk on 2014-12-17 17:22:51
'''
from top.api.base import RestApi
class MarketingPromotionKfcRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.promotion_desc = None
		self.promotion_title = None

	def getapiname(self):
		return 'taobao.marketing.promotion.kfc'
