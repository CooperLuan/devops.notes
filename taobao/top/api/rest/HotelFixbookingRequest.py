'''
Created by auto_sdk on 2014-12-17 17:22:51
'''
from top.api.base import RestApi
class HotelFixbookingRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.booking_id = None
		self.cou_code = None
		self.hn_code = None
		self.rev_count = None

	def getapiname(self):
		return 'taobao.hotel.fixbooking'
